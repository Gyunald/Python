from Crypto.Cipher import AES
from Crypto.Hash import SHA512
import base64
import hashlib
import winreg
import os
import shutil
import sqlite3
import binascii
from Crypto.Util.Padding import pad
import time

# 기본 디바이스 정보 키 만들기 PART1
def get_device_key() :
    DeviceInfo_Path = "Software\Kakao\KakaoTalk\DeviceInfo"
    keypath = winreg.OpenKey(winreg.HKEY_CURRENT_USER, DeviceInfo_Path, 0, winreg.KEY_READ)
    reg_path = winreg.QueryValueEx(keypath, "Last")[0]
    DeviceInfo_Key_Path = DeviceInfo_Path +"\\" + reg_path
    keypath = winreg.OpenKey(winreg.HKEY_CURRENT_USER, DeviceInfo_Key_Path, 0, winreg.KEY_READ)
    hdd_model = winreg.QueryValueEx(keypath, "hdd_model")[0]
    hdd_serial = winreg.QueryValueEx(keypath, "hdd_serial")[0]
    sys_uuid = winreg.QueryValueEx(keypath, "sys_uuid")[0]
    device_key = f"{sys_uuid}|{hdd_model}|{hdd_serial}"
    return device_key.encode('utf-8')

#pragma + userId 합쳐서 데이터베이스 키 값 얻기
def generate_key_iv(pragma, userId):
    key = (pragma + str(userId))
    print(key)
    while len(key) < 512:
        key += key
    key = key[:512]
    key_hash = hashlib.md5(key.encode()).digest()
    iv = hashlib.md5(base64.b64encode(key_hash)).digest()
    return key_hash, iv

# 복호화 하기
def decrypt_database(key, iv, encDB):
    decDB = b""
    i = 0
    print("encDB 길이 값:"+str(len(encDB)))
    while i < len(encDB):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encDB[i:i+4096])
        decDB += decrypted_data
        i += 4096
    return decDB

# 복호화 된 값, DB로 만들기
def save_decrypted_database(decDB, output_file):
    with open(output_file, "wb") as f:
        f.write(decDB)

# 일반적인 전수조사 방안
def find_correct_user_id(encDB, maxUserId, pragma_hash):
    i = 197823700
    while i <= maxUserId:
        # 키 생성
        key = pragma_hash + str(i)
        while len(key) < 512:
            key += key
        key = key[:512]
        key = hashlib.md5(key.encode()).digest()  # MD5 해시 계산
        
        # IV 생성
        iv = hashlib.md5(base64.b64encode(key)).digest()
        
        # 복호화 수행
        decDB = bytearray()
        j = 0
        while j < len(encDB):
            # AES128/CBC/NOPADDING 복호화
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted_data = cipher.decrypt(encDB[j:j + 4096])
            decDB.extend(decrypted_data)
            j += 4096
        
        # 임시 데이터베이스 파일에 저장
        temp_db_path = "temp.db"
        with open(temp_db_path, "wb") as f:
            f.write(decDB)
        
        # SQLite 무결성 검사
        try:
            conn = sqlite3.connect(temp_db_path)
            conn.execute("PRAGMA integrity_check")
            conn.close()  # 연결 닫기
            
            # 연결이 닫힌 후에 파일 삭제
            os.remove(temp_db_path)
            return i  # 무결성 검사 통과 시 user_id 반환
        except sqlite3.DatabaseError:
            # 무결성 검사 실패 시 파일 삭제
            conn.close()
            os.remove(temp_db_path)
        
        i += 1
        # print(i)
    return None  # 유효한 user_id를 찾지 못한 경우

# 헤더 기반 전수조사 방안
def find_user_id(encDB, maxUserId, pragma_hash, normalHeader):
    # encDB에서 헤더 추출
    header = encDB[:16]
    
    # user_id를 찾기 위한 반복
    for i in range(1, maxUserId + 1):
        # 키 생성
        key = pragma_hash + str(i)
        while len(key) < 512:
            key += key
        key = key[:512]
        key = hashlib.md5(key.encode()).digest()  # MD5 해시 계산
        
        # IV 생성
        iv = hashlib.md5(base64.b64encode(key)).digest()
        
        # 헤더 복호화
        cipher = AES.new(key, AES.MODE_CBC, iv)
        result = cipher.decrypt(header)
        
        # 결과가 normalHeader와 일치하는지 확인
        if result == normalHeader:
            return i  # 일치할 경우 user_id 반환
    
    return None  # 일치하는 user_id가 없을 경우 None 반환

