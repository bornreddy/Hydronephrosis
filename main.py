import numpy as np
import cv2, cv
 
# Define a on_mouse function. 
parenchyma = []
def on_mouse(event, x, y, flags, params):
  if event == cv.CV_EVENT_LBUTTONDOWN:
    print 'Mouse Position: '+str(x)+', '+str(y)
    parenchyma.append((x,y))
    # print "parenchyma so far:"
    # print_par()
    if (len(parenchyma) > 1):
      cv2.line(img, parenchyma[-2], parenchyma[-1], (255,0,0), 1)
      cv2.imshow('image', img)

#test function - prints array of parenchyma parameter
def print_par():
  for p in parenchyma:
    print p

# Set up image window
img = cv2.imread('lt_long.jpg', 0)
cv2.imshow('image', img)
cv.SetMouseCallback('image', on_mouse, 0)

def draw_p_area():
  for x in range( 1, (len(parenchyma)-1) ):
    points = np.array([parenchyma[0], parenchyma[x], parenchyma[x+1]])
    cv2.polylines(img, np.int32([points]), 1, (255,255,255))
    cv2.imshow('image',img)

while(1):
  # wait indefinitely for a key to be pressed
  k = cv2.waitKey(0)
  # if key pressed is 'enter' connect first and last point, and calculate area.
  if (k == 13):
    cv2.line(img, parenchyma[0], parenchyma[-1], (255,0,0), 1)
    cv2.imshow('image', img)
    draw_p_area()
  # if key pressed is 'esc' close window
  elif (k == 27):
    cv2.destroyAllWindows()

    break 
