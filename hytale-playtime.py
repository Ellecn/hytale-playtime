##################################################################
### This script shows the play time of your Hytale worlds.     ###
### It works with the Flatpak Linux version.                   ###
##################################################################
import json
from pathlib import Path
from datetime import datetime

def get_world_folders():
    worlds_dir = f"{Path.home()}/.var/app/com.hypixel.HytaleLauncher/data/Hytale/UserData/Saves/"
    return [p for p in Path(worlds_dir).iterdir() if p.is_dir()]

def get_world_display_name(world_folder):
    with open(f"{world_folder}/universe/worlds/default/config.json", 'r') as file:
        json_data = json.load(file)
        return json_data['DisplayName']

def get_playtime_in_seconds(world_folder):
    with open(f"{world_folder}/universe/worlds/default/resources/Time.json", 'r') as file:
        json_data = json.load(file)
        delta = datetime.strptime(json_data['Now'].rstrip('Z')[:-3], '%Y-%m-%dT%H:%M:%S.%f') - datetime(1970, 1, 1)
        return delta.seconds

def format(seconds):
    return f"{seconds//3600}h:{(seconds%3600)//60}m"

if __name__ == "__main__":
    total_play_time_seconds = 0
    world_folders = get_world_folders()
    for world_folder in world_folders:
        world_name = get_world_display_name(world_folder)
        playtime_in_seconds = get_playtime_in_seconds(world_folder)
        print(f"{world_name}: {format(playtime_in_seconds)}")
        total_play_time_seconds += playtime_in_seconds
    print(f"--> Total: {format(total_play_time_seconds)}")
