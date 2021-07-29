import numpy as np
import cv2
from PIL import Image
import base64
import io
from com.chaquo.python import Python
from os.path import dirname, join
import os
from ArabicOcr import arabicocr


def main(image_name):
    data_dir = os.path.join('/storage/emulated/0/Android/data/com.test.myapplication/files/Pictures/'+image_name, 'DCIM')
    image_find = data_dir
    results = arabicocr.arabic_ocr(image_find, 'out.jpg')
    print(results)
    words = []
    for i in range(len(results)):
        word = results[i][1]
        words.append(word)

    return str(words)
