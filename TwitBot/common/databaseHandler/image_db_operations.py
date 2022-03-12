import json


def add_predicted_image_details_to_db(database, image_path, predicted_labels, game_id):
    cursor = database.cursor()
    query = "INSERT INTO image_db.videogame_image_dataset(image_path, predicted_labels, game_id) VALUES(%s,%s,%s); "
    values = [image_path, json.dumps(predicted_labels), game_id]
    cursor.execute(query, values)
    database.commit()
