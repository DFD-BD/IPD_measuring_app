import cv2
from f_measurents import *


# Config
import config
import os
landmarks = config.landmarks
top_to_bottom_angle_ref = config.top_to_bottom_angle_ref
top_to_bottom_angle_max_deviation = config.top_to_bottom_angle_max_deviation
left_to_right_angle_ref = config.left_to_right_angle_ref
left_to_right_angle_max_deviation_perc = config.left_to_right_angle_max_deviation_perc
area_ratio_right_to_left_max_deviation_perc = config.area_ratio_right_to_left_max_deviation_perc
area_ratio_right_to_left_ref = config.area_ratio_right_to_left_ref
# 
interactive_plot = True





cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:


    frame = process_image(frame, landmarks, top_to_bottom_angle_ref, top_to_bottom_angle_max_deviation, left_to_right_angle_ref, left_to_right_angle_max_deviation_perc, area_ratio_right_to_left_max_deviation_perc, area_ratio_right_to_left_ref)

    cv2.imshow("preview", frame)

    rval, frame = vc.read()


    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")