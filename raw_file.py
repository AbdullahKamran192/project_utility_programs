import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np


def read_raw_image_method(img):


    # instance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # detect text on image
    text_ = reader.readtext(img)

    threshold = 0.25
    # draw bbox and text
    for t_, t in enumerate(text_):
        #print(t)

        bbox, text, score = t

        if score > threshold:
            cv2.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
            cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
        
        return text
    
    return ""

    #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    #plt.show()