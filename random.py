from random import *
import random
a = randrange(4,29)
b = randint(4,28)
c = random.sample(range(1,29),2)
print(f"오프라인 스터디 모임 날짜는 매월 {a}일로 선정되었습니다.")
print(f"오프라인 스터디 모임 날짜는 매월 {b}일로 선정되었습니다.")
print(f"오프라인 스터디 모임 날짜는 매월 {sorted(c)}일로 선정되었습니다.")