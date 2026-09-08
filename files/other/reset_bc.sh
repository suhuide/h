#!/bin/bash
# kill bcompare
pkill bcompare
# remove config file
rm -rf ~/.config/bcompare/registry.dat
echo "Beyond Compare trial period reset."
