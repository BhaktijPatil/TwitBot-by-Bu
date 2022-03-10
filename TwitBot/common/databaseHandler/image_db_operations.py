def add_entry_video_game_image_dataset(database, image_path, image_label_detection_response, expected_labels,
                                       video_game_name):
    cursor = database.cursor()
    query = "INSERT INTO image_db.video_game_image_dataset(image_path, image_label_detection_response, " \
            "expected_labels, video_game_name) VALUES(%s,%s,%s,%s); "
    values = [image_path, image_label_detection_response, expected_labels, video_game_name]
    cursor.execute(query, values)
    database.commit()
