import matplotlib.pyplot as plt


# plt.plot([1, 2, 3, 4]) # y축 기준으로 x축 지정안하면 자동 실수 입력
# plt.show()

x = range(0, 100)
y = [v*v for v in x] # 리스트 내장방법
# y = []
# for v in x:
#     y.append(v*v)

plt.plot(x, y, 'ro') # 세번째 인자로 스타일= 색red, blue / 마커 o서클--대시,s사각,^삼각,+플
plt.show()

# 한 화면에 여러 그래프

fig = plt.figure() # Figure 객체 만든후, add_subplot 추가할 그래프 갯수만큼 만들기
ax1 = fig.add_subplot(2, 1, 1) # 행*열 2*1 subplot생성, 세번째 인자는 첫번째 subplot을 의미
ax2 = fig.add_subplot(2, 1, 2) # 2번째 subplot
plt.show()
