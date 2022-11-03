
from pandas import Series, DataFrame

# import pandas
# print(pandas.Series) # 임포트 방식에 따라 앞에 pandas. 을 붙일지 여부 달라짐.


# Series 자료구조.

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao) # 인덱스와 밸류값 동시 저장., 리스트와 달리 인덱싱 값을 지정할 수 있음.
print(kakao[0])

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['2022-11-01',
                                                            '2022-11-02',
                                                            '2022-11-03',
                                                            '2022-11-04',
                                                            '2022-11-05'])

print(kakao2)
print(kakao2['2022-11-05'])

for date in kakao2.index: # 인덱스 값(index) 출력 코드.
    print(date)

for ending_price in kakao2.values: # 저장된 종가 값(value) 출력코드
    print(ending_price)

# 여러 나눠서 취합하게 되는 경우.

mine = Series([10,20,30], index=['naver','sk','kt'])
friend = Series([10,30,20], index=['kt','naver','sk'])

merge = mine + friend
print(merge)

# 판다스는 IDLE이나 주피터콘솔이 바로바로 값을 확인할수 있어 더 적합함. IDE(통합개발환경) 보다/

# DataFrame 자료구조 여러개의 칼럼으로 구성된 2차원 형태의 자료구조(엑셀)

# 파이썬의 딕셔너리를 사용하는 방법.
raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

# col0,1,2 세개의 칼럼. 각 칼럼을 인덱싱 하는데 사용됩니다., 로우 방향으로는 시리즈와 유사하게 자동으로 0,1,2,3,4인덱싱
data = DataFrame(raw_data)
print(data)
daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'close': [11900, 11600, 11000, 11100, 11050]}


daeshin_day = DataFrame(daeshin)
print(daeshin_day)

daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close']) # 칼럼의 순서 변경가능
print(daeshin_day)

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date) # 인덱스 변경
print(daeshin_day)

# 종가에만 접근, 하나의 칼럼에만 접근
close = daeshin_day['close']
print(close)

# 하나의 로우 데이터만(날짜) 가져오는 경우
# print(daeshin_day['16.02.29']) # 키값이 없으므로 에러 발생
# loc 메서드를 사용 인덱스 값을 넘겨주면 됩니다.

day_data = daeshin_day.loc['16.02.29']
print(day_data) # 시리즈로 출력
print(type(day_data))

# 칼럼 이름과 인덱스 값을 확인
print(daeshin_day.columns)
print(daeshin_day.index)


# 데이터리더로 주식 데이터 가져오기(야후)
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2022, 10, 1) # 01 날짜 안됨. 1로/
end = datetime.datetime(2022, 11, 1)

gs = web.DataReader("078930.KS", "yahoo", start, end) # 데이터프레임으로,
#                    인자:종목정보, 소스(야후), 시작, 종료

# 주식 차트 그려보기
gs = web.DataReader("078930.KS", "yahoo") # 전체데이터
gs.info()

# matplotlib 의 pyplot 모듈로 그래프 그리기
import matplotlib.pyplot as plt

plt.plot(gs['Adj Close']) # y축 수정종가, x축 날짜(정수인덱스x업댓됫나봄)
plt.plot(gs.index, gs['Adj Close']) # x축 인덱스(로우), y축 수정종가(칼럼)
plt.show() # 표시

# 이동평균선 구하기
gs = web.DataReader("078930.KS", "yahoo", "2019-01-01", "2022-11-01") # 01 날짜 됨 datatime과 달리;

gs.tail() # 잘 받아졌는지 뒤5개 데이터 확인

# 5일 이평 (수정종가)
ma5 = gs['Adj Close'].rolling(window=5).mean()

ma5.tail(10) # 객체 타입 시리즈.

new_gs = gs[gs['Volume'] != 0] # 거래량 0 false 아닌날 true/ 거래량 0인날(공휴일) 모두 제거한 새로운 객체 생성.

ma5 = new_gs['Adj Close'].rolling(window=5).mean()
ma5.tail(10)

# 5이평값을 기존 객체에 새로운 칼럼으로 추가 insert / 첫인자 위치, 이름, 데이터
new_gs.insert(len(new_gs.columns), "MA5", ma5)
#               인자 위치(맨뒤)      칼럼이름, 데이터

ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()
# rolling mean 함수 인자로 20,60,120 전달하면 이평 다양하게 가능.

new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")

plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")
# 범례표시 legend,loc , 격자표시 grid
plt.legend(loc='best')
plt.grid()
plt.show()

