def aes_encrypt(data, key, iv, mode=AES.MODE_CBC):
    cipher = AES.new(key, mode, iv)
    # Ensure PKCS#7 padding for AES encryption
    pad_len = 16 - (len(data) % 16)
    data += bytes([pad_len] * pad_len)
    return cipher.encrypt(data)#cipher.encrypt(pad(data, AES.block_size))

#유저 아이디로, 디렉터리 만드는것
def creating_directory_name_userid(user_id, user_dir_home, pragma_hash):
    # Step 1: USERID를 String 값으로 바꾼다.
    user_id_str = str(user_id)
    
    #KAKAOTALK_PC_FOREVER에 해당하는 값을, BYTE 형태로 변환한 후, 해시값 가져옴.
    key = hashlib.md5("KAKAOTALK_PC_FOREVER".encode()).digest()
    iv = hashlib.md5(base64.b64encode(key)).digest()
    # USER_ID 값을 STR 형태로 만든 다음에, KAKAOTALK_PC_FOREVER이란 키와 IV를 이용.
    result = aes_encrypt(user_id_str.encode(), key, iv)
    
    result = os.path.join(user_dir_home, result.hex())
    result = result.encode()

    key = hashlib.md5(pragma_hash.encode()).digest()
    iv = hashlib.md5(base64.b64encode(key)).digest()
    

    result = aes_encrypt(result, key, iv)

    final_hash = hashlib.sha1(result).digest()
    print("User Id 로 만든 디렉토리 이름값:"+final_hash.hex())
    return final_hash.hex()

