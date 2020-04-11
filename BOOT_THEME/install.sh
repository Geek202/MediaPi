#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run this script as root!"
  exit
fi

echo This script will install the mediapi BOOT SPLASH THEME to
echo 		/usr/share/plymouth/themes
echo and will also set this theme as the default
echo

echo Copying files
cp -r mediapi/ /usr/share/plymouth/themes/
echo Done! Setting theme as default...
plymouth-set-default-theme -R mediapi
echo Installation complete!
