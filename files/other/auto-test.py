#!/usr/bin/env python3
"""
Extended chip-tool automation script with QR code parsing and device type-specific actions
(Improved version with single-threaded sequential endpoint testing)
"""
import subprocess
import time
import sys
import threading
import argparse
import re
import json
import logging
import os
import signal
import glob
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# Node ID for the device
NODE_ID = 2250

# Device type mappings
DEVICE_TYPES = {
    514: {"name": "Window Covering", "interval": 30.0},   # Changed to 30 seconds
    269: {"name": "Extended Color Light", "interval": 2.0},
    257: {"name": "Dimmable Light", "interval": 2.0},
    266: {"name": "On/Off Plug-in Unit", "interval": 2.0},
    256: {"name": "On/Off Light", "interval": 2.0},
}

# Thread network dataset (example - should be adjusted for your network)
THREAD_DATASET = "hex:0e0800000000000100004a0300000b35060004001fffe00208d66aa42e602782d70708fd119c64dd37b8c40510af58620082e94dcc8b2e7e4a5735245b030f4f70656e5468726561642d323235660102225f04101ab41530faf60b359a71bbd4d65101e50c0402a0f7f8000300000f"

# PAA certificate path - hardcoded as requested
PAA_TRUST_STORE_PATH = "/home/ubuntu/paa-root-certs"

# Lock for writing to interactive chip-tool stdin (now only one thread, but keep for safety)
stdin_lock = threading.Lock()


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
    logging.info("Extended chip-tool Automation Script (Sequential)")
    logging.info("=" * 80)
    logging.info(f"Log file: {log_filename}")
    logging.info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    return log_filename


def output_reader(proc, logger, prefix="[CHIP-TOOL]"):
    """
    Background thread: Continuously reads and clears the subprocess output.
    This is mandatory; otherwise, once the chip-tool output buffer is full,
    the process will hang/deadlock.
    """
    try:
        for line in iter(proc.stdout.readline, b''):
            decoded_line = line.decode('utf-8', errors='ignore').strip()
            if decoded_line:
                logger.debug(f"{prefix} {decoded_line}")
    except Exception as e:
        if logger:
            logger.debug(f"{prefix} Reader error: {e}")


def run_command_realtime(cmd: List[str], timeout: int = 120, logger=None, prefix="[CMD]") -> bool:
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


