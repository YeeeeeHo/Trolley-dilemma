import os
from set import classify_images

def get_image_files(folder, extensions):
    if os.path.exists(folder):
        files = [file for file in os.listdir(folder) if file.lower().endswith(extensions)]
        return files
    else:
        return []

def calculate_weight(images, keywords_weights):
    # 키워드 및 가중치를 기반으로 총 가중치 계산
    total_weight = 0
    keyword_weights = {}  # 추가: 각 키워드별 가중치 저장
    for keyword, weight in keywords_weights.items():
        keyword_count = sum(keyword in image.lower() for image in images)
        total_weight += keyword_count * weight
        keyword_weights[keyword] = keyword_count * weight
    return total_weight, keyword_weights

def autonomous_vehicle_decision(left_images, right_images, auv_images):
    # 각 상황의 인원 수
    num_left = len(left_images)
    num_right = len(right_images)
    num_auv = len(auv_images)

    # 키워드 및 가중치 정의
    keywords_weights = {
        'child': 1.2,
        'grand': 0.5,
        'patient': 0.75,
        'doctor': 1.2,
        'animal': 1,
        'police': 1.1,
        'pregnant': 1.3,
        'thief': 0.1
    }

    # 각 상황에 대한 가중치 계산
    weight_left, keyword_weights_left = calculate_weight(left_images, keywords_weights)
    weight_right, keyword_weights_right = calculate_weight(right_images, keywords_weights)
    weight_auv, keyword_weights_auv = calculate_weight(auv_images, keywords_weights)
    weight_wall = num_auv + calculate_weight(auv_images, keywords_weights)[0]

    # 트롤리 딜레마 결정을 위해 가중치 비교
    if 'wall' in left_images or 'wall' in right_images:
        if weight_wall > weight_auv:
            decision = '벽 쪽으로 이동'
        else:
            decision = '자율주행 자동차 쪽으로 이동'
    else:
        if weight_auv > max(weight_left, weight_right):
            if weight_left < weight_right:
                decision = '왼쪽으로 이동'
            else:
                decision = '오른쪽으로 이동'
        elif weight_left < weight_right:
            decision = '왼쪽으로 이동'
        else:
            decision = '오른쪽으로 이동'

    return decision, weight_left, weight_right, weight_auv, keyword_weights_left, keyword_weights_right, keyword_weights_auv

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
decision, weight_left, weight_right, weight_auv, _, _, _ = autonomous_vehicle_decision(left_images, right_images, auv_images)

# 각 폴더의 총 가중치 계산
total_weight_left = weight_left
total_weight_right = weight_right
total_weight_auv = weight_auv

# 결과 출력
print("트롤리 딜레마 시뮬레이션을 시작합니다.")
print(f"\n왼쪽 갈림길에 있는 사람들: {left_images}")
print(f"\n오른쪽 갈림길에 있는 사람들: {right_images}")
print(f"\n차안의 사람들: {auv_images}")
print(f"\n자율주행 자동차의 결정: {decision}")
print(f"\n가중치 결과:")
print(f"   - 왼쪽 갈림길 총 가중치: {total_weight_left}")
print(f"   - 오른쪽 갈림길 총 가중치: {total_weight_right}")
print(f"   - 차안 총 가중치: {total_weight_auv}")
print("\n트롤리 딜레마 시뮬레이션이 완료되었습니다.")
