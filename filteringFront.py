import os

# 대상 폴더 설정
target_folder = "F:/datasets/images/train"  # ← 실제 경로로 변경 가능

# 삭제할 확장자 기준 (필요시 수정)
image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

# 유지 조건
def should_keep(filename: str) -> bool:
    base = os.path.splitext(filename)[0]
    return base.endswith("1") or base.endswith("t") or base.endswith("f")

# 정리 시작
for filename in os.listdir(target_folder):
    filepath = os.path.join(target_folder, filename)

    if not os.path.isfile(filepath):
        continue  # 폴더 무시

    _, ext = os.path.splitext(filename)
    if ext.lower() not in image_extensions:
        continue  # 이미지 아닌 파일 무시

    if not should_keep(filename):
        print(f"삭제: {filename}")
        os.remove(filepath)
    else:
        print(f"유지: {filename}")
