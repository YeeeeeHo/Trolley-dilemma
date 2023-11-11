import os
import shutil
import random

# 예시 폴더 경로
input_folder = "../Trolley-dilemma/iamge"
output_left_folder = "../Trolley-dilemma/left_folder"
output_right_folder = "../Trolley-dilemma/right_folder"

# 이미지에 숫자를 부여하고 해당 카테고리의 폴더로 이동
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(input_folder, filename)

        # 파일명에서 번호와 카테고리 추출
        try:
            number, category = filename.split('_')
            number = int(number)
        except ValueError:
            continue  # 형식에 맞지 않는 파일은 무시

        # 이미지에 숫자를 부여하고 해당 카테고리의 폴더로 이동
        new_filename = f"{number}_{category}"
        new_img_path = os.path.join(input_folder, new_filename)
        os.rename(img_path, new_img_path)

# 무작위로 왼쪽 또는 오른쪽 갈림길로 이미지 이동
for category in os.listdir(input_folder):
    input_category_folder = os.path.join(input_folder, category)

    if os.path.isdir(input_category_folder):
        for filename in os.listdir(input_category_folder):
            img_path = os.path.join(input_category_folder, filename)

            # 무작위로 왼쪽 또는 오른쪽 갈림길로 분류
            output_folder = output_left_folder if random.choice([True, False]) else output_right_folder

            # 해당 카테고리의 폴더에 이미지 복사
            output_category_folder = os.path.join(output_folder, category)
            os.makedirs(output_category_folder, exist_ok=True)
            shutil.copy(img_path, os.path.join(output_category_folder, filename))

print("이미지 분류가 완료되었습니다.")
