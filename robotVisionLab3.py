import cv2
import numpy as np

# keep running total of each
blueTotal = 0
greenTotal = 0
yellowTotal = 0
orangeTotal = 0
brownTotal = 0
redTotal = 0
defaultTotal = 0

circleList = []
count = 0

def onClick(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            # helper function to get thresholds
            print(original[y, x])

original = cv2.imread("candyBigSmallerTiny.jpg", cv2.IMREAD_COLOR)

# use blur with 5x5 mask
blur = cv2.blur(original, (5, 5), 0)
# use canny edge detection
edge = cv2.Canny(blur, 5, 150)

# ref from https://opencv2-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
houghCircles = cv2.HoughCircles(edge,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=9,minRadius=10,maxRadius=15)
houghCircles = np.uint16(np.around(houghCircles))

# Circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
for circle in houghCircles[0,:]:
    drawCircles = np.zeros((original.shape[0], original.shape[1]), np.uint8)
    # thickness at -1 so the circles dont get drawn and ensure they arent touching
    cv2.circle(drawCircles,(circle[0], circle[1]), circle[2]-5, (255, 255, 255), -1)
    circleList.append(drawCircles)

for img in circleList:
    rgb = cv2.mean(original, mask = img)
    count += 1
    current = houghCircles[0,count-1]

    # just checking of each circle is within thresholds
    #blue
    #blue vals ~ [252,185,0] - [255,172,0]
    if (int(rgb[0]) in range(220, 255) and int(rgb[1]) in range(140, 195) and int(rgb[2]) in range(0, 30)):
        blueTotal += 1
        cv2.circle(original, (current[0], current[1]), current[2], (0,255,0), 1)

    #orange
    #orange vals ~ [17,83,226] - [62,127,249]
    elif (int(rgb[0]) in range(5,80) and int(rgb[1]) in range(10,130) and int(rgb[2]) in range(220,255)):
        orangeTotal += 1
        cv2.circle(original, (current[0], current[1]), current[2], (0,255,0), 1)

    #yellow
    #yellow vals ~ [0,238,255] - [53,196,204]
    elif (int(rgb[0]) in range(0,50) and int(rgb[1]) in range(196,240) and int(rgb[2]) in range(200,255)):
        yellowTotal += 1
        cv2.circle(original, (current[0],current[1]), current[2],(0,255,0), 1)

    #brown
    #brown vals ~ [94,88,83] - [174,153,131]
    elif (int(rgb[0]) in range(2,175) and int(rgb[1]) in range(3,155) and int(rgb[2]) in range(7,130)):
        brownTotal += 1
        cv2.circle(original,(current[0], current[1]),int(current[2]),(0,255,0), 1)

    #green
    #green vals ~ [24,121,5]- [96,215,0]
    elif (int(rgb[0]) in range(24,244) and int(rgb[1]) in range(120,250) and int(rgb[2]) in range(0,24)):
        greenTotal += 1
        cv2.circle(original, (current[0], current[1]), current[2], (0,255,0),1)

    #red
    #red vals ~ [23,14,164] - [106,87,220]
    elif (int(rgb[0]) in range(55,140) and int(rgb[1]) in range(14,165) and int(rgb[2]) in range(152,220)):
        redTotal += 1
        cv2.circle(original, (current[0], current[1]), current[2], (0,255,0), 1)

    else:
        defaultTotal += 1

cv2.putText(original,("Blue: " + str(blueTotal)), (225, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

cv2.putText(original,("Orange: " + str(orangeTotal)), (225, 60), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,255,0),1,cv2.LINE_AA)

cv2.putText(original,("Yellow: " + str(yellowTotal)), (225, 90), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

cv2.putText(original,("Brown: " + str(brownTotal)), (225, 120), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

cv2.putText(original,("Green: " + str(greenTotal)), (225, 150), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

cv2.putText(original,("Red: " + str(redTotal)), (225, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

# show the image
cv2.imshow("img", original)
cv2.setMouseCallback('img', onClick)

cv2.waitKey(0)
cv2.destroyAllWindows()
