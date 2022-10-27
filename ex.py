'''
# 3-1 리스트 만들기
naver_closing_price = [474500, 461500, 501000, 500500, 488500]
print(naver_closing_price)

# 3-2,3 최고가, 최저가 찾기
print(max(naver_closing_price))
print(min(naver_closing_price))

# 3-4 최고가 최저가 가격차 표시
max_price = max(naver_closing_price)
min_price = min(naver_closing_price)
differ_price = max_price - min_price
print(differ_price)

# 3-5 수요일 종가 출력
print(naver_closing_price[2])

# 3-6 날짜를 딕셔너리 key로, 종가를 value로
naver_closing_price2 = {}
naver_closing_price2['09/07'] = naver_closing_price[0]
naver_closing_price2['09/08'] = naver_closing_price[1]
naver_closing_price2['09/09'] = naver_closing_price[2]
naver_closing_price2['09/10'] = naver_closing_price[3]
naver_closing_price2['09/11'] = naver_closing_price[4]
print(naver_closing_price2)

# 3-7 09/09의 종가를 출력
print(naver_closing_price2['09/09'])
# ''''''또는 """""" 블록주석은 들여쓰기(줄맞춤)을 해야 에러가 안뜸.

# 4-1 ***** 출력 작성
# print('*', end='') # 줄바꿈없이 화면출력 가능.

for i in range(5):
    print('*', end='')
print('')

# 4-2 별패턴 출력 '중첩루프'활용
for i in range(4):
    for j in range(5):
        print('*', end='')
    print('')


# 4-3 별패턴 출력

for i in range(5):
    print('*' * (i + 1))

# 4-4 별패턴 출력

for i in range(5):
    print('*'*(5-i))

# 4-5 별패턴
for i in range(5):
    print(" "*(4-i)+"*"*(i+1))
# 4-6 별패턴
for i in range(5):
    print(" "*(i)+"*"*(5-i))
# 4-7 별패턴
for i in range(5):
    print(" "*(4-i)+"*"*((i+1)*2-1))
# 4-8 별패턴
for i in range(5):
    print(" "*(i)+"*"*(11-(i+1)*2))
# 4-9 신문배달(중첩루프 이용)
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for i in apart:
    for y in i:
        if y not in arrears: # 이부분에서 틀렸었음 not in 사용 또는 in 쓰고 continue로 넘긴후 else: 시 프린트.
            print(y)
#       if y in arrears:
#             continue
#         else:
#             print(y)

'''

# 5-1 평균 구하는 함수
def myaverage(a, b):
    averg = (a + b) / 2
    return averg
print(myaverage(2,4))

# 5-2 리스트를 인자로 받은 후, 최대값 최소값 반환.
def get_max_min(data_list):
    max_value = max(data_list)
    min_value = min(data_list)
    return max_value, min_value
listda = [5,3,2]
print(get_max_min([1]))

# 5-3 절대 경로를 입력받은 후, txt파일 목록을 리스트로 반환.
import os

def get_txt_list(path):
    for x in os.listdir(path):
        if x.endswith('txt'): # 문자열이 txt로 끝나는 경우 반
            return x

dir_a1 = os.getcwd()
































