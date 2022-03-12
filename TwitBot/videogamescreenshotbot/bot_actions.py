import json
import os

from PIL import Image
from jproperties import Properties

import twitbot.common.databasehandler.database_connector as db
import twitbot.common.filemanagement.file_manager as fm
import twitbot.imagerecognition.google_vision as vision

from twitbot.common.databasehandler.image_db_operations import add_predicted_image_details_to_db
from twitbot.common.databasehandler.videogame_metadata_operations import add_game_metadata_to_db, \
    get_game_metadata_from_db

# Code to copy and rename screenshots
from twitbot.endpoints.tweet import tweet_img
from twitbot.endpoints.upload import upload_img


def copy_and_rename(src_path, des_path):
    fm.copy_and_rename_files(src_path, des_path)


# Code to add game metadata to database
def add_game_metadata(game_id, game_name, game_hashtags, game_dev_twitter_id):
    add_game_metadata_to_db(database, game_id, game_name, game_hashtags, game_dev_twitter_id)


# Code to prepare tweet
def prepare_tweet_text_for_screenshot_recognition(game_name, game_hashtags, game_dev_twitter_id, predicted_labels):
    tweet = 'I think that this screenshot from {} has :'.format(game_name)
    for predicted_label in predicted_labels:
        tweet += '\n{} : {score:.2f}%'.format(predicted_label.get('label'), score=predicted_label.get('score') * 100)
    tweet += '\n{}'.format(game_dev_twitter_id)
    tweet += '\n{}'.format(game_hashtags)
    return tweet


# Main
configs = Properties()
with open('D:/Projects/Pycharm/TwitBot/twitbot/resources/path.properties', 'rb') as read_prop:
    configs.load(read_prop)

# Source folders for screenshots of games
cyberpunk_2077_src_path = configs.get('cyberpunk-2077-ss-src-path').data
minecraft_src_path = configs.get('minecraft-ss-src-path').data
elden_ring_src_path = configs.get('elden-ring-ss-src-path').data

videogame_dataset_path = configs.get('video-game-dataset-path').data
ai_recognized_dataset_path = configs.get('ai-recognized-dataset-path').data

game_list = ['MINECRAFT', 'CYBERPUNK_2077', 'ELDEN_RING']

# Config parameters
confidence = 0.7
min_labels = 3
ignore_labels = ['World', 'Sky', 'Cloud', 'Cg artwork', 'Terrain', 'Biome', 'Landscape', 'Lighting', 'Atmosphere',
                 'Purple', 'Green', 'Red', 'Pink', 'White', 'Flash photography', 'Violet', 'Magenta', 'Blue',
                 'Entertainment', 'Performing arts', 'Aqua', 'Light', 'Vehicle', 'Motor vehicle', 'Tire', 'Games',
                 'Lens flare', 'Recreation', 'Space']

database = db.connect_img_db()

# des_path = os.path.join(videogame_dataset_path, game_list[2])
# src_path = elden_ring_src_path
# copy_and_rename_files(src_path, des_path)

# game_id = game_list[2]
# game_name = 'Elden Ring'
# game_hashtags = '#EldenRing #FromSoft #SoulsLike'
# game_dev_twitter_id = '@ELDENRING'
# game_path_property_name = 'elden-ring-ss-src-path'

# game_id = game_list[1]
# game_name = 'Cyberpunk 2077'
# game_hashtags = '#Cyberpunk2077 #PhotoMode #CDPR'
# game_dev_twitter_id = '@CyberPunkGame'
# game_path_property_name = 'minecraft-ss-src-path'

# game_id = game_list[0]
# game_name = 'Minecraft'
# game_hashtags = '#Minecraft #Shaders'
# game_dev_twitter_id = '@Minecraft'
# game_path_property_name = 'elden-ring-ss-src-path'

# add_game_metadata_to_db(database, game_id, game_name, game_hashtags, game_dev_twitter_id, game_path_property_name)

game_id = game_list[1]

game_details = get_game_metadata_from_db(database, game_id)
game_name = game_details[1]
game_hashtags = game_details[2]
game_dev_twitter_id = game_details[3]
game_path_property_name = game_details[4]

game_path = os.path.join(videogame_dataset_path, game_id)
image_path = os.path.join(game_path, fm.get_random_file_name(game_path))
label_annotations = vision.detect_labels(image_path)
predicted_labels = vision.get_predicted_labels(label_annotations, confidence, ignore_labels)

# Move image to AI_RECOGNIZED
move_img_name = str(fm.count_files_in_dir(ai_recognized_dataset_path)) + fm.get_file_extension(image_path)
fm.move_and_rename_file(image_path, os.path.join(ai_recognized_dataset_path, move_img_name))

# Set new image path
image_path = os.path.join(ai_recognized_dataset_path, move_img_name)

# Update DB with recognized image details
add_predicted_image_details_to_db(database, move_img_name, predicted_labels, game_id)

# Show user the image and prediction
image = Image.open(image_path)
image.show()
print('Label Annotations : \n {}'.format(label_annotations))
print('Predicted Labels : \n {}'.format(predicted_labels))

if len(predicted_labels) >= min_labels:
    doSendTweet = input('Send Tweet? (Y/N):')
    if doSendTweet == 'Y' or doSendTweet == 'y':
        media_id = upload_img(image_path)
        text = prepare_tweet_text_for_screenshot_recognition(game_name, game_hashtags, game_dev_twitter_id,
                                                             predicted_labels)
        tweet_img(text, str(media_id))
    else:
        print('Tweet Rejected')

db.disconnect_db(database)
