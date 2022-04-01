import cv2
import time
#import numpy as np

def main():
    video = cv2.VideoCapture(0)
    while 1:
        ret, cam = video.read()
        if ret:
            bw = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
            videoThresh = cv2.threshold(bw, 140, 255, cv2.THRESH_BINARY)[1]
            time.sleep(1 / 30)

            cv2.imshow('frame', videoThresh)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break





if __name__ == '__main__':
    main()