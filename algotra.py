x = 10000
y = 10000

print(id(x), id(y))

mystring = 'hello world'
print(len(mystring))
print(mystring[0:5])
print(mystring[:5])  # 시작값 생략 가능

print(mystring[6:11])
print(mystring[6:])  # 마지막 까지 세기 귀찮을시 마지막 값 생략 가능

# 스플릿
print(mystring.split(' '))  # 공백으로 스플릿 후 리스트[]로 반환
print(mystring.split(' ')[0])  # 뒤에 인덱스값[] 주면 리스트 값에 접근반환

# 머지 합치기
daum = "Daum"
kakao = "KAKAO"
print(daum + ' ' + kakao)  # 계속 합치기 귀찮으니 변수 생성
daum_kakao = daum + ' ' + kakao
print(daum_kakao)

print(type(10))
print(type(3.14))
print(type('python'))
print(type(daum))

# 리스트 []
kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
kospi_top5 = kospi_top10[0:5]  # 슬라이싱
print(kospi_top5)

kospi_top10.append("SK텔레콤")  # 추가 append는 리스트 끝에 추가
print(kospi_top10)

kospi_top10.insert(3, "SK매직")  # insert 위치에 삽입
print(kospi_top10)

print(len(kospi_top10))  # len() 개수 세기 메소드, 내장함수 빌트인

del kospi_top10[-1]  # 삭제 del 뒤에 _빈칸***** 두고 입력
print(len(kospi_top10))

# 튜플 () 원소 변경 불가 /속도 빠르므로 추가,삭제 필요없다면 이용
t = ('Samsung', 'LG', 'SK')
print(len(t))
# print(t(0:2)) 에러, 데이터 접근시 []를 사용해야함 ()쓰면 에러.
print(t[0:2])

# 딕셔너리 {} key, value 쌍저장, 입력순서대로 저장하지 않음.
cur_price = {}
print(type(cur_price))
cur_price["daeshin"] = 30000
print(cur_price)
cur_price['Daum KAKAO'] = 80000
print(cur_price)
print(len(cur_price))

# cur_price[0] 딕셔너리는 인덱싱을 지원하지 않음, append(x) insert(x)
del cur_price['daeshin']  # del 띄어쓰기로 삭제가능.
print(cur_price)

cur_price['daeshin'] = 30000
cur_price['naver'] = 110000
print(cur_price.keys())  # 딕셔너리.keys() 로 키 값만 호출가능.
print(list(cur_price.keys()))  # 리스트 방식으로 키 값을 호출하기. list(딕셔너리.keys())

# 조건문
wikibooks_cur_price = 9000
if wikibooks_cur_price >= 10000:
    print('buy 10')
else:
    print('Holding')

price = 7000
if price < 1000:
    bid = 1  # 호가 가격단위 bid
elif price >= 1000 and price < 5000:
    bid = 5
elif price >= 5000 and price < 10000:
    bid = 10
elif price >= 10000 and price < 50000:
    bid = 50
elif price >= 50000 and price < 100000:
    bid = 100
elif price >= 100000 and price < 500000:
    bid = 500
elif price >= 500000:
    bid = 1000
print(bid)

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
for i in range(0, 11):  # range() 마지막 숫자 11은 포함안됨
    print(i)

interest_stocks = ['Naver', 'Samsung', 'SK Hynix']
for company in interest_stocks:
    print("%s: Buy 10" % company)  # print안에서 문자열위치에 %s 를 쓰고, %기호뒤 변수명으로 지정.
    print(company + ": Buy 10")  # 위와 같은 값이 나오는 다른 방법

# 딕셔너리로 for문 사용법, 2개변수 사용;
interest_stocks2 = {'naver': 10, 'samsung': 5, 'sk hynix': 30}
for company, stock_num in interest_stocks2.items():
    print("%s: Buy %s" % (company, stock_num))  # 두개의 %s 뒤에서 튜플로 표현.
    # print(company +": Buy "+ stock_num) # 왜 구동이 안되고 for문에서 나가지는지;
    # -> item()메서드가 튜플(key,value)를 가져오기 때문에

