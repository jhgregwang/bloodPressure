import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# def 리소스_패스
# form = 리소스_패스('main.ui')
# form_class = uic.loadUiType(form)[0] # 파일 경로 불러오는 방식

form_class = uic.loadUiType("main_window.ui")[0] # ui파일을 로드해서 만든 클래스.
# [0]은 Ui)MainWindow클래스, [1]은 PyQt5.QtWidgets.QMainWindow

class MyWindow(QMainWindow, form_class): # 2클래스로부터 다중 상속받은 클래스
    def __init__(self):
        super().__init__() # 부모클래스의 초기값을 호출.
        self.setupUi(self) # Qt Designer를 통해 구성한 UI를 사용가능.

        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self, "message", "clicked")


if __name__ == "__main__": # 이 파일을 여기서 실행할 경우.
    app = QApplication(sys.argv) # sys.argv 실행할 때 입력된 값을 읽는 메서드, 여기서는 작업중인 py파일의 절대경로.
    # = QApplication 객체가 실행할 파일이 현재 파이썬 코드라는 것을 의미.
    myWindow = MyWindow() # 인스턴스생성.
    myWindow.show() # 화면에 출력
    app.exec_() # app의 무한루프, 종료되는 경우 0을 반환하여 종료.

