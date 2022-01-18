with open("/Users/kyu-deokkim/Documents/Git/practice/byme.py", "w", encoding="utf-8") as f:
    f.writelines("""def sign():\n\tprint("이 프로그램은 'GYUNALD'에 의해 만들어졌습니다.")""")
f.close()

import byme
byme.sign()