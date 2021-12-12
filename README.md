# Image Similarity

### TODO/IDEA:

1. Calculate brightness difference of two images, which indicates if the image was taken in sunny day or cloudy day
2. Count total no of tree and calculate the difference of tree of two images
3. check visual similarity b/w two images

### custom module details

1. TreeCount: Used different image processing steps to get contours and calculate no of contours using template matching
2. VisualSimilarity: Used pre-trained model VGG16 and used the model upto flatten layer for the similarity calculation and here I used cosine similarity to calculate similarity b/w two input images

### Steps to run the code

1. use **requirements.txt** to install necessary modules

```
pip install -r requirements.txt
```

2. Run the python file using

```
python ImageDifference.py
```
