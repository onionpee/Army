import random

def calc_bmi(h, w):         # bmi와 신장에 따른 신체등급 기준표
    bmi = w / (h/100) ** 2
    if h <= 140:
        return "6th"
    elif 141 <= h <= 145:
        return "5th"
    elif 146 <= h <= 158:
        return "4th"
    elif 159 <= h <= 203:
        if bmi < 16:
            return "4th"
        elif 16 <= bmi < 18.5:
            return "3rd"
        elif 18.5 <= bmi < 20:
            return "2nd"
        elif 20 <= bmi < 25:
            return "1st"
        elif 25 <= bmi < 30:
            return "2nd"
        elif 30 <= bmi < 35:
            return "3rd"
        elif bmi >= 35:
            return "4th"
    elif h >= 204:
        return "4th"

fp = open("army.csv", "w", encoding='utf-8')       # army.csv 파일을 인코딩하여 작성함
fp.write("height,weight,rank\n")        # 작성한 csv파일에 문구 입력

cnt = {"1st":0,"2nd":0,"3rd":0,"4th":0,"5th":0,"6th":0}     # 카운트 딕셔너리

for i in range(100000):     # for문을 통한 무작위 표본 산출
    h = random.randint(135, 206)        # random 모듈을 통한 키 및 몸무게 산출
    w = random.randint(45, 110)
    rank = calc_bmi(h, w)       # 산출된 키와 몸무게를 상단에 생성한 함수에 대입
    # print(h, w, rank)           
    cnt[rank] = cnt[rank] + 1   # 리턴 받은 값을 딕셔너리에 1개씩 넣어줌
    fp.write("{0},{1},{2}\n".format(h,w,rank))      # format 값을 읽어온 csv파일에 하나씩 대입함
fp.close()      # 읽어온 csv파일을 닫아줌

print(cnt)