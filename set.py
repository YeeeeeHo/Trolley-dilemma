import os
import shutil
import random

# 예시 폴더 경로
input_folder = "../Trolley-dilemma/iamge"
output_left_folder = "../Trolley-dilemma/left_folder"
output_right_folder = "../Trolley-dilemma/right_folder"


max_images_per_branch = 6

# 이미지를 무작위로 왼쪽 또는 오른쪽 갈림길로 이동
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg')):
        img_path = os.path.join(input_folder, filename)

        # 무작위로 왼쪽 또는 오른쪽 갈림길로 분류
        output_folder = output_left_folder if random.choice([True, False]) else output_right_folder
        os.makedirs(output_folder, exist_ok=True)

        # 해당 갈림길 폴더에 이미지 복사 (최대 5개까지)
        if len(os.listdir(output_folder)) < max_images_per_branch:
            shutil.copy(img_path, output_folder)

print("이미지 분류가 완료되었습니다.")