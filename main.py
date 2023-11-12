import os
from set import classify_images

def get_image_files(folder, extensions):
    if os.path.exists(folder):
        files = [file for file in os.listdir(folder) if file.lower().endswith(extensions)]
        return files
    else:
        return []

def autonomous_vehicle_decision(left_images, right_images, auv_images):
    # 왼쪽, 오른쪽, 차안의 인원 수
    num_left = len(left_images)
    num_right = len(right_images)
    num_auv = len(auv_images)

    # 트롤리 딜레마 결정
    if num_left > num_right and num_left > num_auv:
        decision = "Go to right"
    elif num_left < num_right and num_right > num_auv:
        decision = "Go to left"
    elif num_auv > num_left and num_auv > num_right:
        decision = "Go to the safest route considering passengers in the vehicle"
    else:
        decision = "No specific decision"

    return decision 


# 예시 폴더 경로
input_folder = "../Trolley-dilemma/image"
output_left_folder = "../Trolley-dilemma/left_folder"
output_right_folder = "../Trolley-dilemma/right_folder"
auv_folder = "../Trolley-dilemma/AUV"
classify_images(input_folder, output_left_folder, output_right_folder, auv_folder)

# 이미지 파일 확장자 목록
image_extensions = ('.png', '.jpg', '.jpeg')

# 이미지가 있는지 확인하고 없으면 빈 리스트로 설정
left_images = get_image_files(output_left_folder, image_extensions)
right_images = get_image_files(output_right_folder, image_extensions)
auv_images = get_image_files(auv_folder, image_extensions)

# 자율주행 자동차의 판단
decision = autonomous_vehicle_decision(left_images, right_images, auv_images)

# 결과 출력
print("트롤리 딜레마 시뮬레이션을 시작합니다.")
print(f"\n왼쪽 갈림길에 있는 사람들: {left_images}")
print(f"\n오른쪽 갈림길에 있는 사람들: {right_images}")
print(f"\n차안의 사람들: {auv_images}")
print(f"\n자율주행 자동차의 결정: {decision}")
print("\n트롤리 딜레마 시뮬레이션이 완료되었습니다.")
