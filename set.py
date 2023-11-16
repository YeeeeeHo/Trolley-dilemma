import os
import shutil
import random

# 예시 폴더 경로

def classify_images(input_folder, output_left_folder, output_right_folder, auv_folder):
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

            # wall.jpg 파일이 아닌 경우에만 해당 갈림길에 이미지 복사
            if 'wall.jpg' not in filename:
                # 현재 갈림길에 이미 배치된 이미지 개수
                num_people_in_folder = len(os.listdir(selected_folder))

                # 무작위로 이미지 개수 부여 (최대 5명까지)
                max_people_in_folder = random.randint(0, 5)

                if selected_folder == auv_folder:
                    # 이미지가 어린이인지 확인
                    is_child = 'child' in filename.lower()

                    # 이미지가 어린이인 경우, grand 또는 patient에 해당하는 보호자 이미지 생성
                    if is_child:
                        guardian_type = random.choice(['grand', 'patient'])
                        guardian_filename = filename.replace('child', guardian_type)
                        guardian_path = os.path.join(auv_folder, guardian_filename)

                        # 해당하는 보호자가 없다면 어린이 이미지를 스킵
                        if not os.path.exists(guardian_path):
                            continue

                        # grand 또는 patient 이미지를 강제로 생성해서 넣음
                        guardian_force_filename = filename.replace('child', 'grand' if guardian_type == 'patient' else 'patient')
                        guardian_force_path = os.path.join(auv_folder, guardian_force_filename)
                        open(guardian_force_path, 'a').close()

                    # 'AUV' 폴더에 최소 1명에서 최대 5명까지의 사람 이미지 추가
                    if num_people_in_folder < max_people_in_folder:
                        # 차 안의 사람 이미지도 최대 5명 이내로 정해줌
                        if 'car' in filename.lower():
                            num_people_in_folder += 1

                        # 선택된 갈림길에 이미지 복사
                        new_img_path = os.path.join(selected_folder, filename)
                        shutil.copy(img_path, new_img_path)
                else:
                    # wall.jpg 파일이 아닌 경우에만 다른 이미지 파일 복사
                    if num_people_in_folder < max_people_in_folder:
                        new_img_path = os.path.join(selected_folder, filename)
                        shutil.copy(img_path, new_img_path)

    # 이미지 분류가 끝난 후에 'wall.jpg' 파일이 폴더에 존재하면 해당 폴더의 다른 이미지 파일 삭제
    for folder in [output_left_folder, output_right_folder]:
        wall_path = os.path.join(folder, 'wall.jpg')
        if os.path.exists(wall_path) and len(os.listdir(folder)) > 1:
            image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg')) and f != 'wall.jpg']
            for image_file in image_files:
                image_path = os.path.join(folder, image_file)
                os.remove(image_path)

print("이미지 분류가 완료되었습니다.")
