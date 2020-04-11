#!/bin/bash

echo This script will install the mediapi BOOT SPLASH THEME to
echo 		/usr/share/plymouth/themes
echo and will also set this theme as the default
echo

echo Copying files
sudo cp -r mediapi/ /usr/share/plymouth/themes/
echo Done! Setting theme as default...
sudo plymouth-set-default-theme -R mediapi
echo Installation complete!
