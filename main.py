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

    # 이미지 개수를 기준으로 가중치를 계산
    for keyword, weight in keywords_weights.items():
        keyword_count = sum(keyword in image.lower() for image in images)
        keyword_weight = keyword_count * weight / len(images)  # 개수로 나눠서 평균 계산
        total_weight += keyword_weight
        keyword_weights[keyword] = keyword_weight

    # 값들을 소수점 둘째 자리까지 반올림
    total_weight = round(total_weight, 2)
    keyword_weights = {key: round(value, 2) for key, value in keyword_weights.items()}

    return total_weight, keyword_weights

def autonomous_vehicle_decision(left_images, right_images, auv_images):
    # 각 상황의 인원 수
    num_auv = len(auv_images)

    # 키워드 및 가중치 정의
    keywords_weights = {
        'child': 1.3,
        'grand': 0.5,
        'patient': 0.75,
        'doctor': 1.2,
        'animal': 1,
        'police': 1.1,
        'pregnant': 1.35,
        'thief': 0.1
    }

    # 각 상황에 대한 가중치 계산
    weight_left, keyword_weights_left = calculate_weight(left_images, keywords_weights)
    weight_right, keyword_weights_right = calculate_weight(right_images, keywords_weights)
    weight_auv, keyword_weights_auv = calculate_weight(auv_images, keywords_weights)

    # 'wall'이라는 키워드가 포함된 파일이 갈림길에서 발견되면 해당 갈림길의 가중치를 차 안의 가중치로 설정
    # 트롤리 딜레마 결정을 위해 가중치 비교
    if any('wall' in image.lower() and image.lower().endswith('.jpg') for image in left_images) or any('wall' in image.lower() and image.lower().endswith('.jpg') for image in right_images):
    # 'wall.jpg'가 왼쪽 또는 오른쪽 폴더 안에 있는 경우
        if any('wall' in image.lower() and image.lower().endswith('.jpg') for image in left_images):
            weight_left = weight_auv  # 왼쪽 갈림길의 가중치를 벽 쪽 갈림길의 가중치로 설정
        if any('wall' in image.lower() and image.lower().endswith('.jpg') for image in right_images):
            weight_right = weight_auv  # 오른쪽 갈림길의 가중치를 벽 쪽 갈림길의 가중치로 설정

        if weight_auv > weight_right:
            decision = 'Go Right'
        else:
            decision = 'Go Left'
    else:
        # 'wall.jpg'가 없는 경우
        weight_left, keyword_weights_left = calculate_weight(left_images, keywords_weights)  # 왼쪽 갈림길의 가중치 계산
        weight_right, keyword_weights_right = calculate_weight(right_images, keywords_weights)  # 오른쪽 갈림길의 가중치 계산

        if weight_auv > max(weight_left, weight_right):
            if weight_left < weight_right:
                decision = 'Go Left'
            else:
                decision = 'Go Right'
        elif weight_left < weight_right:
            decision = 'Go Left'
        else:
            decision = 'Go Right'

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
