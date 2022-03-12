def add_game_metadata_to_db(database, game_id, game_name, game_hashtags, game_dev_twitter_id, game_path_property_name):
    cursor = database.cursor()
    query = "INSERT INTO image_db.videogame_metadata(game_id, game_name, game_hashtags, game_dev_twitter_id, " \
            "game_path_property_name) VALUES(%s,%s,%s,%s,%s); "
    values = [game_id, game_name, game_hashtags, game_dev_twitter_id, game_path_property_name]
    cursor.execute(query, values)
    database.commit()


def get_game_metadata_from_db(database, game_id):
    cursor = database.cursor()
    query = "SELECT * FROM image_db.videogame_metadata WHERE game_id = %s;"
    values = [game_id]
    cursor.execute(query, values)
    return cursor.fetchall()[0]
