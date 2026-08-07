#!/usr/bin/env python3
"""
Simplified chip-tool automation script - Pairing only
"""
import subprocess
import time
import sys
import threading
import argparse
import re
import logging
import glob
from datetime import datetime
from typing import Tuple, Optional

# Node ID for the device
NODE_ID = 2250

# Thread network dataset (example - should be adjusted for your network)
THREAD_DATASET = "hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f"

# PAA certificate path
PAA_TRUST_STORE_PATH = "/home/ubuntu/paa-root-certs"


def setup_logging():
    """
    Setup logging to both console and file.
    Log file name format: YYYYMMDDHHMMSS.log
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    log_filename = f"{timestamp}.log"

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers = []

    detailed_formatter = logging.Formatter(
        '%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(detailed_formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_filename, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    logger.addHandler(file_handler)

    logging.info("=" * 80)
    logging.info("CHIP-Tool Pairing Script")
    logging.info("=" * 80)
    logging.info(f"Log file: {log_filename}")
    logging.info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    return log_filename


def output_reader(proc, logger, prefix="[CHIP-TOOL]"):
    """
    Background thread: Continuously reads and clears the subprocess output.
    """
    try:
        for line in iter(proc.stdout.readline, b''):
            decoded_line = line.decode('utf-8', errors='ignore').strip()
            if decoded_line:
                logger.debug(f"{prefix} {decoded_line}")
    except Exception as e:
        if logger:
            logger.debug(f"{prefix} Reader error: {e}")


def run_command_realtime(cmd: list, timeout: int = 120, logger=None, prefix="[CMD]") -> bool:
    """
    Run a command with real-time output capture.
    Returns: success (bool)
    """
    if logger:
        logger.info(f"{prefix} Executing: {' '.join(cmd)}")
    else:
        print(f"\n{prefix} Executing: {' '.join(cmd)}")

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        reader_thread = threading.Thread(
            target=output_reader,
            args=(proc, logger, prefix),
            daemon=True
        )
        reader_thread.start()

        try:
            return_code = proc.wait(timeout=timeout)
            if return_code == 0:
                if logger:
                    logger.info(f"{prefix} Command completed successfully")
                else:
                    print(f"{prefix} Command completed successfully")
                return True
            else:
                extra = f" (signal {-return_code})" if return_code < 0 else ""
                if logger:
                    logger.error(f"{prefix} Command failed with return code: {return_code}{extra}")
                else:
                    print(f"{prefix} Command failed with return code: {return_code}{extra}")
                return False
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            if logger:
                logger.error(f"{prefix} Command timed out after {timeout} seconds")
            else:
                print(f"{prefix} Command timed out after {timeout} seconds")
            return False
    except FileNotFoundError as e:
        if logger:
            logger.error(f"{prefix} Command not found: {e}")
        else:
            print(f"{prefix} Command not found: {e}")
        return False
    except Exception as e:
        if logger:
            logger.error(f"{prefix} Exception: {e}")
        else:
            print(f"{prefix} Exception: {e}")
        return False


def run_command_and_capture(cmd: list, timeout: int = 30, logger=None) -> Tuple[int, str, str]:
    """
    Run a command and capture its output.
    Returns: (return_code, stdout, stderr)
    """
    if logger:
        logger.info(f"[COMMAND] {' '.join(cmd)}")
    else:
        print(f"\n[COMMAND] {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        if logger:
            if result.stdout:
                logger.debug(f"[STDOUT] {result.stdout}")
            if result.stderr:
                logger.debug(f"[STDERR] {result.stderr}")
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        error_msg = f"Command timed out: {' '.join(cmd)}"
        if logger:
            logger.error(error_msg)
        else:
            print(f"[ERROR] {error_msg}")
        return -1, "", "Timeout"
    except Exception as e:
        error_msg = f"Command failed: {e}"
        if logger:
            logger.error(error_msg)
        else:
            print(f"[ERROR] {error_msg}")
        return -1, "", str(e)


def clean_chip_temp_files(logger=None):
    """
    Clean CHIP temporary files before pairing.
    """
    if logger:
        logger.info("[CLEAN] Cleaning CHIP temporary files...")
    else:
        print("\n[CLEAN] Cleaning CHIP temporary files...")

    files = glob.glob('/tmp/chip_*')
    if not files:
        if logger:
            logger.info("[CLEAN] No /tmp/chip_* files found")
        else:
            print("[CLEAN] No /tmp/chip_* files found")
        return True

    cmd = ["sudo", "rm", "-rf"] + files
    success = run_command_realtime(cmd, timeout=10, logger=logger, prefix="[CLEAN]")
    if success:
        if logger:
            logger.info("[CLEAN] Successfully cleaned /tmp/chip_* files")
        else:
            print("[CLEAN] Successfully cleaned /tmp/chip_* files")
    else:
        if logger:
            logger.warning("[CLEAN] Note: Could not clean temp files (may not exist)")
        else:
            print("[CLEAN] Note: Could not clean temp files (may not exist)")
    return True


def parse_setup_payload(qr_code: str, logger=None) -> Tuple[Optional[int], Optional[int], Optional[str]]:
    """
    Parse the setup payload to extract Passcode and Discriminator.
    Returns: (passcode, discriminator, error_message)
    """
    if logger:
        logger.info(f"[PARSE] Parsing QR code: {qr_code}")
    else:
        print(f"\n[PARSE] Parsing QR code: {qr_code}")

    cmd = ["sudo", "./chip-tool", "payload", "parse-setup-payload", qr_code]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)

    if returncode != 0:
        error_msg = f"Failed to parse payload: {stderr}"
        if logger:
            logger.error(error_msg)
        else:
            print(f"[ERROR] {error_msg}")
        return None, None, stderr

    passcode = None
    discriminator = None

    passcode_match = re.search(r'Passcode[:\s]+(\d+)', stdout, re.IGNORECASE)
    discriminator_match = re.search(r'Discriminator[:\s]+(\d+)', stdout, re.IGNORECASE)

    if passcode_match:
        passcode = int(passcode_match.group(1))
        if logger:
            logger.info(f"[PARSE] Extracted Passcode: {passcode}")
        else:
            print(f"[PARSE] Extracted Passcode: {passcode}")
    else:
        numbers = re.findall(r'\d{4,}', stdout)
        if numbers:
            passcode = int(numbers[0])
            if logger:
                logger.info(f"[PARSE] Extracted Passcode (fallback): {passcode}")
            else:
                print(f"[PARSE] Extracted Passcode (fallback): {passcode}")

    if discriminator_match:
        discriminator = int(discriminator_match.group(1))
        if logger:
            logger.info(f"[PARSE] Extracted Discriminator: {discriminator}")
        else:
            print(f"[PARSE] Extracted Discriminator: {discriminator}")
    else:
        short_numbers = re.findall(r'\d{3,4}(?!\d)', stdout)
        if short_numbers:
            discriminator = int(short_numbers[0])
            if logger:
                logger.info(f"[PARSE] Extracted Discriminator (fallback): {discriminator}")
            else:
                print(f"[PARSE] Extracted Discriminator (fallback): {discriminator}")

    return passcode, discriminator, None


def pair_device(
    passcode: int,
    discriminator: int,
    node_id: int,
    thread_dataset: str,
    use_cert: bool = True,
    logger=None
) -> bool:
    """
    Pair the device using BLE-Thread.
    use_cert: If True, includes --paa-trust-store-path parameter
    Returns: success (bool)
    """
    if logger:
        logger.info(f"[PAIR] Attempting to pair device...")
        logger.info(f"[PAIR] Passcode: {passcode}, Discriminator: {discriminator}")
        logger.info(f"[PAIR] Node ID: {node_id}")
        logger.info(f"[PAIR] Use certificate: {use_cert}")
    else:
        print(f"\n[PAIR] Attempting to pair device...")
        print(f"[PAIR] Passcode: {passcode}, Discriminator: {discriminator}")
        print(f"[PAIR] Node ID: {node_id}")
        print(f"[PAIR] Use certificate: {use_cert}")

    cmd = [
        "sudo", "./chip-tool", "pairing", "ble-thread", str(node_id),
        thread_dataset,
        str(passcode), str(discriminator)
    ]

    if use_cert:
        paa_path = PAA_TRUST_STORE_PATH
        import os
        if logger:
            logger.info(f"[PAIR] PAA trust store path: {paa_path}")
            if not os.path.isdir(paa_path):
                logger.warning(f"[PAIR] PAA trust store path does not exist: {paa_path}")
        else:
            print(f"[PAIR] PAA trust store path: {paa_path}")
            if not os.path.isdir(paa_path):
                print(f"[WARN] PAA trust store path does not exist: {paa_path}")
        cmd.extend(["--paa-trust-store-path", paa_path])
    else:
        # When not using certificate, bypass attestation verifier
        if logger:
            logger.info("[PAIR] Bypassing attestation verifier (--no-cert)")
        else:
            print("[PAIR] Bypassing attestation verifier (--no-cert)")
        cmd.extend(["--bypass-attestation-verifier", "1"])

    success = run_command_realtime(cmd, timeout=180, logger=logger, prefix="[PAIR]")

    if success:
        if logger:
            logger.info("[PAIR] Successfully paired device")
        else:
            print("[PAIR] Successfully paired device")
        return True
    else:
        if logger:
            logger.error("[PAIR] Failed to pair device")
        else:
            print("[ERROR] Failed to pair device")
        return False


def main():
    global NODE_ID, THREAD_DATASET

    parser = argparse.ArgumentParser(
        description='CHIP-Tool Pairing Script',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic usage with certificate (default)
    sudo python3 chip_tool_pairing.py MT:GYFB5KY61495TG11V10

    # Without certificate
    sudo python3 chip_tool_pairing.py MT:GYFB5KY61495TG11V10 --no-cert

    # Custom node ID
    sudo python3 chip_tool_pairing.py MT:GYFB5KY61495TG11V10 --node-id 1234
        """
    )
    parser.add_argument('qr_code', type=str, help='QR code setup payload (e.g., MT:GYFB5KY61495TG11V10)')
    parser.add_argument('--node-id', type=int, default=NODE_ID, help='Node ID (default: 2250)')
    parser.add_argument('--thread-dataset', type=str, default=THREAD_DATASET, help='Thread network dataset')
    parser.add_argument('--no-cert', action='store_true', help='Do not use PAA certificate (default: use certificate)')

    args = parser.parse_args()

    log_filename = setup_logging()
    logger = logging.getLogger()

    NODE_ID = args.node_id
    THREAD_DATASET = args.thread_dataset
    use_cert = not args.no_cert

    logger.info(f"QR Code: {args.qr_code}")
    logger.info(f"Node ID: {NODE_ID}")
    logger.info(f"Thread Dataset: {THREAD_DATASET[:50]}...")
    logger.info(f"Use Certificate: {use_cert}")
    if use_cert:
        logger.info(f"PAA Trust Store Path: {PAA_TRUST_STORE_PATH}")
    else:
        logger.info("PAA Trust Store Path: N/A (bypass attestation enabled)")

    print(f"\nLog file: {log_filename}")
    print("=" * 80)

    # Step 1: Clean temporary files
    logger.info("\n" + "=" * 80)
    logger.info("STEP 1: Clean Temporary Files")
    logger.info("=" * 80)
    clean_chip_temp_files(logger)
    time.sleep(0.5)

    # Step 2: Parse setup payload
    logger.info("\n" + "=" * 80)
    logger.info("STEP 2: Parse Setup Payload")
    logger.info("=" * 80)
    passcode, discriminator, error = parse_setup_payload(args.qr_code, logger)

    if passcode is None:
        logger.error("Could not extract passcode from QR code")
        logger.error(f"Error: {error}")
        sys.exit(1)

    if discriminator is None:
        logger.warning("Could not extract discriminator from QR code")
        logger.warning("Using default discriminator (might not work)")
        discriminator = 0

    logger.info(f"Passcode: {passcode}")
    logger.info(f"Discriminator: {discriminator}")
    print(f"\n[INFO] Passcode: {passcode}")
    print(f"[INFO] Discriminator: {discriminator}")

    # Step 3: Pair device
    logger.info("\n" + "=" * 80)
    logger.info("STEP 3: Pair Device")
    logger.info("=" * 80)
    pair_success = pair_device(
        passcode,
        discriminator,
        NODE_ID,
        THREAD_DATASET,
        use_cert,
        logger
    )

    if not pair_success:
        logger.error("Failed to pair device")
        sys.exit(1)

    logger.info("\n" + "=" * 80)
    logger.info("Pairing completed successfully!")
    logger.info("=" * 80)
    print("\n" + "=" * 80)
    print("Pairing completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()