# 동네에 항상 대기 손님이 있는 치킨집이 있습니다.
# 대기 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 처리
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리.
# 치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생 시키고 프로그램 종료.
# 출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
class SoldOutError(Exception) :
    def __init__(self):
        print("재고 소진")        

chicken = 10
waiting = 1
while 1 :
    try:
        print(f"[남은 치킨 : {chicken}]")
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order < 1 :
            raise ValueError
        else :
            print(f"대기번호 {waiting} : {order} 마리 주문이 완료되었습니다.")
            chicken -= order
            waiting += 1
        if chicken == 0 :
            raise SoldOutError
        
    except ValueError :
        print("주문을 확인하세요.")
    
    except SoldOutError:
        break