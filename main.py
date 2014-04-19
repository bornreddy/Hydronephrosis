import numpy as np
import cv2, cv
 
# Define a on_mouse function. 
parenchyma = []
def on_mouse(event, x, y, flags, params):
  if event == cv.CV_EVENT_LBUTTONDOWN:
    print 'Mouse Position: '+str(x)+', '+str(y)
    parenchyma.append((x,y))
    if (len(parenchyma) > 1):
      cv2.line(img, parenchyma[-2], parenchyma[-1], (255,0,0), 1)
      cv2.imshow('image', img)

#test function - prints array of parenchyma parameter
def print_par():
  print "parenchyma so far:"
  for p in parenchyma:
    print p
    print "p[0]: " + str(p[0])
    print "p[1]: " + str(p[1])

# Set up image window
img = cv2.imread('lt_long.jpg', 0)
cv2.imshow('image', img)
cv.SetMouseCallback('image', on_mouse, 0)

#works for likely kidney shapes - only works on some nonconvex shapes :(
def draw_p_area():

  x_average = 0
  y_average = 0
  for z in range(0, len(parenchyma) ):
    x_average = x_average + parenchyma[z][0]
    y_average = y_average + parenchyma[z][1]
  x_average = x_average/len(parenchyma)
  y_average = y_average/len(parenchyma)
  # print_par()
  print "xaverage: " + str(x_average)
  print "yaverage: " + str(y_average)
  for x in range( 0, (len(parenchyma)-1) ):
    points = np.array([[x_average, y_average], parenchyma[x], parenchyma[x+1]])
    cv2.polylines(img, np.int32([points]), 1, (255,255,255))
    cv2.imshow('image',img)
  points = np.array([[x_average,y_average], parenchyma[0], parenchyma[-1]])
  cv2.polylines(img, np.int32([points]), 1, (255,255,255))
  cv2.imshow('image',img)



#algorithm to find the area of the nonregulare polygon (parenchyma)
def calculate_p_area():
  a_val = 0
  b_val = 0
  for z in range( 0, (len(parenchyma)-1) ):
    a_val = a_val + parenchyma[z][0]*parenchyma[z+1][1]
    b_val = b_val + parenchyma[z][1]*parenchyma[z+1][0]
  print "a_val: " + str(a_val)
  print "b_val: " + str(b_val)
  print "area: " + str(((a_val-b_val)/2))


while(1):
  # wait indefinitely for a key to be pressed
  k = cv2.waitKey(0)
  # if key pressed is 'enter' connect first and last point, and calculate area.
  if (k == 13):
    cv2.line(img, parenchyma[0], parenchyma[-1], (255,0,0), 1)
    cv2.imshow('image', img)
    calculate_p_area()
    draw_p_area()
  # if key pressed is 'esc' close window
  elif (k == 27):
    cv2.destroyAllWindows()

    break 
