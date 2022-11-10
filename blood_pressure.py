import time

class Bld_Prssr: # Blood_Pressure 줄여씀.
    def __init__(self, sys, dia, pulse, cur_time):
        self.sys = sys
        self.dia = dia
        self.pulse = pulse
        self.cur_time = cur_time

    def print_info(self):
        print("수축기: ", self.sys)
        print("이완기: ", self.dia)
        print("맥박: ", self.pulse)
        print("입력시간: ", self.cur_time)


def print_menu():  # 메뉴 함수 정의.
    print("1. 혈압 입력")
    print("2. 기록 출력")
    print("3. 기록 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)


def set_bld_prssr():  # 사용자로부터 데이터 입력받는 함수 정의.
    sys = input("수축기: ")
    dia = input("이완기: ")
    pulse = input("맥박: ")
    cur_time = time.ctime() # time 임포트 후 time.ctime() 으로 인스턴스 생성 으로 입력.
    bld_prssr = Bld_Prssr(sys, dia, pulse, cur_time)  # 받은 정보로 인스턴스 생성
    return bld_prssr  # 생성된 인스턴스 반환


def print_bld_prssr(bld_prssr_list):  # bld_prssr 인스턴스를 저장하고 있는 리스트를 인자로 입력받음
    for bld_prssr in bld_prssr_list:
        bld_prssr.print_info()


def delete_bld_prssr(bld_prssr_list, sys):  # 연락처리스트, 삭제할 이름을 인자로 받음.
    for i, bld_prssr in enumerate(bld_prssr_list):
        if bld_prssr.sys == sys:
            del bld_prssr_list[i]


def store_bld_prssr(bld_prssr_list):  # 연락처리스트 입력받아 인스턴스 순회하며 데이터를 파일로 저장.
    f = open("blood_pressure_db.txt", "wt")
    for bld_prssr in bld_prssr_list:
        f.write(bld_prssr.sys + '\n')
        f.write(bld_prssr.dia + '\n')
        f.write(bld_prssr.pulse + '\n')
        f.write(bld_prssr.cur_time + '\n')
    f.close()


def load_bld_prssr(bld_prssr_list):  # 연락처리스트 인자, 파일열어서, 읽어들여 bld_prssr인스턴스생성후 리스트에 추가.
    f = open("blood_pressure_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)  # 윗줄 나눗셈 연산 수행으로 num 값이 실수가 된걸 int 로 형변환.

    for i in range(num):
        sys = lines[4 * i].rstrip('\n')  # i 가 0부터 이므로 4*0,1,2,3// rstrip은 지우기함수
        phone = lines[4 * i + 1].rstrip('\n')
        email = lines[4 * i + 2].rstrip('\n')
        cur_time = lines[4 * i + 3].rstrip('\n')
        bld_prssr = Bld_Prssr(sys, phone, email, cur_time)
        bld_prssr_list.append(bld_prssr)


def run():
    # kim = bld_prssr('김일구', '010-8812-1193', 'ilgu.kim@python.com', 'Seoul')
    # kim.print_info()
    # set_bld_prssr()
    bld_prssr_list = []  # 파일 없을때 오류로 실행불가.
    load_bld_prssr(bld_prssr_list)  # 실행시-연락처리스트 인자, 파일열어서, 읽어들여 bld_prssr인스턴스생성후 리스트에 추가.
    while 1:  # 프로그램 실행 유지, 무한루프
        menu = print_menu()
        if menu == 1:
            bld_prssr = set_bld_prssr()
            bld_prssr_list.append(bld_prssr)
            # print(bld_prssr_list) # 리스트에 어떤 변수? 이름으로 담길지 궁금해서 넣어봄 메인.bld_prssr object at 주소로 출력.
        elif menu == 2:
            print_bld_prssr(bld_prssr_list)  # bld_prssr 인스턴스를 저장하고 있는 리스트를 인자로 입력받음
        elif menu == 3:
            sys = input("수축기: ")
            delete_bld_prssr(bld_prssr_list, sys)  # 연락처리스트, 삭제할 이름을 인자로 받음.
        elif menu == 4:
            store_bld_prssr(bld_prssr_list)  # 연락처리스트 입력받아 인스턴스 순회하며 데이터를 파일로 저장.
            break

# 차트 그릴수 있도록
if __name__ == "__main__":
    run()
