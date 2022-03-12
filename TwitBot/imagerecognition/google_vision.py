def detect_labels(path):
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    labels = response.label_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return labels


def get_predicted_labels(label_annotations, confidence, ignore_labels):
    predicted_labels = []
    for label_annotation in label_annotations:
        if label_annotation.score >= confidence and not label_annotation.description in ignore_labels:
            label_annotation = {'label': label_annotation.description, 'score': label_annotation.score}
            predicted_labels.append(label_annotation)
    return predicted_labels
