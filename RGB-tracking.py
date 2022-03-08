import cv2
def do_nothing (x):
    pass
cv2.namedWindow('Track Bars', cv2.WINDOW_NORMAL)
cv2.createTrackbar('min_blue', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('min_green', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('min_red', 'Track Bars', 0, 255, do_nothing)

cv2.createTrackbar('max_blue', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('max_green', 'Track Bars', 0, 255, do_nothing)
cv2.createTrackbar('max_red', 'Track Bars', 0, 255, do_nothing)

img = cv2.imread('blue-flower-2.jpeg')
img = cv2.resize(img, (600, 426))
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow('HSV Image', cv2.WINDOW_NORMAL)
cv2.imshow('HSV Image',img_hsv)

while True:
    min_blue = cv2.getTrackbarPos('min_blue', 'Track Bars')
    min_green = cv2.getTrackbarPos('min_green', 'Track Bars')
    min_red = cv2.getTrackbarPos('min_red', 'Track Bars')

    max_blue = cv2.getTrackbarPos('max_blue', 'Track Bars')
    max_green = cv2.getTrackbarPos('max_green', 'Track Bars')
    max_red = cv2.getTrackbarPos('max_red', 'Track Bars')

    mask = cv2.inRange(img_hsv,
                       (min_blue, min_green, min_red),
                       (max_blue, max_green, max_red))

    cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
    cv2.imshow('Mask', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
print('min_blue, min_green, min_red = {0}, {1}, {2}'.format(min_blue, min_green,
                                                            min_red))
print('max_blue, max_green, max_red = {0}, {1}, {2}'.format(max_blue, max_green,
                                                            max_red))
