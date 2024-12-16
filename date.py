import os
import re
# import streamlit as st
from collections import defaultdict

# 입력 파일 폴더 경로 설정
input_folder = r'C:\Users\zetji\Documents\chat_log\pc'
output_folder = r'C:\Users\zetji\Documents\chat_log\date'

# 폴더가 없다면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 날짜별로 내용을 저장할 딕셔너리
date_dict = defaultdict(list)
current_date = None

# 날짜를 기준으로 텍스트 나누기 위한 정규 표현식
date_pattern = r'\d{4}년 \d{1,2}월 \d{1,2}일'

# 입력 폴더 내 모든 .txt 파일 순회
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder, filename)
        
        # 텍스트 파일 읽기
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        date_data = {}
        current_date = None

        for line in lines:
            # 날짜가 포함된 부분을 찾기
            date_match = re.match(date_pattern, line)
            
            if date_match:
                # 날짜가 '2024년 8월 19일' 형태로 저장되도록 처리
                current_date = date_match.group()
                
            if current_date:
                # 날짜별로 해당 내용을 저장
                # 마지막 줄이 다른 날짜의 대화로 이어지지 않도록 처리
                if len(date_dict[current_date]) > 0 and re.match(date_pattern, line):
                    continue
                date_dict[current_date].append(line.strip())

# 날짜별로 텍스트 파일 생성
for date, content in date_dict.items():
    # 파일명에서 날짜를 형식에 맞게 정리 (공백, 한글, 점 제거)
    file_name = os.path.join(output_folder, f"{date.replace('년', '').replace('월', '').replace('일', '').replace(' ', '. ')}.txt")
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

print(f"모든 파일이 저장되었습니다.")
