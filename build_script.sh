#!/bin/bash
XSA_FILE=$1
OUTPUT_IMAGE=$2

echo "Building Linux image for $XSA_FILE..."
# Run Petalinux build (Modify as needed)
# Example:
# petalinux-create -t project -s $XSA_FILE -n my_project
# cd my_project
# petalinux-config --get-hw-description
# petalinux-build
# petalinux-package --boot --fsbl fsbl.elf --fpga system.bit --u-boot u-boot.elf
# tar -czvf $OUTPUT_IMAGE ./images/linux

echo "Build complete! Image saved as $OUTPUT_IMAGE"
