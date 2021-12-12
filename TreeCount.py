import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
import numpy as np

class TreeCount:
    def __init__(self):
        self.img = None
    
    # method to count total number of tree from a image
    
    def getTotalTreeCount(self, img):
        self.img = img
        # BGR to HSV convertion
        '''
        We need the V channel of HSV image for further steps
        '''
        hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Applying OTSU thresholding on HSV image with range 120 - 210
        _, binary_image = cv2.threshold(hsvImage[:, :, 2], 120, 210, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # Applying median filter to remove some noise from the binary image
        denoisedImage = filters.median(binary_image, selem=np.ones((5, 5)))

        binary_image = denoisedImage
        
        # 4x4 kernel to do morphological closing to make the regions of interests - trees more dominant
        kernel = np.ones((4, 4), dtype='uint8')
        morph_closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
        
        # Applying distance transfrom for more accuracy 
        dist_transform_image = cv2.distanceTransform(morph_closed_image, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)

        # Applying padding to the image
        border_size = 25
        dist_border = cv2.copyMakeBorder(dist_transform_image, border_size, border_size, border_size, border_size, 
                                cv2.BORDER_CONSTANT | cv2.BORDER_ISOLATED, 0)

        
        # Using Temple matching technique
        '''
        I cropped a tree portion from given image for template matching 
        '''
        gap = 8

        template_file = cv2.imread('./template.JPG')
        template_file = cv2.resize(template_file, (64, 64))
        # converting template image BGR to HSV
        template_file = cv2.cvtColor(template_file, cv2.COLOR_BGR2HSV)

        _, kernel2 = cv2.threshold(template_file[:, :, 2], 120, 210, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Applying median filtering on the tree teamplate
        denoisedImage = filters.median(kernel2, selem=np.ones((5, 5)))
        kernel2 = denoisedImage

        for i in range(len(kernel2)):
            for j in range(len(kernel2[i])):
                if kernel2[i][j] != 0:
                    kernel2[i][j] = 1
        
        # Applying padding to template image
        kernel2 = cv2.copyMakeBorder(kernel2, gap, gap, gap, gap, cv2.BORDER_CONSTANT | cv2.BORDER_ISOLATED, 0)
        
        # Applying distance transform on the template image
        dist_trans_template = cv2.distanceTransform(kernel2, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
        
        # Matching template image on the output of distance transform image of main input image
        template_matched = cv2.matchTemplate(dist_border, dist_trans_template, cv2.TM_CCOEFF_NORMED)

        # Applying thresholding on the template matched image
        _, peaks = cv2.threshold(template_matched, 0.10, 0.60, cv2.THRESH_BINARY)

        # Going with the peak value of the template matched image
        peaksMatched = cv2.convertScaleAbs(peaks)

        # Finding the contours in the peaks
        contours, _  = cv2.findContours(peaksMatched, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        peaksMatched = cv2.convertScaleAbs(peaks)
   
        # count the contours
        count = 0
        for i in range(len(contours)):
            if cv2.contourArea(contours[i]) < 150:
                continue    
            count += 1

        return count