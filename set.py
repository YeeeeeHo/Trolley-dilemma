import os
import shutil
import random

# 예시 폴더 경로

def classify_images(input_folder, output_left_folder, output_right_folder,auv_folder):
# 이미지를 무작위로 왼쪽 갈림길 또는 오른쪽 갈림길로 이동
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg')):
            img_path = os.path.join(input_folder, filename)

            # 이미지 번호에 따라 무작위로 왼쪽 또는 오른쪽 갈림길로 분류
            random_choice = random.choice([0, 1, 2])
            if random_choice == 0:
                selected_folder = output_left_folder
            elif random_choice == 1:
                selected_folder = output_right_folder
            else:
                selected_folder = auv_folder

            os.makedirs(selected_folder, exist_ok=True)

            # 현재 갈림길에 이미 배치된 이미지 개수
            num_people_in_folder = len(os.listdir(selected_folder))
            
            
            # 무작위로 이미지 개수 부여 (최대 5명까지)
            max_people_in_folder = random.randint(0, 5)

            if num_people_in_folder < max_people_in_folder:
                # 선택된 갈림길에 이미지 복사
                new_img_path = os.path.join(selected_folder, filename)
                shutil.copy(img_path, new_img_path)

print("이미지 분류가 완료되었습니다.")