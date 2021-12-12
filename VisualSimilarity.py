import warnings
warnings.filterwarnings("ignore")
import cv2
from keras.models import Model
import tensorflow as tf
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Similarity:
    def __init__(self):
        # using vgg16 flatten layer to get flatten image with extracted feature from previous layers
        self.vgg16 = tf.keras.applications.VGG16(weights='imagenet', include_top=True, pooling='max', input_shape=(224, 224, 3))
        self.basemodel = Model(inputs=self.vgg16.input, outputs=self.vgg16.get_layer('fc2').output)

    # method to get feature vector of img
    def get_feature_vector(self,img):
        img = cv2.resize(img, (224, 224))
        feature_vector = self.basemodel.predict(img.reshape(1, 224, 224, 3))
        return feature_vector

    # method to calculate image similarity
    def getSimilarity(self,img_1, img_2):
       
        img_1 = np.array(img_1)
        img_2 = np.array(img_2)

        vector1 = self.get_feature_vector(img_1)
        vector2 = self.get_feature_vector(img_2)

        similarity = cosine_similarity(vector1, vector2) 
        similarity = str(round(similarity[0][0]*100,2))+"%"
        return f"Image 1 is {similarity} similar to Image 2"



