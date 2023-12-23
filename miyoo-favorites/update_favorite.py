import json
import xml.etree.ElementTree as ET
import os

# Path to the favourite.json file
favourite_json_path = "/userdata/miyoo-favorites/favourite.json"

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

def update_gamelist(rompath):
    # Extract the filename from the rompath
    filename = os.path.basename(rompath)
    
    # Extract the system name from the rompath and translate it
    system_name = rompath.split('/')[4]  # Adjust based on the structure of the path
    batocera_system_name = directory_map.get(system_name.upper(), None)

    if batocera_system_name:
        gamelist_xml_path = f"/userdata/roms/{batocera_system_name}/gamelist.xml"
        print(f"Attempting to update {gamelist_xml_path}")

        # Load the XML file
        tree = ET.parse(gamelist_xml_path)
        root = tree.getroot()
        game_found = False

        # Find the game based on the path and update the favorite tag
        for game in root.findall('game'):
            game_path = game.find('path').text if game.find('path') is not None else ''
            if filename in game_path:
                game_found = True
                if game.find('favorite') is None:
                    ET.SubElement(game, 'favorite').text = 'true'
                else:
                    game.find('favorite').text = 'true'
                break

        if game_found:
            # Save the changes back to the file
            tree.write(gamelist_xml_path)
            print(f"Updated the favorite status for {filename} in {gamelist_xml_path}")
        else:
            print(f"Game with filename {filename} not found in {gamelist_xml_path}")

    else:
        print(f"No Batocera directory mapping found for {system_name}")

try:
    with open(favourite_json_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            try:
                favorite_game = json.loads(line)
                print(f"Processing game with path: {favorite_game['rompath']}")
                update_gamelist(favorite_game['rompath'])
            except json.JSONDecodeError as e:
                print(f"An error occurred while parsing a line in {favourite_json_path}: {e}")
except Exception as e:
    print(f"An error occurred while reading {favourite_json_path}: {e}")
