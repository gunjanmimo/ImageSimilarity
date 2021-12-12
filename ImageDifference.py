import warnings
warnings.filterwarnings("ignore")
# required libraries
from PIL import Image,ImageStat
import numpy as np




class ImageDifference:
    def __init__(self):
        self.image1 = None
        self.image2 = None
      
    
    
    def calculateDifference(self,imgPath1,imgPath2):
        print(f"Calculating difference b/w Image 1:{imgPath1} and Image 2:{imgPath2}")
        # reading image files
        self.image1 = Image.open(imgPath1)
        self.image2 = Image.open(imgPath2)
        # calling functions
        print(self.getBrightnessDifference())
   
        
    # method to calculate brightness difference b/w two images
    def getBrightnessDifference(self):
        '''
        approach: convert image to Grayscale and calculate 
        the average pixel brightness
        '''
        img1 = self.image1.convert('L')
        img2 = self.image2.convert('L')
        stat1 = ImageStat.Stat(img1)
        stat2 = ImageStat.Stat(img2)
        
        if stat1.mean[0] > stat2.mean[0]:
            diff = ((stat1.mean[0] - stat2.mean[0])/stat1.mean[0])*100
            diff = str(round(diff,2))+"%"
            return "Image 1 has {} more brightness than Image 2".format(diff)
        else:
            diff = ((stat2.mean[0] - stat1.mean[0])/stat2.mean[0])*100
            diff = str(round(diff,2))+"%"
            return "Image 2 has {} more brightness than Image 1".format(diff)
       


        


if __name__ == "__main__":
    # all the given image files
    image1 = "./Image/DJI_0042.JPG"
    image2 = "./Image/DJI_0047.JPG"
    image3 = "./Image/DJI_0048.JPG"
    image4 = "./Image/DJI_0103.JPG"
    image5 = "./Image/DJI_0141.JPG"
    
    # init instance of ImageDifference class
    imageDifference = ImageDifference()
    
    # calculating difference b/w every pair of images
    imageDifference.calculateDifference(image1,image2)
    print("-"*30)
    imageDifference.calculateDifference(image1,image3)
    print("-"*30)
    imageDifference.calculateDifference(image1,image4)
    print("-"*30)
    imageDifference.calculateDifference(image1,image5)
    print("-"*30)
    imageDifference.calculateDifference(image2,image3)
    print("-"*30)
    imageDifference.calculateDifference(image2,image4)
    print("-"*30)
    imageDifference.calculateDifference(image2,image5)
    print("-"*30)
    imageDifference.calculateDifference(image3,image4)
    print("-"*30)
    imageDifference.calculateDifference(image3,image5)
    print("-"*30)
    imageDifference.calculateDifference(image4,image5)
    
    