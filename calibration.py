import numpy as np
import cv2
import tkinter as tk

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        mouseX,mouseY = x,y


img = cv2.imread("test_img1.jpg")
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("size:", screen_width, screen_height)


while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        cv2.rectangle(img, (round(screen_width*0.039), round(screen_height*0.756)),(round(screen_width*0.234),round(screen_height*0.84)),(0,255,0),6)
        # print(mouseX,mouseY)
    elif k == ord('q'):
        break

cv2.destroyAllWindows()