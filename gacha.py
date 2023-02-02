import random
import sqlite3

# 포인트 가져오기
with sqlite3.connect("point.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS point(
    name text NOT NULL,
    point integer,
    ticket integer,
    day integer)
""")

# 이름 물어보고 소문자or 대문자로 바꾸기.
newName = "Wang"


while (True):
    cursor.execute("SELECT * FROM point WHERE name=?", [newName])
    # for i in cursor.fetchall():
    #     prePoint += i[1]
    list_db = cursor.fetchall()
    if list_db == []:
        cursor.execute("""INSERT INTO point(name,point,ticket,day)
        VALUES(?,?,?,?)""", (newName, 0, 0, 20230128))
        db.commit()
    else:
        break
prePoint = list_db[-1][1]
preTicket = list_db[-1][2]
lastDay = list_db[-1][3]

# print(prePoint)
# cursor.execute("SELECT * FROM point WHERE name=?",[newName])
# print(cursor.fetchall()[-1][1])
# cursor.execute("SELECT * FROM point WHERE name=?",[newName])
# list = cursor.fetchall()
# print(list)
# print(len(list))

print("Your point is {}.".format(prePoint))

# 최대 티켓 까지만 돌릴수 있도록 하기, 돌리면 횟수만큼 티켓장수 줄이기.
print("You have {} tickets.".format(preTicket))
# 확률을 가진 방법으로 랜덤뽑기. 가중치 입력받고, 확률로 변환// 확률을 입력받고
reward01 = 10
reward02 = 5
reward03 = 1
while True:
    run_num = int(input("Enter a number of turns(Max:{}): ".format(preTicket)))
    if run_num == 0:
        break
    elif run_num > preTicket or run_num < 0:
        print("wrong number. try again")
        continue

    preTicket -= run_num
    list = []

    for i in range(run_num):
        a = random.random()
        # print(a)
        if a < 0.1:
            b = reward01
        elif a < 0.3:
            b = reward02
        else:
            b = reward03
        list.append(b)
        prePoint += b
    print(*list, sep=' ', )
    print("Your point is", prePoint)
    cursor.execute("""INSERT INTO point(name,point,ticket,day)
        VALUES(?,?,?,?)""", (newName, prePoint,preTicket,lastDay))
    db.commit()

# sql 변경사항 저장

# newPoint = str(newPoint)

# 메인메소드. 1)가챠하기, 2) 기록보기, 3) 포인트상점, 4) 뽑기권추가.
def main():
    print("""1) Gacha!
2) Record.
3) Pocha!(point bar)
4) Add Ticket.
""")
    menu = int(input("Select menu:(1~4)"))
    if menu == 1:
        # 가챠 구동 함수

        pass
    elif menu == 2:
        # 기록내역 함수

        pass
    elif menu == 3:
        # 포인트상점, 포장마차, 푸드트럭, 선술집, 주점. 타치노미, 드링크바, 노미호다이, 야타이
        # 술도 팔고, 식권 충전 및 팔기, 그리고 포장마차 요리 판매.

        pass
    elif menu == 4:
        # 티켓 추가하는 방법들, 1장씩 버튼 추가, 일일퀘스트 미션추가,(로그)

        pass
    else:
        print("wrong number!")

    db.close()


main()

# 가중치를 입력해서, 그 안의 값으로 나올수 있는 것을 생각/
# 뭔가를 다 더해서 1이 나올수 있도록 만들어두고, == 다 더해서 total 값으로 나누면 0~1의 값이 나오므로.


# 뽑기권이 몇장 있는지 쓰고, 턴 돌릴때마다 뽑기권 감소,

# 뽑기권 사용하는 상점 만들기. 선술집ㅋㅋ
# 포인트상점. 리스트 존재하고, 구매확인, 총구매내역 영수증 개념, 선술집 키오스크 같은 분위기.

# 나중에 exe로 실행가능한 파일로 만들기.(ui추가)