import cv2
import numpy as np

def main():
    video = cv2.VideoCapture(4)
    cv2.namedWindow('image')
    while 1:
        ret, cam = video.read()
        #videoThresh = cv2.threshold(cam, 150,255, cv2.THRESH_BINARY)
        cv2.imshow('image', cam)





if __name__ == '__main__':
    main()