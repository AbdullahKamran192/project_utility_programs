import cv2
from image_adjustment import read_adjusted_image_method
from raw_file import read_raw_image_method
import time

correct_plates_text = {
    "plate1": "RV59 VRO",
    "plate2": "LY66 FCO",
    "plate3": "EK67 XUL",
    "plate4": "EY66 ZXC",
    "plate5": "JCC 3P",
    "plate6": "ND66 YEJ",
    "plate7": "KY68 WZM",
    "plate8": "LB02 APF",
    "plate9": "BN65 GTU",
    "plate10": "SJ10 HLR",
    "plate11": "MY 2 OHMS", # remove this plate, no one really knows if its 0 or O
    "plate12": "NO67 GAS"
}

def test_images_method2():

    correct_plates_read_count = 0

    for i in range(1,12):
        plate = f"plate{i}"
        image_path = f'data/{plate}.jpg'
        img = cv2.imread(image_path)

        for thresh_value in range(0, 255, 10):

            plate_text = read_adjusted_image_method(img, thresh_value=thresh_value)

            print(f"The {plate} is {plate_text.upper()}.")

            plate_text = plate_text.upper()

            if plate_text == correct_plates_text.get(plate):
                print(f"{plate_text} was read correctly")
                correct_plates_read_count += 1
                break
        
    
    print(f"{correct_plates_read_count} plates were read correctly")

def test_image_threshes(filename):
    image_path = f'data/{filename}.jpg'
    img = cv2.imread(image_path)

    for thresh_value in range(0, 255, 10):
        plate_text = read_adjusted_image_method(img, thresh_value=thresh_value)

        print(f"The {filename} is {plate_text.upper()}.")

        plate_text = plate_text.upper()

        if plate_text == correct_plates_text.get(filename):
            print(f"{plate_text} was read correctly")
            break


def test_image(filename):
    correct_plates_read_count = 0

    image_path = f'data/{filename}.jpg'
    img = cv2.imread(image_path)

    plate_text = read_adjusted_image_method(img)

    print(f"The {filename} is {plate_text.upper()}.")

    plate_text = plate_text.upper()

    if plate_text == correct_plates_text.get(filename):
        print(f"{plate_text} was read correctly")
        correct_plates_read_count += 1

#Reads the raw images
def test_images_method1():

    correct_plates_read_count = 0

    for i in range(1, 12):
        plate = f"plate{i}"
        image_path = f'data/{plate}.jpg'
        img = cv2.imread(image_path)

        plate_text = read_raw_image_method(img)

        print(f"The {plate} is {plate_text.upper()}.")

        plate_text = plate_text.upper()

        if plate_text == correct_plates_text.get(plate):
            print(f"{plate_text} was read correctly")
            correct_plates_read_count += 1

    print(f"{correct_plates_read_count} plates were read correctly")



test_images_method2()