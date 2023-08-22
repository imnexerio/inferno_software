import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
if (video_capture.isOpened() == False):
  print("Unable to read camera feed")

while True:
    frame = video_capture.read()[1]
    image = frame
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 1, 1,apertureSize=7,L2gradient=False)

    contours1=cv2.blur(edges,(5,5),)
    contours, _ = cv2.findContours(contours1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    shapes=['Line','Triangle','Square','Pentagon',"hexagon","Heptagon",'Octagon',"nonagon","circle"]
    centroids = []
    couunt=0

    #red color
    hsvFrame = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    red_lower = np.array([120,50,50], np.uint8)
    red_upper = np.array([139,255,255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # green color
    green_lower = np.array([50, 100, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    #blue color
    blue_lower = np.array([20, 240, 200], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    for contour in contours:
        #print(cv2.arcLength(contour,True))
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        num_vertices = len(approx)
        #print(num_vertices)
        
        moments = cv2.moments(contour)
        if moments['m00'] != 0:
            cX = int(moments['m10'] / moments['m00'])
            cY = int(moments['m01'] / moments['m00'])
            centroids.append((cX, cY))
        
        #print(centroids)



        if num_vertices == 3:
            shape = shapes[1]
        elif num_vertices == 4:
            shape = shapes[2]
        elif num_vertices == 5:
            shape=shapes[3]
        elif num_vertices==6:
            shape=shapes[4]
        elif num_vertices==7:
            shape=shapes[5]
        elif num_vertices==8:
            shape=shapes[6]
        elif num_vertices==9:
            shape=shapes[7]
        else:
            shape = shapes[-1]

        #print(shape)

        # For red color
        res_red = cv2.bitwise_and(image, image, 
                                    mask = red_mask)
            
        # For green color
        res_green = cv2.bitwise_and(image, image,
                                    mask = green_mask)
            
        # For blue color
        res_blue = cv2.bitwise_and(image, image,
                                    mask = blue_mask)
        

        cv2.putText(image, shape, (cX-10, cY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.imshow('Red',res_red)
    cv2.imshow("blue",res_blue)
    cv2.imshow('green',res_green)
    #cv2.imshow('thres',thresh)
    #cv2.imshow('edges',edges)
    #cv2.imshow('bl',contour)
    cv2.imshow("Shape Detection", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()


