


from Transform  import four_point_transform
import numpy as np
import cv2
import imutils




# Input image"
image = cv2.imread("Sample_Pictures/Test/11.jpg")   #Path to image
ratio = image.shape[0] / 300.0
orig = image.copy()
image = imutils.resize(image, height = 300)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#noise_removal = cv2.bilateralFilter(gray,9,75,75)


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(gray)
cv2.imshow('c1',cl1)

#cv2.imshow('noise_removal',noise_removal)
#equ = cv2.equalizeHist(noise_removal)
#cv2.imshow('histo',equ)



thresh = cv2.threshold(cl1, 165, 255,cv2.THRESH_BINARY)[1]
cv2.imshow('thresh',thresh)
    #Adaptive Thresholding
#thresh= cv2.adaptiveThreshold(t1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#cv2.imshow('A_thresh',thresh)



# Finds contours
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:3]
#screenCnt = None
# Draws contours
for c in cnts:

    if cv2.contourArea(c)  < 5000:
        continue
    print("area",cv2.contourArea(c))
    #(x, y, w, h) = cv2.boundingRect(c)
    #cv2.rectangle(image, (x,y), (x+w,y+h), (0, 255, 0), 2)

    ## BEGIN - draw rotated rectangle
    print("test")
    rect = cv2.minAreaRect(c)
    print("areas",rect)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print(box)
    cv2.drawContours(image,[box],0,(0,255,0),2)
    break  #Boss Line



warped = four_point_transform(image, box)
#cv2.imwrite('warped.jpg', warped)
 
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()