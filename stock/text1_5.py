naver_mon_start = int(input("가격입력 >>>"))
naver_mon_end = naver_mon_start * 0.7
naver_tue_strat = naver_mon_end
naver_tue_end = naver_tue_strat * 0.7
naver_wed_start = naver_tue_end
naver_wed_end = naver_wed_start * 0.7
print(int(naver_wed_end))