#!/usr/bin/env python3
import subprocess
import time
import sys
import threading
# Target switching interval (seconds), 0.2s = 200ms
INTERVAL_SEC = 0.2 
def output_reader(proc):
    """
    Background thread: Continuously reads and clears the subprocess output.
    This is mandatory; otherwise, once the chip-tool output buffer is full, 
    the process will hang/deadlock.
    """
    for line in iter(proc.stdout.readline, b''):
        decoded_line = line.decode('utf-8', errors='ignore').strip()
        if decoded_line:
            # If you don't want to see the verbose underlying logs, you can comment out the line below
            print(decoded_line)
def main():
    print("Starting chip-tool in interactive mode...")
    try:
        proc = subprocess.Popen(
            ["sudo", "./chip-tool", "interactive", "start"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            text=False
        )
    except FileNotFoundError:
        print("Error: './chip-tool' not found. Please ensure the path is correct.")
        sys.exit(1)
    # Start the background reading thread
    thread = threading.Thread(target=output_reader, args=(proc,), daemon=True)
    thread.start()
    # Wait for chip-tool to initialize
    print("Waiting for chip-tool to initialize (3 seconds)...")
    time.sleep(3.0)
    print(f"\nStarting alternating ON/OFF loop with {INTERVAL_SEC*1000:.0f}ms interval...")
    print("Press Ctrl+C to stop.")
    counter = 0
    is_on = True
    prev_start = None
    try:
        while True:
            counter += 1
            state = "on" if is_on else "off"
            start = time.time()
            # Build and send the command
            cmd_str = f"onoff {state} 2250 1\n"
            proc.stdin.write(cmd_str.encode('utf-8'))
            proc.stdin.flush()
            print(f"[{counter}] Sent {state.upper()} at {start:.3f}")
            if prev_start is not None:
                interval = start - prev_start
                print(f"[{counter}] Actual interval since last send: {interval*1000:.1f} ms")
            prev_start = start
            # Toggle state
            is_on = not is_on
            # Calculate exactly how long to sleep to maintain a stable frequency
            elapsed = time.time() - start
            sleep_time = INTERVAL_SEC - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting interactive mode...")
        try:
            proc.stdin.close()
        except:
            pass
        proc.terminate()
        proc.wait()
        sys.exit(1)
    except BrokenPipeError:
        print("\nchip-tool process closed unexpectedly.")
        sys.exit(1)
if __name__ == "__main__":
    main()
