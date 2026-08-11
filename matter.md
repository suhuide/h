# [DAC](./files/matter/dac/dac.md)  
# [Commissioning](./files/matter/Commissioning/commissioning.md)  
# [OTA](./files/matter/ota/ota.md)  

# Chip-tool on Ubuntu
```c
https://snapcraft.io/install/chip-tool/ubuntu
https://snapcraft.io/install/openthread-border-router/ubuntu
https://canonical-matter.readthedocs-hosted.com/en/latest/how-to/otbr-on-ubuntu/
```
```c
sudo apt update
sudo apt install snapd
sudo snap install chip-tool
sudo snap install openthread-border-router --beta
```

## install the dependencies:
```c
sudo apt update
sudo apt install bluez avahi-daemon
```
## Connect the following interfaces:
```c
# Allow setting up the firewall
sudo snap connect openthread-border-router:firewall-control
# Allow access to USB Thread Radio Co-Processor (RCP)
sudo snap connect openthread-border-router:raw-usb
# Allow setting up the networking
sudo snap connect openthread-border-router:network-control
# Allow controlling the Bluetooth devices
sudo snap connect openthread-border-router:bluetooth-control

# Allow device discovery over Bluetooth Low Energy
sudo snap connect openthread-border-router:bluez
# Allow DNS-SD registration and discovery
# sudo snap connect openthread-border-router:avahi-control
```
## Configure the OTBR snap
The configurations are set via Snap Configuration Options and passed on the services.

First, check the default configurations:
```c
sudo snap get openthread-border-router
Key        Value
autostart  false
infra-if   enp0s3
radio-url  spinel+hdlc+uart:///dev/ttyUSB0?uart-flow-control=1"
thread-if  wpan0
```
## Then, override them based on the local setup.

For example, if the networking interface is eth0, change it as follows:
```
snap set openthread-border-router infra-if="enp0s3"
sudo snap set openthread-border-router radio-url="spinel+hdlc+uart:///dev/ttyUSB0?uart-flow-control=1"
```
## Start OTBR
By default the services are disabled and not started. After everything is configured, we can start and enable the services:
```c
sudo snap start --enable openthread-border-router
```
## Use the following command to query and follow the logs:
```c
snap logs -n 100 -f openthread-border-router
Note
```
To start and enable via a Gadget snap, set autostart snap configuration to true.

## Form a Thread network
Use the CTL tool to initialize the Thread network:
```c
sudo openthread-border-router.ot-ctl dataset init new
sudo openthread-border-router.ot-ctl dataset commit active
sudo openthread-border-router.ot-ctl ifconfig up
sudo openthread-border-router.ot-ctl thread start
sudo openthread-border-router.ot-ctl state
sudo openthread-border-router.ot-ctl dataset active -x
```