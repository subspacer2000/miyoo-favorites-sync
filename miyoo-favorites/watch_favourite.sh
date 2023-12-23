#!/bin/bash
echo "Script started."

# Path to the favourite.json file
FAVOURITE_JSON="/userdata/miyoo-favorites/favourite.json"

# Path to your Python update script
UPDATE_SCRIPT="/userdata/miyoo-favorites/update_favorite.py"

# Using inotifywait to monitor favourite.json for modifications
while inotifywait -e modify,move,create,delete,close_write "/userdata/miyoo-favorites/"; do
    echo "Change detected in favourite.json."
    /usr/bin/python3 "$UPDATE_SCRIPT"
    echo "Python script run command issued."
done

echo "Script ended or exited unexpectedly."
