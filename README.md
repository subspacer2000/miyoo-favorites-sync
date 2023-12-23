# miyoo-favorites-sync
Sync favorites from your Miyoo mini plus to batocera

This guide provides instructions on setting up your Batocera system to automatically sync and update favorites from a Miyoo handheld device using favourite.json, update_favorite.py, and watch_favourite.sh.

Prerequisites:
Ensure you have SSH access to your Batocera system and basic knowledge of navigating and executing commands in a Linux environment.

File Transfer:
Move the “miyoo-favorites” directory and its contents inside Batocera’s /userdata directory. This can be done over the network or using the command line:
/userdata/miyoo-favorites/

Set File Permissions:
Set executable permissions for each of the 3 files in the miyoo-favorites directory. In the SSH terminal, execute:
chmod +x /userdata/miyoo-favorites/*.sh
chmod +x /userdata/miyoo-favorites/*.py
This command makes the scripts executable, which is necessary for them to run.

Syncthing Setup:
Set up Syncthing to share the favourite.json file between your Miyoo and Batocera devices. Place it in the /userdata/miyoo-favorites/ directory. If needed, replace the existing favourite.json file with your own. For detailed Syncthing setup instructions, refer to Syncthing documentation for batocera (https://wiki.batocera.org/syncthing) and miyoo (https://github.com/XK9274/syncthing-app-miyoo).

Automate Script Execution:
To ensure the watch_favourite.sh script runs automatically after each boot:

Enable Writing to Boot Partition:
mount -o remount,rw /boot

Edit the postshare.sh File:
nano /boot/postshare.sh

Add the following lines to postshare.sh:
#!/bin/bash
/userdata/miyoo-favorites/watch_favourite.sh &

Make the Script Executable:
chmod +x /boot/postshare.sh

Secure the Boot Partition:
mount -o remount,ro /boot

Reboot the System:
reboot

SSH Commands for Monitoring and Manual Execution:

To check the status of watch_favourite.sh instances: ps aux | grep watch_favourite.sh
To run the script that watches for changes/auto-detect: ./watch_favourite.sh
To manually run the script that updates/not auto-detect: /usr/bin/python3 /userdata/miyoo-favorites/update_favorite.py
To add a “test modification” line to favourite.json: echo "test modification" >> /userdata/miyoo-favorites/favourite.json
Important Notes:

Safety First: Be cautious when using nano or other editors to modify system files. A small mistake can lead to system issues. Always back up your configuration and important files before making significant changes.

Translation Table: Update the translation table in update_favorite.py for more systems based on your needs. This table maps directory names from the Miyoo handheld to corresponding system names in Batocera. 

Here's a snippet for reference:
makefile
Copy code
# Translation table from Miyoo handheld to Batocera
directory_map = {
"INTELLIVISION": "intellivision",

    "ARCADE": "fbneo",
    
    "ATARI": "atari2600",
    
    "COLECO": "colecovision",
    
    "FAIRCHILD": "fairchild",  # Update if there's a specific name in Batocera
    
    "FC": "nes",
    
    "GB": "gb",
    
    "GBA": "gba",
    
    "GBC": "gbc",
    
    "GG": "gamegear",
    
    "JAGUAR": "jaguar",
    
    "LYNX": "lynx",
    
    "MD": "megadrive",
    
    "MEGADUCK": "megaduck",  # Update if there's a specific name in Batocera
    
    "MS": "mastersystem",
    
    "MSX": "msx",
    
    "NEOGEO": "neogeo",
    
    "NGP": "ngp",
    
    "ODYSSEY": "o2em",
    
    "PANASONIC": "3do",
    
    "PCE": "pcengine",
    
    "PCECD": "pcenginecd",
    
    "POKE": "pokemini",
    
    "PS": "psx",
    
    "SEGACD": "segacd",
    
    "SEGASGONE": "segasgone",  # Update if there's a specific name in Batocera
    
    "SEVENTYEIGHTHUNDRED": "atari7800",
    
    "SFC": "snes",
    
    "SUFAMI": "sufami",
    
    "SUPERVISION": "supervision",
    
    "THIRTYTWOX": "sega32x",
    
    "VB": "virtualboy",
    
    "WS": "wswan",
    
    # Add other mappings as needed
}

Post-Execution Check: After rebooting, check the status of watch_favourite.sh to ensure it's running as expected. If it's not, review the steps and check Batocera logs for potential issues.
By following these instructions, you should be able to set up your Batocera system to automatically sync and update favorites from your Miyoo handheld to Batocera. 

