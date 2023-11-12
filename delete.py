import os
import shutil

def delete_images_with_extensions(folder, extensions):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) and filename.lower().endswith(extensions):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# 예시 폴더 경로
auv_folder = "../Trolley-dilemma/AUV"
left_folder = "../Trolley-dilemma/left_folder"
right_folder = "../Trolley-dilemma/right_folder"

# 삭제할 파일 확장자 목록
allowed_extensions = ('.png', '.jpg', '.jpeg')

# 각 폴더에 있는 특정 확장자의 이미지 삭제
delete_images_with_extensions(auv_folder, allowed_extensions)
delete_images_with_extensions(left_folder, allowed_extensions)
delete_images_with_extensions(right_folder, allowed_extensions)

print("각 폴더의 이미지 삭제가 완료되었습니다.")
