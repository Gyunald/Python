def deposit(balance, momey): # 입금
    print(f"입금이 {momey}원 완료되었습니다. 잔액은 {balance+momey}원 입니다.")
    return balance + momey

def withdraw(balance, money): # 출금
    if balance >= money : # 잔액이 출금보다 많으면
        print(f"출금이 {money}원 완료되었습니다. 잔액은 {balance - money}원 입니다.")
        return balance - money
    else :
        print(f"출금이 {money}원 완료되지 않았습니다. 잔액은 {balance}원 입니다.")
        return balance

def withdrw_night(balance, momey): # 저녁 수수료
    commission = 500 # 수수료
    return commission, balance - momey - commission

balance = 0 #잔액
balance = deposit(balance, 5000)
# balance = withdraw(balance, 3000)

commission, balance = withdrw_night(balance, 1000)
print(f"{1000}원 출금이 완료되었습니다. 수수료는 {commission}원 입니다. 잔액은 {balance}원 입니다.")