for company in interest_stocks2.keys():  # .keys() 메서드 활용 방법.
    print("%s: Buy %s" % (company, interest_stocks2[company]))


# 일반적으로 for문은 반복횟수가 미리 정해져 있거나 리스트, 튜플, 딕셔너리와 같은 자료구조와 함께 사용.
# while문은 반복횟수 특정x, 어떤 조건을 충족하는 동안만 실행될때 주로 사용.

# 함수 def

def print_ntimes(n):  # n 함수 파라미터, 함수인자
    for i in range(n):
        print("대신증권")


print_ntimes(2)  # 출력값이 있는 함수 반환값은x


# return 값이 있는 함수.
def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset
    return (upper, lower)


print(cal_upper_lower(10000))

# 모듈, 코드의 재사용을 위해, 이름.py로 사용, import.이름 으로 모듈 임포트, 접근시 모듈명.함수명으로 사용.

import stock

print(stock.author)
print(stock.cal_upper(10000))
print(stock.cal_lower(10000))

# time 모듈 사용

import time

print(time.time())  # 실수형태 반환 1667375624.273856
print(time.ctime()) # Wed Nov  2 16:53:44 2022
# type(_) # _인자는 가장 최근 반환값을 바인딩하는 변수

cur_time = time.ctime()
print(cur_time.split(' ')[-1])

for i in range(0):
    print(i)
    time.sleep(1)  # sleep 초간 멈추기, 1초간격으로 출력.

import random

print(random)  # 모듈 위치 확인
print(dir(time))  # 모듈안에 어떤 함수나 변수가 있는지 확인(구성요소 확인)

# os 모듈

import os

print(os.getcwd())  # 현재 경로 찾기

# 임포트 세가지 방법
# 1) import 방식
# 2) from os import listdir # os모듈로부터 listdir을 임포트하라는 뜻. os.listdir()하면 오류, 직접사용만 가능
# 3) from os import * # 모든것 임포트.
# 첫번째 방식을 추천, os.함수 이런식으로 번거롭지만, 기존 변수나 함수와 충돌가능성 없음.
# 4) import os as winos # os 모듈을 winos로 임포트하라. 기존 모듈명이 길거나 헷갈릴때 바꿔사용하는 방식.

# enumerate 시퀀스자료형(리스트,튜플,문자열) 등을 입력받은후 객체를 반환.
for i, x in enumerate(['naver', 'kakao', 'sk']):
    print(i, x)

i = 0
for x in ['naver', 'kakao', 'sk']:
    print(i, x)
    i += 1

# list 내장함수는 문자열이나 튜플을 입력받은 후 리스트 객체로 만들고, 반환.
print(list('hello'))
print(list((1, 2, 3)))

# sorted 내장함수는 정렬한후 '리스트'***로 반환
# int('3') 문자열을 입력받아 정수형을 변환후 반환, str(3) 객체를 입력받아 문자열로 변환.

# class

name = ["kimyuna", "DusanBack"]
email = ["yunakim@naver.com", "dusan.back@naver.com"]
addr = ["seoul", "Kyunggi"]


def print_business_card(name, email, addr):
    print("--------------------------")
    print("Name: %s" % name)
    print("E-mail: %s" % email)
    print("Office Address: %s" % addr)
    print("--------------------------")


print_business_card(name, email, addr)


# 위의 방식이 절차지향. 객체를 만들어 이름,이멜,주소,함수 모두 포함.
# 클래스를 사용하는 목적이/ 변수와 함수를 묶어서 하나의 새로운 객체로 만드는 것.

class BusinessCard:
    def set_info(self, name, email, addr):  # 클래스 내부 정의된 함수의 첫번째 인자는 반드시 self 걍 외워.
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("--------------------------")
        print("Name: ",self.name)
        print("E-mail: ", self.email)
        print("Office Address: ", self.addr)
        print("--------------------------")


