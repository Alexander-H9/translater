import numpy as np
import pyautogui
import cv2 as cv
import pytesseract
import tkinter as tk
from deep_translator import GoogleTranslator    # https://pypi.org/project/deep-translator/#quick-start
import time

# IMPORTANT
# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
# still problems? go here -> https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

# get window size and set target area
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
h_b = round(screen_height*0.84)- round(screen_height*0.756)
w_b = round(screen_width*0.315) - round(screen_width*0.039)
y_b = round(screen_height*0.756)
x_b = round(screen_width*0.034)
# print("h, w, x, y", h,w,x,y)

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close() 

def read_and_translate(current_message, translated):
    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv.rectangle(chat_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = chat_img[y:y + h, x:x + w]
        
        # Open the file in append mode
        file = open("recognized.txt", "a")
        
        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        # text.replace("\n", "")
        text = text.rstrip()

        
        if len(text) > 2 and len(text) < 200:
            #print("text: ", text)
            #print("len: ", len(text))
            # translate the text
            translated = GoogleTranslator(source='ru', target='en').translate(text)
        # print("translated:", translated)
        if translated != current_message:
            current_message = translated
            print("\033[92m", current_message)
            # Appending the text into file
            file.write(current_message)
            file.write("\n")
            file.close
        time.sleep(1.0)
        return current_message

print('\033[95m' + "The script will start in 3 secons. Be sure to swap in game.")
# time.sleep(3.0)

current_message = ""
translated = "Welcome to the translater"

while(1):

    screen = image = pyautogui.screenshot()
    img = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
    # img = cv.imread("test_img1.jpg")
    # region of intesst is the chat area
    chat_img = img[y_b:y_b + h_b, x_b:x_b + w_b]

    # Convert the image to gray scale
    gray = cv.cvtColor(chat_img, cv.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    
    # Specify structure shape and kernel size. 
    # Kernel size increases or decreases the area 
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect 
    # each word instead of a sentence.
    rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15)) # 20, 20

    # Appplying dilation on the threshold image
    dilation = cv.dilate(thresh1, rect_kernel, iterations = 1)

    # Finding contours
    contours, hierarchy = cv.findContours(dilation, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    current_message = read_and_translate(current_message, translated)
    # cv.imshow('image',img)

    cv.imshow('chat_img', chat_img)
    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('q'):
        break

# Close the file
file.close
cv.destroyAllWindows()