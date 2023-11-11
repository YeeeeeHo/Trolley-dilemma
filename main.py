import os
import shutil
import random
from set import classify_images  # set.py에서 classify_images 함수를 import

# 예시 폴더 경로
input_folder = "../Trolley-dilemma/iamge"
output_left_folder = "../Trolley-dilemma/left_folder"
output_right_folder = "../Trolley-dilemma/right_folder"

# set.py의 classify_images 함수 호출
classify_images(input_folder, output_left_folder, output_right_folder)
