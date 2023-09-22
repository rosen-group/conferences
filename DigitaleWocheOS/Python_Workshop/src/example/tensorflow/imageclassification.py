from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

IMAGE_PATH = "./images"

# Load input data specific to an on-device ML app.
data = DataLoader.from_folder(IMAGE_PATH)
train_data, test_data = data.split(0.9)

# Customize the TensorFlow model.
model = image_classifier.create(train_data, epochs=5, shuffle=True, batch_size=256)

# Evaluate the model.
loss, accuracy = model.evaluate(test_data)

# Export to Tensorflow Lite model and label file in `export_dir`.
model.export(export_dir='./dogs')