# 인스턴스 / 클래스 정의 = 새로운 데이터 타입 정의 -> 사용하려면 인스턴스 생성.
member1 = BusinessCard()  # 클래스뒤에 ()를 넣어 인스턴스 생성.
member1.set_info("kim", "kim@naver.com", "seoul")
print(member1.name)  # 인스턴스.인스턴스변수 로 접근가능.
print(member1.email)
print(member1.addr)

member2 = BusinessCard()
member2.set_info("lee", "lee@gmail.com", "busan")
member2.print_info()

# 생성자 __init__(self) 메서드.
class MyClass:
    def __init__(self):
        print("객체가 생성되었습니다.")
inst1 = MyClass() # 인스턴스 생성시 - 객체가 생성되었습니다.

class BusinessCard1:
    def __init__(self, name, email, addr):  # 생성자로 바로 입력받기.
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("--------------------------")
        print("Name: ",self.name)
        print("E-mail: ", self.email)
        print("Office Address: ", self.addr)
        print("--------------------------")

member3 = BusinessCard1("Wang", "jh@gmail.com", "Yongin") # 생성시 인자 전달하지 않으면 오류 발생.
member3.print_info()

# self 이해하기.
class Foo:
    def func1():
        print("function 1")

    def func2(self):
        print(id(self))
        print("function 2")

f = Foo()
print(id(f))
f.func2()
# f.func1() 오류
Foo.func1() # 클래스명.메서드() 인스턴스 생성 상관없이 직접 메서드 호출 가능.
Foo.func2(f) # self 위치에 인자를 전달해야 함.

# 네임스페이스 변수(a)가 객체(2)를 바인딩할 때 그 둘 사이의 관계(주소)를 저장하고 있는 공간을 의미.

class Stock:
    market = "kospi"
print(dir())

print(Stock.market)
s1 = Stock()
s2 = Stock()
print(id(s1))
print(id(s2))
print(id(Stock)) # 클래스와 인스턴스의 별도 네임스페이스 유지.
print(s1.market)

# 클래스 변수, 인스턴스 변수, 소멸자 __del__
class Account:
    num_accounts = 0 # 클래스 변수, 클래스 내부에 선언된 변수, 클래스의 네임스페이스 위치
    def __init__(self, name):
        self.name = name # 인스턴스 변수, self가 붙붙있는 변수, 인스턴스의 네임스페이스 위치
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1

kim = Account("kim")
lee = Account("lee")
print(kim.name)
print(kim.num_accounts) # 인스턴스 네임스페이스에서 찾았지만 없어서, 클레스 네임스페이스에서 찾고 반환됨.
print(lee.num_accounts)
# 여러 인스턴스 간에 공유해야 하는 값은 클래스 변수로 바인딩.

# 상속 class Child(Parent)

# 파일 읽기, 쓰기. 구분자 \\ 두개거나 / 사용


f = open('C:\\Users\\jhgre\\IdeaProjects\\codingEnglish\\buy_list.txt', 'rt') # 읽기r 텍스트t
lines = f.readlines() # readlines 메소드 각 라인을 리스트에 넣은 후 리스트를 리턴.
print(lines)
for line in lines:
    print(line, end="") # \n 줄바꿈 없애기 end=""
    nline = line.split('\n')[0]
    print(nline) # 이런식도 가능.

f = open('C:\\Users\\jhgre\\IdeaProjects\\codingEnglish\\sell_list.txt', 'wt') # 쓰기w 텍스트t
f.write('삼성전자\n')
f.write('SK하이닉스\n')
f.close

# contact 디렉토리, 주소록 만들기 프로젝트.
# 프로그램 한 번 실행후 계속 실행 = 무한루프 while 사용 / 종료명령시 break
# 프로그램 종료시 데이터를 파일로 출력, 실행시 파일을 로드.

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}
    def GetCount(self):
        return len(self.stocks)
    def NameToCode(self, name):
        return self.stocks[name]

inst2 = CpStockCode()
print(inst2.GetCount())
print(inst2.NameToCode('유한양행'))

# COM 컴포넌트오브젝트모델 클래스의 객체를 생성하는 방법; Dispatch 사용

# import win32com.client
# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True

# 증권사 API 연결과정에서 중단.

















