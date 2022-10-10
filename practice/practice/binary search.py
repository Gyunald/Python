numbers = [ 52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print(f" - {52} 는 {numbers.index(52)} 위치에 있습니다.")
print()

try:
    number = 10000
    print("# (2) 요소 내부에 없는 값 찾기")
    print(f"- {number} 는 {numbers.index(number)} 위치에 있습니다.")
except: 
    print("- 리스트 내부에 없는 값 입니다")
    print()
finally:
    print("정상적으로 죵료되었습니다.")