def run_command_and_capture(cmd: List[str], timeout: int = 30, logger=None) -> Tuple[int, str, str]:
    """
    Run a command and capture its output (for simple commands).
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
        if logger:
            logger.info(f"[PAIR] PAA trust store path: {paa_path}")
            if not os.path.isdir(paa_path):
                logger.warning(f"[PAIR] PAA trust store path does not exist: {paa_path}")
        else:
            print(f"[PAIR] PAA trust store path: {paa_path}")
            if not os.path.isdir(paa_path):
                print(f"[WARN] PAA trust store path does not exist: {paa_path}")
        cmd.extend(["--paa-trust-store-path", paa_path])

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


def discover_endpoints(node_id: int, logger=None) -> Dict[int, Dict]:
    """
    Discover endpoints and their device types.
    Returns: Dict mapping endpoint_id -> {device_type, device_name}
    """
    if logger:
        logger.info("[DISCOVER] Discovering endpoints...")
    else:
        print(f"\n[DISCOVER] Discovering endpoints...")

    endpoints = {}

    # Method 1: Read parts-list from endpoint 0 (root) to get all endpoints
    if logger:
        logger.debug("[DISCOVER] Reading parts-list from endpoint 0...")
    else:
        print("[DISCOVER] Reading parts-list from endpoint 0...")
    cmd = ["sudo", "./chip-tool", "descriptor", "read", "parts-list", str(node_id), "0"]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)

    if returncode == 0:
        # Parse output like:
        #   PartsList: 6 entries
        #     [1]: 1
        #     [2]: 2
        #     ...
        # We match lines like "[1]: 1" and extract the number after the colon.
        # Also handle possible "Endpoint: 1" format just in case.
        for line in stdout.splitlines():
            # Try pattern [number]: number
            match = re.search(r'\[(\d+)\]\s*:\s*(\d+)', line)
            if match:
                ep_num = int(match.group(2))
                endpoints[ep_num] = {"device_type": None, "device_name": "Unknown"}
                continue
            # Fallback: match "Endpoint: 1"
            match = re.search(r'[Ee]ndpoint[:\s]+(\d+)', line)
            if match:
                ep_num = int(match.group(1))
                endpoints[ep_num] = {"device_type": None, "device_name": "Unknown"}

    # If no endpoints found, try device-type-list on endpoint 0 (might not give all endpoints)
    if not endpoints:
        if logger:
            logger.debug("[DISCOVER] No endpoints found from parts-list, trying device-type-list on endpoint 0...")
        else:
            print("[DISCOVER] No endpoints found from parts-list, trying device-type-list on endpoint 0...")
        cmd = ["sudo", "./chip-tool", "descriptor", "read", "device-type-list", str(node_id), "0"]
        returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)
        if returncode == 0:
            # This command returns device types for endpoint 0, not a list of endpoints.
            # But we can't infer other endpoints from this, so just treat endpoint 0 if not already.
            if 0 not in endpoints:
                endpoints[0] = {"device_type": None, "device_name": "Unknown"}

    # If still empty, fallback to common endpoints (1-6, etc.)
    if not endpoints:
        if logger:
            logger.warning("[DISCOVER] No endpoints found, falling back to common endpoints 1-6...")
        else:
            print("[DISCOVER] No endpoints found, falling back to common endpoints 1-6...")
        for ep_id in range(1, 7):
            endpoints[ep_id] = {"device_type": None, "device_name": "Unknown"}

    if logger:
        logger.info(f"[DISCOVER] Found endpoints: {list(endpoints.keys())}")
    else:
        print(f"[DISCOVER] Found endpoints: {list(endpoints.keys())}")

    # Determine device type for each endpoint
    for ep_id in endpoints.keys():
        device_type = discover_device_type(ep_id, node_id, logger)
        if device_type:
            endpoints[ep_id]["device_type"] = device_type
            endpoints[ep_id]["device_name"] = DEVICE_TYPES.get(device_type, {}).get("name", f"Unknown ({device_type})")
        else:
            endpoints[ep_id]["device_type"] = None
            endpoints[ep_id]["device_name"] = "Unknown Device"

    return endpoints


def discover_device_type(endpoint_id: int, node_id: int, logger=None) -> Optional[int]:
    """
    Discover the device type for a specific endpoint using device-type-list.
    Returns: device_type code or None
    """
    if logger:
        logger.info(f"[DISCOVER] Discovering device type for endpoint {endpoint_id}...")
    else:
        print(f"[DISCOVER] Discovering device type for endpoint {endpoint_id}...")

    # Primary method: read device-type-list
    cmd = ["sudo", "./chip-tool", "descriptor", "read", "device-type-list", str(node_id), str(endpoint_id)]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)

    if returncode == 0:
        # Look for "DeviceType: 266" or "DeviceType: 0x10A" etc.
        dt_match = re.search(r'[Dd]evice[Tt]ype[:\s]+(?:0x)?(\d+)', stdout)
        if dt_match:
            device_type = int(dt_match.group(1))
            device_name = DEVICE_TYPES.get(device_type, {}).get("name", "Unknown")
            if logger:
                logger.info(f"[DISCOVER] Endpoint {endpoint_id} - Device Type: {device_type} ({device_name})")
            else:
                print(f"[DISCOVER] Endpoint {endpoint_id} - Device Type: {device_type} ({device_name})")
            return device_type

    # Fallback: try reading device-type (older format)
    cmd = ["sudo", "./chip-tool", "descriptor", "read", "device-type", str(node_id), str(endpoint_id)]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)
    if returncode == 0:
        dt_match = re.search(r'[Dd]evice\s+[Tt]ype[:\s]+(?:0x)?(\d+)', stdout)
        if dt_match:
            device_type = int(dt_match.group(1))
            device_name = DEVICE_TYPES.get(device_type, {}).get("name", "Unknown")
            if logger:
                logger.info(f"[DISCOVER] Endpoint {endpoint_id} - Device Type: {device_type} ({device_name})")
            else:
                print(f"[DISCOVER] Endpoint {endpoint_id} - Device Type: {device_type} ({device_name})")
            return device_type

    # Last resort: infer from clusters
    device_type = infer_device_type_from_clusters(endpoint_id, node_id, logger)
    if device_type:
        return device_type

    if logger:
        logger.warning(f"[DISCOVER] Could not determine device type for endpoint {endpoint_id}")
    else:
        print(f"[DISCOVER] Could not determine device type for endpoint {endpoint_id}")
    return None


def infer_device_type_from_clusters(endpoint_id: int, node_id: int, logger=None) -> Optional[int]:
    """
    Infer device type by checking which clusters are supported.
    Returns: device_type code or None
    """
    if logger:
        logger.info(f"[DISCOVER] Inferring device type for endpoint {endpoint_id} from clusters...")
    else:
        print(f"[DISCOVER] Inferring device type for endpoint {endpoint_id} from clusters...")

    cmd = ["sudo", "./chip-tool", "colorcontrol", "read", "color-mode", str(node_id), str(endpoint_id)]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)
    if returncode == 0:
        if logger:
            logger.info(f"[DISCOVER] Endpoint {endpoint_id} supports ColorControl -> Extended Color Light")
        else:
            print(f"[DISCOVER] Endpoint {endpoint_id} supports ColorControl -> Extended Color Light")
        return 269

    cmd = ["sudo", "./chip-tool", "levelcontrol", "read", "current-level", str(node_id), str(endpoint_id)]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)
    if returncode == 0:
        if logger:
            logger.info(f"[DISCOVER] Endpoint {endpoint_id} supports LevelControl -> Dimmable Light")
        else:
            print(f"[DISCOVER] Endpoint {endpoint_id} supports LevelControl -> Dimmable Light")
        return 257

    cmd = ["sudo", "./chip-tool", "windowcovering", "read", "type", str(node_id), str(endpoint_id)]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)
    if returncode == 0:
        if logger:
            logger.info(f"[DISCOVER] Endpoint {endpoint_id} supports WindowCovering -> Window Covering")
        else:
            print(f"[DISCOVER] Endpoint {endpoint_id} supports WindowCovering -> Window Covering")
        return 514

    cmd = ["sudo", "./chip-tool", "onoff", "read", "on-off", str(node_id), str(endpoint_id)]
    returncode, stdout, stderr = run_command_and_capture(cmd, timeout=30, logger=logger)
    if returncode == 0:
        if logger:
            logger.info(f"[DISCOVER] Endpoint {endpoint_id} supports OnOff -> On/Off Light")
        else:
            print(f"[DISCOVER] Endpoint {endpoint_id} supports OnOff -> On/Off Light")
        return 256

    return None


def get_actions_for_device_type(device_type: Optional[int], node_id: int) -> List[List[str]]:
    """
    Get the list of actions for a given device type.
    Each action is a list of command parts.
    """
    if device_type == 514:  # Window Covering - 30s interval (changed)
        return [
            ["windowcovering", "up-or-open", str(node_id)],
            ["windowcovering", "go-to-lift-percentage", "6000", str(node_id)],  # 60%
            ["windowcovering", "go-to-lift-percentage", "3000", str(node_id)],  # 30%
            ["windowcovering", "down-or-close", str(node_id)],
        ]
    elif device_type == 269:  # Extended Color Light - 2s interval
        return [
            ["onoff", "on", str(node_id)],
            ["colorcontrol", "move-to-color", "9831", "3932", "0", "0", "0", str(node_id)],  # Blue
            ["colorcontrol", "move-to-color", "41947", "21624", "0", "0", "0", str(node_id)],  # Red
            ["colorcontrol", "move-to-color", "19660", "39320", "0", "0", "0", str(node_id)],  # Green
            ["colorcontrol", "move-to-color", "20971", "9830", "0", "0", "0", str(node_id)],  # Purple
            ["onoff", "off", str(node_id)],
        ]
    elif device_type == 257:  # Dimmable Light - 2s interval
        return [
            ["onoff", "on", str(node_id)],
            ["levelcontrol", "move-to-level", "32", "0", "0", "0", str(node_id)],  # 50% (128/255)
            ["levelcontrol", "move-to-level", "128", "0", "0", "0", str(node_id)],  # 50% (128/255)
            ["levelcontrol", "move-to-level", "254", "0", "0", "0", str(node_id)],  # 50% (128/255)
            ["onoff", "off", str(node_id)],
        ]
    elif device_type == 266:  # On/Off Plug-in Unit - 2s interval
        return [
            ["onoff", "on", str(node_id)],
            ["onoff", "off", str(node_id)],
        ]
    elif device_type == 256:  # On/Off Light - 2s interval
        return [
            ["onoff", "on", str(node_id)],
            ["onoff", "off", str(node_id)],
        ]
    else:  # Other - 2s interval
        return [
            ["onoff", "on", str(node_id)],
            ["onoff", "off", str(node_id)],
        ]


def send_command_to_chip_tool(proc: subprocess.Popen, cmd_parts: List[str], logger=None) -> bool:
    """
    Send a single command to the interactive chip-tool process.
    Returns True if successful (no immediate error).
    """
    cmd_str = " ".join(cmd_parts) + "\n"
    try:
        with stdin_lock:
            proc.stdin.write(cmd_str.encode('utf-8'))
            proc.stdin.flush()
        if logger:
            logger.debug(f"[SEND] Sent: {cmd_str.strip()}")
        return True
    except Exception as e:
        if logger:
            logger.error(f"[SEND] Failed to send command: {e}")
        return False


def execute_one_round(proc: subprocess.Popen, endpoints: Dict[int, Dict], node_id: int, logger):
    """
    Execute one full round of actions for all endpoints in order.
    """
    # Sort endpoints by ID, skip endpoint 0
    sorted_eps = sorted([ep for ep in endpoints.keys() if ep != 0])
    if not sorted_eps:
        logger.warning("No valid endpoints (excluding 0) to test.")
        return

    for ep_id in sorted_eps:
        ep_info = endpoints[ep_id]
        device_type = ep_info.get("device_type")
        device_name = ep_info.get("device_name")

        # Get interval for this device type
        interval = DEVICE_TYPES.get(device_type, {}).get("interval", 2.0)

        logger.info(f"[ROUND] Testing endpoint {ep_id} ({device_name}, type={device_type})")
        print(f"\n[ROUND] Testing endpoint {ep_id} ({device_name}, type={device_type})")

        # Get action list for this device type
        actions = get_actions_for_device_type(device_type, node_id)
        if not actions:
            logger.warning(f"[ROUND] No actions defined for endpoint {ep_id}")
            continue

        # Execute each action command with the endpoint ID appended
        for action in actions:
            action_with_ep = action.copy()
            action_with_ep.append(str(ep_id))
            cmd_str = " ".join(action_with_ep)
            logger.info(f"[ACTION][{ep_id}] Sending: {cmd_str}")
            print(f"[ACTION][{ep_id}] Sending: {cmd_str}")

            success = send_command_to_chip_tool(proc, action_with_ep, logger)
            if not success:
                logger.error(f"[ACTION][{ep_id}] Failed to send command, skipping rest of actions for this endpoint")
                break

            # Wait for the interval after each command (except maybe last? keep as original)
            logger.debug(f"[ACTION][{ep_id}] Waiting {interval}s before next command...")
            time.sleep(interval)

        logger.info(f"[ROUND] Finished endpoint {ep_id}")
        print(f"[ROUND] Finished endpoint {ep_id}")


proc_global = None
logger_global = None


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    global proc_global, logger_global
    if logger_global:
        logger_global.info("Received SIGINT, cleaning up...")
    print("\nReceived SIGINT, cleaning up...")
    if proc_global:
        try:
            proc_global.stdin.close()
        except:
            pass
        proc_global.terminate()
        try:
            proc_global.wait(timeout=5)
        except:
            proc_global.kill()
            proc_global.wait()
    sys.exit(0)


def main():
    global NODE_ID, THREAD_DATASET, proc_global, logger_global

    parser = argparse.ArgumentParser(
        description='Extended chip-tool automation script (sequential testing)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Basic usage with certificate (default)
    sudo python3 chip_tool_extended.py MT:GYFB5KY61495TG11V10

    # Without certificate
    sudo python3 chip_tool_extended.py MT:GYFB5KY61495TG11V10 --no-cert

    # Discover only
    sudo python3 chip_tool_extended.py MT:GYFB5KY61495TG11V10 --discover-only

    # Skip pairing (already paired)
    sudo python3 chip_tool_extended.py MT:GYFB5KY61495TG11V10 --skip-pairing
        """
    )
    parser.add_argument('qr_code', type=str, help='QR code setup payload (e.g., MT:GYFB5KY61495TG11V10)')
    parser.add_argument('--node-id', type=int, default=NODE_ID, help='Node ID (default: 2250)')
    parser.add_argument('--thread-dataset', type=str, default=THREAD_DATASET, help='Thread network dataset')
    parser.add_argument('--skip-pairing', action='store_true', help='Skip pairing (use existing pairing)')
    parser.add_argument('--discover-only', action='store_true', help='Only discover endpoints and exit')
    parser.add_argument('--no-cert', action='store_true', help='Do not use PAA certificate (default: use certificate)')

    args = parser.parse_args()

    log_filename = setup_logging()
    logger = logging.getLogger()
    logger_global = logger

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
        logger.info("PAA Trust Store Path: N/A")

    print(f"\nLog file: {log_filename}")
    print("=" * 80)

    signal.signal(signal.SIGINT, signal_handler)

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

    if args.discover_only:
        logger.info("Discover-only mode, skipping pairing...")
    elif not args.skip_pairing:
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

        logger.info("Waiting for device to be ready (5 seconds)...")
        time.sleep(5)

    # Step 4: Discover endpoints
    logger.info("\n" + "=" * 80)
    logger.info("STEP 4: Discover Endpoints")
    logger.info("=" * 80)
    endpoints = discover_endpoints(NODE_ID, logger)

    if not endpoints:
        logger.error("No endpoints discovered")
        sys.exit(1)

    logger.info("\n" + "-" * 80)
    logger.info("Discovered Endpoints:")
    logger.info("-" * 80)
    print("\n" + "-" * 80)
    print("Discovered Endpoints:")
    print("-" * 80)
    for ep_id, ep_info in endpoints.items():
        device_type = ep_info.get("device_type")
        device_name = ep_info.get("device_name")
        log_line = f"  Endpoint {ep_id}: {device_name} (Type: {device_type})"
        logger.info(log_line)
        print(log_line)
    logger.info("-" * 80)
    print("-" * 80)

    if args.discover_only:
        logger.info("Discover-only mode, exiting...")
        sys.exit(0)

    # Step 5: Start interactive mode and execute actions sequentially in a loop
    logger.info("\n" + "=" * 80)
    logger.info("STEP 5: Execute Device-Specific Actions (Sequential, Round-Robin)")
    logger.info("=" * 80)

    logger.info("Starting chip-tool in interactive mode...")
    print("\n[INFO] Starting chip-tool in interactive mode...")
    try:
        proc = subprocess.Popen(
            ["sudo", "./chip-tool", "interactive", "start"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        proc_global = proc
    except FileNotFoundError:
        logger.error("'./chip-tool' not found. Please ensure the path is correct.")
        print("[ERROR] './chip-tool' not found. Please ensure the path is correct.")
        sys.exit(1)

    # Start the background output reader
    thread = threading.Thread(target=output_reader, args=(proc, logger, "[INTERACTIVE]"), daemon=True)
    thread.start()

    logger.info("Waiting for chip-tool to initialize (3 seconds)...")
    time.sleep(3.0)

    logger.info("Starting sequential test rounds (endpoints 1..N, then repeat).")
    logger.info("Press Ctrl+C to stop.")
    print("\n[INFO] Starting sequential test rounds (endpoints 1..N, then repeat).")
    print("[INFO] Press Ctrl+C to stop.\n")

    round_counter = 0
    try:
        while True:
            round_counter += 1
            logger.info(f"\n===== ROUND {round_counter} =====")
            print(f"\n===== ROUND {round_counter} =====")
            execute_one_round(proc, endpoints, NODE_ID, logger)
            # Small delay between rounds to avoid tight loop
            time.sleep(1.0)
    except KeyboardInterrupt:
        logger.info("\nInterrupted by user. Stopping...")
        print("\n\n[INFO] Interrupted by user. Stopping...")
    finally:
        logger.info("Cleaning up...")
        print("\n[INFO] Cleaning up...")
        try:
            proc.stdin.close()
        except:
            pass
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except:
            proc.kill()
            proc.wait()

        logger.info("All actions stopped. Exiting...")
        print("[INFO] All actions stopped. Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()