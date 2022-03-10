import os

from jproperties import Properties

from twitbot.common.filemanagement.file_manager import count_files_in_dir, copy_and_rename_files

configs = Properties()
with open('D:/Projects/Pycharm/TwitBot/twitbot/resources/path.properties', 'rb') as read_prop:
    configs.load(read_prop)

# Source folders for screenshots of games
cyberpunk_2077_src_path = configs.get('cyberpunk-2077-ss-src-path').data
minecraft_src_path = configs.get('minecraft-ss-src-path').data
elden_ring_src_path = configs.get('elden-ring-ss-src-path').data

videogame_dataset_path = configs.get("video-game-dataset-path").data

game_list = ['MINECRAFT', 'CYBERPUNK_2077', 'ELDEN_RING']

# Code to move and rename screenshots
# des_path = os.path.join(videogame_dataset_path, game_list[2])
# src_path = elden_ring_src_path
# copy_and_rename_files(src_path, des_path)

# Code to update image info for a game to database
def update_image_db_for_game(game_id):
    pass