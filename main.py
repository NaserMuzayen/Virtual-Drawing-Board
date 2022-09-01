import cv2 as cv
import HandTrackingModule as ht
# import time
import math

# pTime = 0
wCam, hCam = 650, 490
hand = ht.handDetector()
cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
points = []
while True:
    success, img = cap.read()
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime
    img = cv.flip(img, 1)
    for point in points:
        x, y = point
        x = int(x)
        y = int(y)
        cv.circle(img, (x, y), 5, (235, 120, 14), cv.FILLED)

    img = hand.findHands(img, draw=False)

    positions, box = hand.findPositions(img)
    if len(positions) != 0:
        # Thumb finger
        x1, y1 = positions[4][1:]
        # index finger
        x2, y2 = positions[8][1:]
        # distance between Thumb and index fingers
        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)
        if length <= 70:
            x = (x1 + x2) / 2
            y = (y1 + y2) / 2
            points.append((x, y))

    # cv.putText(img, 'fps : ' + str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
    cv.imshow('image', img)
    key = cv.waitKey(2)
    if key == ord('q') or key == ord('Q'):
        break
cv.destroyAllWindows()
cap.release()
