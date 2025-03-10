import os

def get_folder_size(folder_path):
    """
    특정 폴더의 크기를 계산하고 폴더 내 파일 목록을 출력합니다.

    Args:
        folder_path: 크기를 확인할 폴더의 경로

    Returns:
        폴더 크기 (바이트) 또는 폴더가 존재하지 않으면 0
    """

    total_size = 0
    file_list = []  # 파일 목록을 저장할 리스트

    try:
        # 폴더 내 모든 파일과 하위 폴더를 순회
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # os.path.islink() 함수를 사용하여 심볼릭 링크는 크기에 포함하지 않도록 함
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
                    file_list.append(fp)  # 파일 목록에 파일 경로 추가

    except FileNotFoundError:
        print(f"폴더를 찾을 수 없습니다: {folder_path}")
        return 0

    # 파일 목록 출력
    print("폴더 내 파일 목록:")
    for file in file_list:
        print(file)

    return total_size

# 예시:
folder_path = "C:\\Users\\SBA\\Desktop\\cat"  # 확인하려는 폴더 경로로 변경 (주의: 백슬래시는 이중으로 입력해야 합니다)
folder_size_bytes = get_folder_size(folder_path)

if folder_size_bytes > 0:
    # 바이트 크기를 KB, MB, GB 단위로 변환 (선택 사항)
    folder_size_kb = folder_size_bytes / 1024
    folder_size_mb = folder_size_kb / 1024
    folder_size_gb = folder_size_mb / 1024

    print(f"폴더 크기: {folder_size_bytes} 바이트")
    print(f"폴더 크기: {folder_size_kb:.2f} KB")
    print(f"폴더 크기: {folder_size_mb:.2f} MB")
    print(f"폴더 크기: {folder_size_gb:.2f} GB")