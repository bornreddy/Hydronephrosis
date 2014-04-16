import cv2, cv
 
# Define a on_mouse function. 
parenchyma = []
def on_mouse(event, x, y, flags, params):
  if event == cv.CV_EVENT_LBUTTONDOWN:
    print 'Mouse Position: '+str(x)+', '+str(y)
    parenchyma.append((x,y))
    print "parenchyma so far:"
    print_par()

def print_par():
  for p in parenchyma:
    print p

# Set up image window
img = cv2.imread('lt_long.jpg', 0)
cv2.imshow('image', img)
cv.SetMouseCallback('image', on_mouse, 0)

# cv2.line(img, (0,0), (500,500), (255,0,0), 5)
# cv2.imshow('image', img)
# cv.SetMouseCallback('image', on_mouse, 0)


 
# Wait until a key is pressed to destory all windows
cv2.waitKey(0)
cv2.destroyAllWindows 