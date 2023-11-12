import os
import shutil

def delete_all_images(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# 예시 폴더 경로
auv_folder = "../Trolley-dilemma/AUV"
left_folder = "../Trolley-dilemma/left_folder"
right_folder = "../Trolley-dilemma/right_folder"

# 각 폴더에 있는 모든 이미지 삭제
delete_all_images(auv_folder)
delete_all_images(left_folder)
delete_all_images(right_folder)

print("각 폴더의 이미지 삭제가 완료되었습니다.")
