import re
from datetime import datetime
import os

input_folder = r'C:\Users\zetji\Documents\chat_log\mobile'
output_folder = r'C:\Users\zetji\Documents\chat_log\pc'  # 결과 파일 경로

def convert_time_format(original_time):
    # 시간 "오전/오후" 형식으로 변환
    parts = original_time.split()
    meridiem = parts[-2]
    time = parts[-1]
    return f"{meridiem} {time}"

def clean_nickname(nickname):
    # 닉네임의 공백 문제 처리
    return nickname.strip()

def clean_message(message):
    # 본문 내 중복된 공백 제거
    return re.sub(r'\s{2,}', ' ', message).strip()

def convert_file(input_path, output_folder, filename):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    saved_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"GTX 님과 카카오톡 대화\n저장한 날짜 : {saved_date}\n\n"
    result_lines = [header]

    current_message = ""
    for line in lines[5:]:
        # # 날짜 헤더 처리 (예: "2022년 2월 27일")
        # date_match = re.match(r"^\d{4}년 \d{1,2}월 \d{1,2}일", line)
        # if date_match:
        #     # 날짜 줄바꿈 추가
        #     result_lines.append(f"\n{line.strip()}\n\n")
        #     continue

        # 일반 대화 처리
        match = re.match(r"(\d{4}\. \d{1,2}\. \d{1,2}\. (오전|오후) \d{1,2}:\d{2}), (.*?): (.*)", line)
        if match:
            # 이전 메시지 저장
            if current_message:
                result_lines.append(current_message.strip() + "\n")
                current_message = ""

            # 새로운 메시지 추가
            date_time, meridiem, sender, message = match.groups()
            converted_time = f"{meridiem} {date_time.split()[-1]}"
            cleaned_sender = clean_nickname(sender)
            cleaned_message = clean_message(message)
            current_message = f"[{cleaned_sender}] [{converted_time}] {cleaned_message}"
        else:
            # 현재 메시지에 추가 (다중 줄 처리)
            current_message += f" {line.strip()}"

    # 마지막 메시지 저장
    if current_message:
        result_lines.append(current_message + "\n")

    # 출력 파일 경로 생성
    output_path = os.path.join(output_folder, filename)

    # 폴더 생성 (필요시)
    os.makedirs(output_folder, exist_ok=True)

    # 결과 파일 쓰기
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(result_lines)

# 입력 폴더 내 모든 .txt 파일 순회
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file = os.path.join(input_folder, filename)
        convert_file(input_file, output_folder, filename)

print(f"파일이 변환되었습니다.")