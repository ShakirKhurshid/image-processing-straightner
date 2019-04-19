


from Transform  import four_point_transform
import numpy as np
import cv2
import imutils
import matplotlib as plt



# Input image
image = cv2.imread('6.jpg')
ratio = image.shape[0] / 300.0
orig = image.copy()
image = imutils.resize(image, height = 300)
# Converts to grey for better reults
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

noise_removal = cv2.bilateralFilter(gray,9,75,75)
#cv2.imshow('noise_removal',noise_removal)


#canny=cv2.Canny(noise_removal,60,100)
#cv2.imshow('canny',canny)


thresh = cv2.threshold(noise_removal, 150, 255,cv2.THRESH_BINARY)[1]
cv2.imshow('thresh',thresh)






# Finds contours
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
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
    cv2.drawContours(image,[box],0,(0,191,255),2)
    break  #Boss Line

    ## END - draw rotated rectangle
'''for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.015 * peri, True)
 
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)

#cv2.imwrite('out.png', image)'''

warped = four_point_transform(image, box)
cv2.imwrite('warped.jpg', warped)
 
# show the original and warped images//.
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()