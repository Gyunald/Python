class ThailandPackage:
    def detail(self):
        print("타일랜드 패키지 50만원")

if __name__ == "__main__" :
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()

else :
    print("Thailand 외부에서 모듈 호출")