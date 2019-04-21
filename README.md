# License Plate Straightener
This project takes in an image of a cars License plate and uses image processing to straighten it. It can also be used to give a top down view of any Document.
The aim of this project was to straigten tilted licence plates for easy License place Text Extraction


# Prequisites
1.*Python 3*  
2.*Open CV* - OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision. In simple language it is library used for Image Processing. It is mainly used to do all the operation related to Images.
3.*Numpy*  
4.*imutils* -  Provides convenient functions to make basic image processing functions such as translation, rotation, resizing, etc with OpenCV  
To check your python version  type in command line  
 ```python --version```  
## Installing
 To install openCV type  
 ```pip install opencv```  
 Numpy is automatically installed with OPenCv  
  To install imutils  
 ```pip install imutils```  

# Running Tests

Start of by feeding an image : We start of with a sample *image courtesy google.com , and then resize the image
![Sample Image of a License Plate](https://github.com/ShakirKhurshid/Transformer/blob/master/Sample_Pictures/Test/11.jpg) *sample image of a license plate*

Then we gray out the image for better pre processing:
```gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ```

Then Clipped Local Adaptive Histogram Equalization (CLAHE) is applied to get better contrast.CLAHE is an advancement on AHE. AHE has a drawback of overamplifying noise. CLAHE limits the amplification by clipping the histogram at a predefined value (called clip limit) before computing the CDF.  

```clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  
   cl1 = clahe.apply(gray) 
   cv2.imshow('c1',cl1)
```
![Clahe](https://github.com/ShakirKhurshid/Transformer/blob/master/Sample_Pictures/Test/CLAHE.jpg)  
*clahe* 

Then Thresholding is applied to get the binary image :``` thresh = cv2.threshold(cl1, 165, 255,cv2.THRESH_BINARY)[1]```
![Threshold](https://github.com/ShakirKhurshid/Transformer/blob/master/Sample_Pictures/Test/Threshold.jpg)  
*threshold*

Find countours in the thresholded image ,and sort the contours in decreasing order  

``` cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10] #Stores the biggest 10 contours```  

In contours whose area is >5000 as license plate will be one of the biggest contour in the image , draw a bounding rectangle ```rect = cv2.minAreaRect(c)``` around the contour and get  the coordinates of the bounding rectangle using ``` box = cv2.boxPoints(rect)```  
![Detected License Plate](https://github.com/ShakirKhurshid/Transformer/blob/master/Sample_Pictures/Test/Detected.PNG)  
*detectedLicense Plate*

Now the four_point_transformed function is called which take in the image and the coordinates of the bounding rectange as parameteres and performs the transformation, to give the top down view of the ROI and thus straightenes the License Plate  
![Transformed](https://github.com/ShakirKhurshid/Transformer/blob/master/Sample_Pictures/Test/Transformed.jpg)  
*transformed* 

This code worked for almost all license plates 
>can be used to detect and straigten a document in an image

# EXECUTION
execute the file ' run_transformer.py'
```python run_transformer.py```











