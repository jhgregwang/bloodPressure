import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, QDesktopWidget, \
    QGridLayout, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt

# form_class = uic.loadUiType("main_window.ui")[0] //designer에서 불러오는 코드

class MyApp(QMainWindow):
            #, form_class):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate() #현재날짜 얻기
        self.initUI()
        # self.setupUi(self) //desiger에서 가져올때 쓰는 메소드.

    def initUI(self):

        # grid = QGridLayout()
        # self.setLayout(grid)
        #
        # grid.addWidget(QLabel('제목:'), 0, 0)
        # grid.addWidget(QLabel('저자:'), 1, 0)
        # grid.addWidget(QLabel('리뷰:'), 2, 0)
        #
        # grid.addWidget(QLineEdit(), 0, 1)
        # grid.addWidget(QLineEdit(), 1, 1)
        # grid.addWidget(QTextEdit(), 2, 1)


        exitAction = QAction(QIcon('exit.png'), '나가기', self) #아이콘, 나가기, 라벨 갖는 액션 만들기
        exitAction.setShortcut('Ctrl+Q') # 단축키 설정
        exitAction.setStatusTip('나가기 앱')
        exitAction.triggered.connect(qApp.quit) #액션이 시그널 보냄 qApp에 quit메서드

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate)) #현재날짜 표시/

        menubar = self.menuBar() #메뉴바 생성
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File') #파일 메뉴만들고, &앰퍼샌드는 간편하게 단축키설정.Alt+F
        filemenu.addAction(exitAction) #파일메뉴에 액션추가 exitAction

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')


        btn = QPushButton('나가기', self)  # 버튼에 표시될 텍스트, 버튼이 위치할 부모위젯
        btn.setToolTip('이것은 QPushButton 위젯 입니다.')
        btn.move(150, 150)
        btn.resize(btn.sizeHint()) #버튼을 적절한 크기로 설정.
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        # self.setGeometry(1000, 500, 300, 200)  # x, y 위치, 너비, 높이
        self.resize(500, 350)
        self.center() # center() 메서드를 통해 창을 가운데로 위치.
        self.show()

    def center(self):
        qr = self.frameGeometry() #메서드를 이용해서 창의 위치와 크기정보 가져옴.
        cp = QDesktopWidget().availableGeometry().center() #사용하는 모니터의 가운데 위치를 파악
        qr.moveCenter(cp) #창의 qr(직사각형) 위치를 화면의 중심위치로 이동
        self.move(qr.topLeft()) #현재창을 qr의 위치로 이동



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
