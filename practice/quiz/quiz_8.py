with open("byme.py","w") as f:
    f.write("""
def sign():        
    print("이 프로그램은 GYUNALD에 의해 만들어 졌습니다."
    "E_mail : GYUNALD.COM"
    "Phone : 123456789")
    """)

import byme
byme.sign()