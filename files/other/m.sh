#!/bin/bash

# matter.sh - Matter/Thread Border Router setup script
# Usage: ./matter.sh

set -e  # Exit on error, but we'll handle specific errors gracefully

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

print_step() {
    echo -e "\n${BLUE}>>>${NC} $1"
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check device exists
check_device() {
    local device="$1"
    local device_name="$2"
    
    if [ -e "$device" ]; then
        print_success "$device_name found: $device"
        return 0
    else
        print_error "$device_name not found: $device"
        return 1
    fi
}

# Function to check OTBR state with timeout
check_otbr_state() {
    local timeout=30
    local interval=2
    local elapsed=0
    local state=""
    local state_line=""
    
    print_info "Waiting for OTBR to become leader (timeout: ${timeout}s)..."
    
    while [ $elapsed -lt $timeout ]; do
        # Capture output and extract the first line (state)
        if state_output=$(sudo openthread-border-router.ot-ctl state 2>/dev/null); then
            # Extract first line only (the state), ignoring "Done"
            state_line=$(echo "$state_output" | head -n 1 | tr -d '\r\n' | xargs)
            print_info "Current OTBR state: $state_line (${elapsed}s elapsed)"
            
            if [ "$state_line" = "leader" ] || [ "$state_line" = "Leader" ] || [ "$state_line" = "router" ] || [ "$state_line" = "child" ]; then
                # Any valid state means OTBR is running
                if [ "$state_line" = "leader" ] || [ "$state_line" = "Leader" ]; then
                    return 0
                else
                    print_info "OTBR is $state_line, waiting to become leader..."
                fi
            fi
        else
            print_info "OTBR not ready yet (${elapsed}s elapsed)"
        fi
        
        sleep $interval
        elapsed=$((elapsed + interval))
    done
    
    return 1
}

# Main script starts here
print_step "Starting Matter/Thread Border Router Setup Script"
echo "=========================================================="

# Step 1: Detect both serial devices
print_step "Step 1: Detecting serial devices..."

# Check /dev/ttyACM0 for Bluetooth
BT_DEV="/dev/ttyACM0"
OTBR_DEV="/dev/ttyUSB0"
DEVICE_OK=0

if check_device "$BT_DEV" "Bluetooth device (ttyACM0)"; then
    DEVICE_OK=$((DEVICE_OK + 1))
else
    print_error "Bluetooth device not found! Please check:"
    echo "  - Is the Bluetooth module plugged in?"
    echo "  - Check: ls -la /dev/ttyACM*"
    echo "  - You may need: sudo chmod 666 /dev/ttyACM0"
fi

if check_device "$OTBR_DEV" "OTBR device (ttyUSB0)"; then
    DEVICE_OK=$((DEVICE_OK + 1))
else
    print_error "OTBR device not found! Please check:"
    echo "  - Is the Thread RCP (USB dongle) plugged in?"
    echo "  - Check: ls -la /dev/ttyUSB*"
    echo "  - You may need: sudo chmod 666 /dev/ttyUSB0"
fi

# Exit if any device is missing
if [ $DEVICE_OK -lt 2 ]; then
    echo ""
    print_error "Missing required devices! Exiting..."
    exit 1
fi

print_success "Both devices detected successfully"

# Step 2: Mount Bluetooth HCI on /dev/ttyACM0
print_step "Step 2: Setting up Bluetooth HCI on $BT_DEV..."

# Check if hciattach exists
if ! command_exists hciattach; then
    print_error "hciattach command not found. Please install bluez-utils."
    echo "  Try: sudo apt-get install bluez-utils"
    exit 1
fi

# Check if hci0 already exists and remove it
if hciconfig hci0 2>/dev/null | grep -q "hci0"; then
    print_info "hci0 already exists, removing it..."
    sudo hciconfig hci0 down 2>/dev/null || true
    sudo hciconfig hci0 del 2>/dev/null || true
    sleep 1
fi

# Attach Bluetooth device on ttyACM0
print_info "Attaching Bluetooth device on $BT_DEV..."
if sudo hciattach "$BT_DEV" any 2>&1 | tee /tmp/hciattach.log; then
    print_success "Bluetooth HCI attached successfully on $BT_DEV"
else
    print_error "Failed to attach Bluetooth HCI on $BT_DEV"
    print_error "Check /tmp/hciattach.log for details"
    exit 1
fi

# Wait for hci0 to be ready
sleep 2
if hciconfig hci0 2>/dev/null | grep -q "hci0"; then
    print_success "hci0 is ready"
    echo ""
    hciconfig hci0
    echo ""
else
    print_error "hci0 not found after attachment"
    exit 1
fi

# Step 3: Enable OTBR (OpenThread Border Router)
print_step "Step 3: Setting up OpenThread Border Router..."

# Verify OTBR RCP device is present
if [ ! -e "$OTBR_DEV" ]; then
    print_error "OTBR device $OTBR_DEV disappeared!"
    exit 1
fi
print_info "OTBR RCP device: $OTBR_DEV"

# Setup snap connections
print_info "Configuring OTBR snap connections..."

print_info "Enabling firewall control..."
sudo snap connect openthread-border-router:firewall-control

print_info "Enabling raw USB access..."
sudo snap connect openthread-border-router:raw-usb

print_info "Enabling network control..."
sudo snap connect openthread-border-router:network-control

print_info "Enabling Bluetooth control..."
sudo snap connect openthread-border-router:bluetooth-control

print_info "Enabling BlueZ for BLE discovery..."
sudo snap connect openthread-border-router:bluez

print_info "Starting and enabling OTBR service..."
if sudo snap start --enable openthread-border-router; then
    print_success "OTBR service started and enabled"
else
    print_error "Failed to start OTBR service"
    exit 1
fi

# Step 4: Monitor OTBR state
print_step "Step 4: Monitoring OTBR state (30 second timeout)..."

# Wait a bit for OTBR to initialize
print_info "Waiting for OTBR to initialize..."
sleep 5

# Check OTBR state with timeout
if check_otbr_state; then
    print_success "OTBR is running as LEADER!"
    echo "=========================================================="
    print_success "All setup completed successfully!"
    echo ""
    echo "Device summary:"
    echo "  - Bluetooth: $BT_DEV → hci0"
    echo "  - OTBR RCP:   $OTBR_DEV"
    echo ""
    echo "OTBR is ready to use."
    echo ""
    echo "Useful commands:"
    echo "  - Check OTBR state:     sudo openthread-border-router.ot-ctl state"
    echo "  - Get IPv6 address:     sudo openthread-border-router.ot-ctl ipaddr"
    echo "  - Scan Thread network:  sudo openthread-border-router.ot-ctl scan"
    echo "  - Check Bluetooth:      hciconfig hci0"
    echo "  - View OTBR logs:       sudo snap logs openthread-border-router"
    echo "=========================================================="
    exit 0
else
    print_error "OTBR failed to become leader within 30 seconds!"
    echo "=========================================================="
    echo "Troubleshooting:"
    echo "  - Check OTBR status:    sudo snap services openthread-border-router"
    echo "  - View OTBR logs:       sudo snap logs openthread-border-router"
    echo "  - Manual state check:   sudo openthread-border-router.ot-ctl state"
    echo "  - Restart OTBR:         sudo snap restart openthread-border-router"
    echo "  - Check RCP device:     ls -la $OTBR_DEV"
    echo "  - Check Bluetooth:      hciconfig hci0"
    echo "=========================================================="
    exit 1
fi