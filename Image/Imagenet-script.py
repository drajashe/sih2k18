
import os
import numpy as np
from keras.preprocessing import image
from keras.layers import merge, Input
from imagenet_utils import preprocess_input, decode_predictions

from keras.layers import Dense, Activation, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.resnet50 import ResNet50

# VGG16

image_input = Input(shape=(224, 224, 3))
model = VGG16(input_tensor=image_input, include_top=True,weights='imagenet')


PATH = os.getcwd()
# Define data path
data_path = PATH + '/input'
data_dir_list = os.listdir(data_path)


img_data_list=[]

for dataset in data_dir_list:
	img_list=os.listdir(data_path+'/'+ dataset)
	print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
	for img in img_list:
		img_path = data_path + '/'+ dataset + '/'+ img
		img = image.load_img(img_path, target_size=(224, 224))
		x = image.img_to_array(img)
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
		img_data_list.append(x)
        preds = model.predict(x)
        print(' Predicted class : ', decode_predictions(preds))

# ResNet50

image_input = Input(shape=(224, 224, 3))
model = ResNet50(input_tensor=image_input, include_top=True,weights='imagenet')

PATH = os.getcwd()
# Define data path
data_path = PATH + '/input'
data_dir_list = os.listdir(data_path)


img_data_list=[]

for dataset in data_dir_list:
	img_list=os.listdir(data_path+'/'+ dataset)
	print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
	for img in img_list:
		img_path = data_path + '/'+ dataset + '/'+ img
		img = image.load_img(img_path, target_size=(224, 224))
		x = image.img_to_array(img)
		x = np.expand_dims(x, axis=0)
		x = preprocess_input(x)
		img_data_list.append(x)
        preds = model.predict(x)
        print(' Predicted class : ', decode_predictions(preds))

# ---------------------------------------------------------------------------

img_path = 'input/Animals/14.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
print('Input image shape:', x.shape)

preds = model.predict(x)
print('Predicted:', decode_predictions(preds))
