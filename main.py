import os
import random
from set import classify_images

def autonomous_vehicle_decision(left_images, right_images, auv_images):
    # 왼쪽, 오른쪽, 차안의 인원 수
    num_left = len(left_images)
    num_right = len(right_images)
    num_auv = len(auv_images)

    # 트롤리 딜레마 결정
    if num_left > num_right:
        decision = "Go to right"
    elif num_left < num_right:
        decision = "Go to left"
    else:
        decision = "No specific decision"

    return decision

# 예시 폴더 경로
input_folder = "../Trolley-dilemma/image"
output_left_folder = "../Trolley-dilemma/left_folder"
output_right_folder = "../Trolley-dilemma/right_folder"
auv_folder = "../Trolley-dilemma/AUV"
classify_images(input_folder, output_left_folder, output_right_folder,auv_folder)

# 이미지가 있는지 확인하고 없으면 빈 리스트로 설정
left_images = os.listdir(output_left_folder) if os.path.exists(output_left_folder) else []
right_images = os.listdir(output_right_folder) if os.path.exists(output_right_folder) else []
auv_images = os.listdir(auv_folder) if os.path.exists(auv_folder) else []

# 자율주행 자동차의 판단
decision = autonomous_vehicle_decision(left_images, right_images, auv_images)

# 결과 출력
print("트롤리 딜레마 시뮬레이션을 시작합니다.")
print(f"\n왼쪽 갈림길에 있는 사람들: {left_images}")
print(f"\n오른쪽 갈림길에 있는 사람들: {right_images}")
print(f"\n차안의 사람들: {auv_images}")
print(f"\n자율주행 자동차의 결정: {decision}")
print("\n트롤리 딜레마 시뮬레이션이 완료되었습니다.")
