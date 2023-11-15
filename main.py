import os
from set import classify_images

def get_image_files(folder, extensions):
    if os.path.exists(folder):
        files = [file for file in os.listdir(folder) if file.lower().endswith(extensions)]
        return files
    else:
        return []

def calculate_weight(images, keyword):
    # 특정 키워드가 포함된 이미지 수
    count = sum(keyword in image.lower() for image in images)
    return count

def autonomous_vehicle_decision(left_images, right_images, auv_images):
    # 왼쪽, 오른쪽, 차안의 인원 수
    num_left = len(left_images)
    num_right = len(right_images)
    num_auv = len(auv_images)

    # 각 상황에 대한 가중치 설정
    weight_child = 0.5
    weight_grand = 0.2
    weight_patient = 0.3

    # 각 상황에 대한 가중치 계산
    weight_left = -(num_left + weight_child * calculate_weight(left_images, 'child') + weight_grand * calculate_weight(left_images, 'grand') + weight_patient * calculate_weight(left_images, 'patient'))
    weight_right = -(num_right + weight_child * calculate_weight(right_images, 'child') + weight_grand * calculate_weight(right_images, 'grand') + weight_patient * calculate_weight(right_images, 'patient'))
    weight_auv = -(num_auv + weight_child * calculate_weight(auv_images, 'child') + weight_grand * calculate_weight(auv_images, 'grand') + weight_patient * calculate_weight(auv_images, 'patient'))

    # 길 위의 사람과 차 안의 사람을 비교하여 트롤리 딜레마 결정
    if weight_auv > max(weight_left, weight_right):
        decision = 'Go to the safest route considering passengers in the vehicle'
    elif weight_left > weight_right:
        decision = 'Go to left'
    else:
        decision = 'Go to right'

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