#생성되어있는 유저 디렉토리로 찾아보자~
#(유저 디렉터리, 디렉터리 위치, UUID로 생성된 프라그마, 최대로 찾을 max_user_id)
def find_correct_user_id_dir(user_dir, user_dir_home, pragma_hash, max_user_id):
    #KAKAOTALK_PC_FOREVER 문자열을 바이트로 변환한 후, MD5 해시를 적용하는 과정
    key1 = hashlib.md5("KAKAOTALK_PC_FOREVER".encode()).digest()
    iv1 = hashlib.md5(base64.b64encode(key1)).digest()

    key2 = hashlib.md5(pragma_hash.encode()).digest()
    iv2 = hashlib.md5(base64.b64encode(key2)).digest()
    
    #16의 배수 만들기.
    prefix = user_dir_home[:len(user_dir_home) // 16 * 16]
    prefix_encrypted = aes_encrypt(prefix.encode(), key2, iv2, padding=False)
    iv2 = prefix_encrypted[-16:]
    
    user_dir_home_trimmed = user_dir_home[len(prefix_encrypted):] + "\\"
    print(user_dir_home_trimmed)

    for i in range(197823000, max_user_id + 1):
        user_id_str = str(i)
        print(f"Checking user_id {user_id_str}...")
        result = aes_encrypt(user_id_str.encode(), key1, iv1)
        result_combined = user_dir_home_trimmed.encode() + result.hex().encode()
        result_encrypted = aes_encrypt(result_combined, key2, iv2)
        final_result = hashlib.sha1(prefix_encrypted + result_encrypted).digest()
        final_result_hex = final_result.hex()
        # Step 18: Check if final_result matches userDirBytes
        if final_result_hex == user_dir:
            print("Matching user ID found:", i)
            return i
    print("No matching user ID found.")
    return None


            
#key, iv, encode된 pragma
def generate_pragma(key,iv, device_key):
    padded_pragma = pad(device_key, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_pragma = cipher.encrypt(padded_pragma)
    #SHA-512 해시 계산
    sha512_hash = SHA512.new()
    sha512_hash.update(encrypted_pragma)
    hashed_pragma = sha512_hash.digest()
    encoded_pragma = base64.b64encode(hashed_pragma)
    return encoded_pragma.decode()

key = bytes.fromhex("9FBAE3118FDE5DEAEB8279D08F1D4C79") 
device_key = get_device_key() 
iv = bytes([0] * 16)
pragma_hash = generate_pragma(key,iv, device_key)
print("pragma_hash 값:"+pragma_hash)

#USER ID 값을 찾기 위해 사용할 FILE_PATH 지정 . 
file_path = r"C:\Users\zetji\AppData\Local\Kakao\KakaoTalk\users\1509b8b6bbefbeec32e43d571931036a6538a007\chat_data\chatLogs_129407183623464.edb"

with open(file_path, "rb") as file:
   encDB = file.read()  # 파일에서 바이트 데이터를 읽어옵니다.

user_dir_home = r"C:\Users\zetji\AppData\Local\Kakao\KakaoTalk\users" 

# # USER ID 탈취 - 사용자 디렉터리 기반 OR 전수공격 
# find_correct_user_id_dir("1509b8b6bbefbeec32e43d571931036a6538a007", r"C:\Users\zetji\AppData\Local\Kakao\KakaoTalk\users", pragma_hash, 200000000)

# print(find_correct_user_id(encDB, 200000000 ,pragma_hash))

user_id = 197823728 # 가져온 아이디 값 넣으면 됩니다.

# # 가져온 아이디가 맞는지, 내가 가지고있는 폴더명 생성하는지 체크 해보기.
# creating_directory_name_userid(user_id, user_dir_home, pragma_hash)

#자 이제, User_id와, Pragma_hash 값이 있으니 PK 키를 만들고, PK로 새로운 데이터베이스 복호화를 위한 KEY, IV를 만들어야 합니다.     
key, iv = generate_key_iv(pragma_hash, user_id)
output_file_name = r"C:\Users\zetji\Documents\KakaoChatLog\test.db" #여러분들이 존재하는 폴더쪽에 DB를 만드셔야 합니다 ..
# file_path = r"C:\Users\zetji\AppData\Local\Kakao\KakaoTalk\users\1509b8b6bbefbeec32e43d571931036a6538a007\chat_data\chatLogs_129407183623464.edb" # me
file_path = r"C:\Users\zetji\AppData\Local\Kakao\KakaoTalk\users\1509b8b6bbefbeec32e43d571931036a6538a007\chat_data\chatLogs_18267121119450986.edb"
with open(file_path, "rb") as file:
    encDB = file.read()  # 파일에서 바이트 데이터를 읽어옵니다.
return_data = decrypt_database(key, iv,encDB)
save_decrypted_database(return_data,output_file_name)


# 데이터베이스 파일 연결
db_path = r'C:\Users\zetji\Documents\KakaoChatLog\test.db'
  # .db 파일 경로
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# 테이블과 키워드 정의
table_name = "chatLogs"  # 검색할 테이블 이름
column_name = "message"  # 검색할 열 이름
keyword = "nickname"  # 검색할 키워드

# SQL 쿼리 실행
query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE ?"
cursor.execute(query, (f"%{keyword}%",))  # LIKE로 키워드 검색

# 결과 가져오기
results1 = cursor.fetchall()

import json
from datetime import datetime
results = []

# 데이터 처리
for record in results1:
    timestamp = record[4]  # 타임스탬프
    json_str = record[5]  # JSON 문자열
    parsed_json = json.loads(json_str)
    
    # 타임스탬프를 날짜로 변환
    formatted_date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d-%H-%M')
    
    # member 또는 members에서 데이터 추출
    if "member" in parsed_json:
        user_info = parsed_json["member"]
        results.append((formatted_date, user_info["userId"], user_info["nickName"]))
    elif "members" in parsed_json:
        for member in parsed_json["members"]:
            results.append((formatted_date, member["userId"], member["nickName"]))

# 결과 출력
for formatted_date, user_id, nick_name in results:
    print(f"Date: {formatted_date}, User ID: {user_id}, Nick Name: {nick_name}")