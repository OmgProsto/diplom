from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtGui
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage

import sys, os, time, threading, random
import matplotlib.pyplot as plt

from config import getConfig
from mainwindow import Ui_MainWindow as mw
from secondwindow import Ui_Dialog as sw
from autowindow import Ui_Dialog as aw
from testwindow import Ui_Dialog as tw
from statwindow import Ui_Dialog as stw
from selecttestwindow import Ui_Dialog as stestw
from videowindow import Ui_Dialog as vw
from counterwindow import Ui_Dialog as cw
from selectcountwindow import Ui_Dialog as scw
from diagrammwindow import Ui_Dialog as dw
from adminpwdwindow import Ui_Dialog as apw
from adminpanelwindow import Ui_Dialog as apnw

from readFile import text_full, welcomeFile
from autoUser import users, que_user, upd_res, check, sbrosFile
from readQue import lst_que, createQue, removeQue, countQue

surname = ''
group = ''

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
	
		self.SecondWin, self.AutoWin, self.VideoWin, self.CountWin = '', '', '', ''

		self.mwui = mw()
		self.mwui.setupUi(self)
		self.mwui.pushButton.clicked.connect(self.click)
		self.mwui.pushButton_2.clicked.connect(self.test)
		self.mwui.pushButton_3.clicked.connect(self.exit)
		self.mwui.pushButton_4.clicked.connect(self.about)
		self.mwui.pushButton_6.clicked.connect(self.video)
		self.mwui.pushButton_7.clicked.connect(self.count)
		self.mwui.pushButton_8.clicked.connect(self.admin)

		self.achive = que_user(surname, group);
		resultTest = round(self.achive[1] / countQue(1) * 100)
		colorResult = 'red' if resultTest < 40 else 'green'

		self.achiveSec = que_user(surname, group, 2);
		resultTestSec = round(self.achiveSec[1] / countQue(2) * 100)
		colorResultSec = 'red' if resultTestSec < 40 else 'green'

		colorResultPractice = "<span style='color: green'> выполнено </span>"

		self.mwui.label_2.setText(f'Студент: <strong>{surname}</strong>')
		self.mwui.label_3.setText(f'Группа: <strong>{group}</strong>')
		self.mwui.label_4.setText(f"""Процент выполнения 1 теста: <span style="color: {colorResult}">{resultTest}%</span> / Оставшиеся попытки: {self.achive[0]}""")
		self.mwui.label_5.setText(f"""Процент выполнения 2 теста: <span style="color: {colorResultSec}">{resultTestSec}%</span> / Оставшиеся попытки: {self.achiveSec[0]}""")
		self.mwui.label_7.setText(f"""Практическое задание: {colorResultPractice} """)
		self.mwui.label_6.setText("""<div style="text-align: right">
										<div>
											Программа разработана студентом 881гр. УрТИСИ СибГУТИ<br>Зеленковым Савелием Игоревичем для кафедры ИСТ<br>
									 	</div><br>
									 	<img src='img/icon/main.jpg'>
									 </div>""")

	def about(self):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setText('Для выполнения заданий, необходимо для начала ознакомиться с теорией, доступной в меню "Теория"\n Для прохождения теста перейдите в раздел "Тест"\n Для выполнения практического задания перейдите в "Практическое задание"\n Для просмотра видеоматериала перейдите в "Видеоматериалы" ')
		msgBox.exec()

	def admin(self):
		self.AdminAuthWin = AdminAuthWin()
		self.AdminAuthWin.show()

	def test(self):
		self.SelectTestWin = SelectTestWin()
		self.SelectTestWin.setFixedSize(300,200)
		self.SelectTestWin.show()

	def click(self):
		self.SecondWin = SecondWin()
		self.SecondWin.setFixedSize(1200,600)
		self.SecondWin.show()

	def video(self):
		self.VideoWin = VideoWin()
		self.VideoWin.setFixedSize(500,300)
		self.VideoWin.show()

	def count(self):
		self.SelectCountWin = SelectCountWin()
		self.SelectCountWin.setFixedSize(400,300)
		self.SelectCountWin.show()


	def exit(self):
		app.quit()


class SelectTestWin(QtWidgets.QWidget):
	def __init__(self):
		super(SelectTestWin, self).__init__()

		self.stestwui = stestw()
		self.stestwui.setupUi(self)

		self.stestwui.pushButton.clicked.connect(self.test1)
		self.stestwui.pushButton_2.clicked.connect(self.test2)

	def test1(self):
		global surname
		global group
		new_user = que_user(surname, group)

		if new_user[0] == 0:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText(f"Вы больше не можете пройти этот тест. Ваш последний результат {new_user[1]}/{countQue(1)}")
			msgBox.exec()
		else:
			msgBox = QtWidgets.QMessageBox()
			res = msgBox.question(self, 'PyQt5 message', f'У вас осталось попыток {new_user[0]}, хотите пройти тест еще раз? Ваш последний результат {new_user[1]}/{countQue(1)}', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
			
			if res == QtWidgets.QMessageBox.Yes:
				users(surname, group)
				self.TestWin = TestWin()
				self.TestWin.setFixedSize(800,600)
				self.TestWin.show()


	def test2(self):
		global surname
		global group
		new_user = que_user(surname, group, 2)

		if new_user[0] == 0:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText(f"Вы больше не можете пройти этот тест. Ваш последний результат {new_user[1]}/{countQue(2)}")
			msgBox.exec()
		else:
			msgBox = QtWidgets.QMessageBox()
			res = msgBox.question(self, 'PyQt5 message', f'У вас осталось попыток {new_user[0]}, хотите пройти тест еще раз? Ваш последний результат {new_user[1]}/{countQue(2)}', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
			
			if res == QtWidgets.QMessageBox.Yes:
				users(surname, group, 2)
				self.TestWin = TestWin(2)
				self.TestWin.setFixedSize(800,600)
				self.TestWin.show()


class AdminAuthWin(QtWidgets.QWidget):
	def __init__(self):
		super(AdminAuthWin, self).__init__()

		self.apw = apw()
		self.apw.setupUi(self)

		self.apw.pushButton.clicked.connect(self.auth)

	def auth(self):
		password = self.apw.lineEdit.text()

		if (password == getConfig('pwdAdmin')):
			self.AdminPanelWin = AdminPanelWin()
			self.AdminPanelWin.setFixedSize(800,600)
			self.AdminPanelWin.show()
			self.hide()
		else:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText("Пароль не верный!")
			msgBox.exec()


class AdminPanelWin(QtWidgets.QWidget):
	def __init__(self):
		super(AdminPanelWin, self).__init__()

		self.apnw = apnw()
		self.apnw.setupUi(self)

		self.apnw.pushButton.clicked.connect(self.create)
		self.apnw.pushButton_2.clicked.connect(self.remove)
		self.apnw.pushButton_3.clicked.connect(self.exit)
		self.apnw.pushButton_4.clicked.connect(self.stat)

	def create(self):
		createQue(
			1, 
			self.apnw.lineEdit.text(), 
			self.apnw.lineEdit_2.text(),
			self.apnw.lineEdit_3.text(),
			self.apnw.lineEdit_4.text(),
			self.apnw.lineEdit_5.text()
			)

		self.apnw.lineEdit.setText('') 
		self.apnw.lineEdit_2.setText('') 
		self.apnw.lineEdit_3.setText('') 
		self.apnw.lineEdit_4.setText('') 
		self.apnw.lineEdit_5.setText('')

		msgBox = QtWidgets.QMessageBox()
		msgBox.setText("Вопрос добавлен")
		msgBox.exec()

	def remove(self):
		removeQue(1)

		msgBox = QtWidgets.QMessageBox()
		msgBox.setText("Последний вопрос удален")
		msgBox.exec()

	def exit(self):
		self.hide()

	def stat(self):
		self.StatWin = StatWin()
		self.StatWin.show()


class SelectCountWin(QtWidgets.QWidget):
	def __init__(self):
		super(SelectCountWin, self).__init__()

		self.scwui = scw()
		self.scwui.setupUi(self)

		self.scwui.pushButton.clicked.connect(self.count)
		self.scwui.pushButton_2.clicked.connect(self.falstadOpen)
		self.scwui.label.setText(f"Практическое задание состоит из:")


	def count(self):
		self.CountWin = CountWin()
		self.CountWin.setFixedSize(1000,800)
		self.CountWin.show()

	def falstadOpen(self):
		self.FalstadWin = FalstadWin()
		self.FalstadWin.setFixedSize(800,600)
		self.FalstadWin.show()




class FalstadWin(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.questions = [
			['1 впорос', 'ansCount1'],
			['2 вопрос', 'ansCount2']
			]

		self.true = random.randint(0, 1)
		print(self.true)
		self.initUI()
		

	def initUI(self):
		web = QWebEngineView()

		web.load(QtCore.QUrl(getConfig('falstadUrl')))
		def processHTML(html):
		    print(1)
		html = web.page().toHtml(processHTML)

		self.btn = QtWidgets.QPushButton('Выход', self)
		self.btn.resize(self.btn.sizeHint())
		self.btn.clicked.connect(self.exit)

		self.label = QtWidgets.QLabel(self.questions[self.true][0], self) # Пишешь задание вместо 123
		self.edit = QtWidgets.QLineEdit(self)
		self.btnAns = QtWidgets.QPushButton('Ответить', self)

		self.btnAns.clicked.connect(self.answer)

		lay = QtWidgets.QVBoxLayout(self)
		lay.addWidget(self.btn)
		lay.addWidget(web)
		lay.addWidget(self.label)
		lay.addWidget(self.edit)
		lay.addWidget(self.btnAns)


	def answer(self):
		if (self.edit.text() == getConfig(self.questions[self.true][1])):
			self.btnAns.setEnabled(False)
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText("Верно")
			msgBox.exec()
		else:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText("Не верно")
			msgBox.exec()
		
	def exit(self):
		self.hide()
		
		


class CountWin(QtWidgets.QWidget):

	puzzle = [
				{'x': 0, 'y': 50, 'check': False},
				{'x': 170, 'y': 50, 'check': False},
				{'x': 360, 'y': 50, 'check': False},
				{'x': 550, 'y': 50, 'check': False},
				{'x': 680, 'y': 50, 'check': False},
			]

	trueOrder = {
		1: ['label', 'label_2', 'label_3', 'label_4', 'label_6'],
	}

	def __init__(self):
		super(CountWin, self).__init__()

		self.flagBut = {}

		self.cwui = cw()
		self.cwui.setupUi(self)

		for i in self.puzzle:
			i['check'] = False

		self.mission = random.randint(1,1)#,3)
		
		

		self.cwui.pushButton.clicked.connect(lambda: self.jump(self.cwui.label))
		self.cwui.pushButton_2.clicked.connect(lambda: self.jump(self.cwui.label_2))
		self.cwui.pushButton_3.clicked.connect(lambda: self.jump(self.cwui.label_3))
		self.cwui.pushButton_4.clicked.connect(lambda: self.jump(self.cwui.label_4))
		self.cwui.pushButton_6.clicked.connect(lambda: self.jump(self.cwui.label_6))
		self.cwui.pushButton_5.clicked.connect(self.exit)

		if self.mission == 1:
			self.cwui.label.setText("<img src='img/count/первый.png'>")
			self.cwui.label_2.setText("<img src='img/count/пытый.png'>")
			self.cwui.label_3.setText("<img src='img/count/четвертый.png'>")
			self.cwui.label_4.setText("<img src='img/count/второй.png'>")
			self.cwui.label_6.setText("<img src='img/count/третий.png'>")
			self.cwui.label_5.setText("Составить суммирующий счётчик на d-триггерах с модулем счета 9")

		#elif self.mission == 2:
		#	self.cwui.label.setText("<img src='img/count/первый.png'>")
		#	self.cwui.label_2.setText("<img src='img/count/пытый.png'>")
		#	self.cwui.label_3.setText("<img src='img/count/четвертый.png'>")
		#	self.cwui.label_4.setText("<img src='img/count/второй.png'>")
		#	self.cwui.label_6.setText("<img src='img/count/третий.png'>")
		#	self.cwui.label_5.setText("Составить суммирующий счётчик на d-триггерах с модулем счета 9<br><hr>")
		#	
		#else: 	
		#	self.cwui.label.setText("<img src='img/count/первый.png'>")
		#	self.cwui.label_2.setText("<img src='img/count/пытый.png'>")
		#	self.cwui.label_3.setText("<img src='img/count/четвертый.png'>")
		#	self.cwui.label_4.setText("<img src='img/count/второй.png'>")
		#	self.cwui.label_6.setText("<img src='img/count/третий.png'>")
		#	self.cwui.label_5.setText("Составить суммирующий счётчик на d-триггерах с модулем счета 9<br><hr>")
			
			

	def jump(self, label):

		if label.objectName() in list(self.flagBut):
			print(label.pos().x())
			print(label.pos().y())
			for i in self.puzzle:
				if (i['x'] == label.pos().x() and i['y'] == label.pos().y()):
					i['check'] = False
					break
			label.setGeometry(QtCore.QRect(self.flagBut[label.objectName()][0], self.flagBut[label.objectName()][1], label.size().width(), label.size().height()))
			del(self.flagBut[label.objectName()])
			print(label.pos().x())
			print(label.pos().y())
		else:
			print(label.pos().x())
			print(label.pos().y())
			self.flagBut[label.objectName()] = [label.pos().x(), label.pos().y()]
			for i in self.puzzle:
				if (i['check'] == False):
					label.setGeometry(QtCore.QRect(i['x'], i['y'], label.size().width(), label.size().height()))
					i['check'] = True
					break
			print(label.pos().x())
			print(label.pos().y())

		for i in self.puzzle:
			if i['check'] == False:
				return

		if list(self.flagBut) == self.trueOrder[self.mission]:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText("Верно")
			msgBox.exec()
			self.cwui.pushButton.setEnabled(False)
			self.cwui.pushButton_2.setEnabled(False)
			self.cwui.pushButton_3.setEnabled(False)
			self.cwui.pushButton_4.setEnabled(False)
			self.cwui.pushButton_6.setEnabled(False)
		else:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText("Не верно")
			msgBox.exec()



	def exit(self):
		self.flagBut.clear()
		self.hide()


class VideoWin(QtWidgets.QWidget):
	def __init__(self):
		super(VideoWin, self).__init__()

		self.vwui = vw()
		self.vwui.setupUi(self)
		#self.vwui.label_1.setText("Суммирующий счетчик<br>")
		#self.vwui.label_2.setText("Вычитающий счетчик<br>")
		#self.vwui.label_3.setText("Реверсивный счетчик<br>")
		#self.vwui.label_4.setText("Составление счетчиков<br>")

		self.vwui.pushButton_1.clicked.connect(self.playVideo)

		self.videoPlay = QVideoWidget()
		self.videoPlay.resize(300, 300)
		self.videoPlay.move(0, 0)

		self.player = QMediaPlayer()
		self.player.setVideoOutput(self.videoPlay)
		self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("video/счетчики.mp4")))
		self.player.setVolume(25)

		# self.vwui.pushButton_2.clicked.connect(self.playVideo)

		# self.videoPlay = QVideoWidget()
		# self.videoPlay.resize(300, 300)
		# self.videoPlay.move(0, 0)

		# self.player = QMediaPlayer()
		# self.player.setVideoOutput(self.videoPlay)
		# self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("video/тригеры.mp4")))
		# self.player.setVolume(25)

		# self.vwui.pushButton_3.clicked.connect(self.playVideo)

		# self.videoPlay = QVideoWidget()
		# self.videoPlay.resize(300, 300)
		# self.videoPlay.move(0, 0)

		# self.player = QMediaPlayer()
		# self.player.setVideoOutput(self.videoPlay)
		# self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("video/тригеры2.mp4")))
		# self.player.setVolume(25)

		# self.vwui.pushButton_4.clicked.connect(self.playVideo)

		# self.videoPlay = QVideoWidget()
		# self.videoPlay.resize(300, 300)
		# self.videoPlay.move(0, 0)

		# self.player = QMediaPlayer()
		# self.player.setVideoOutput(self.videoPlay)
		# self.player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("video/счетчики.mp4")))
		# self.player.setVolume(25)

	def playVideo(self):
		self.player.setPosition(0)
		self.videoPlay.show()
		self.player.play()


class SecondWin(QtWidgets.QWidget):
	def __init__(self):
		super(SecondWin, self).__init__()

		self.text = []
		self.tek = 0
		self.swui = sw()
		self.swui.setupUi(self)

		self.swui.pushButton.clicked.connect(self.click_but_next)
		self.swui.pushButton_2.clicked.connect(self.click_but_back)

		self.swui.pushButton_3.clicked.connect(lambda: self.tab(self.swui.pushButton_3.objectName()))
		self.swui.pushButton_4.clicked.connect(lambda: self.tab(self.swui.pushButton_4.objectName()))
		self.swui.pushButton_5.clicked.connect(lambda: self.tab(self.swui.pushButton_5.objectName()))
		self.swui.pushButton_6.clicked.connect(lambda: self.tab(self.swui.pushButton_6.objectName()))

		self.swui.pushButton_2.setEnabled(False)
		self.swui.pushButton.setEnabled(False)

		self.swui.label.setText('<h1> Теория </h1> <p> Выберите нужный раздел из меню слева</p>')
		self.swui.label_2.setText(f"<strong>{self.tek+1} страница</strong>")

	def tab(self, btnName):
		self.swui.pushButton.setEnabled(True)
		nameFile =  btnName + '-teor.txt'
		self.text = text_full(nameFile);
		self.swui.label.setText(self.text[0])
		self.tek = 0
		self.swui.label_2.setText(f"<strong>{self.tek+1} страница</strong>")

	def click_but_next(self):
		if self.tek + 1 == 1:
			self.swui.pushButton_2.setEnabled(True)

		self.swui.label.setText(self.text[self.tek + 1])
		self.tek += 1
		self.swui.label_2.setText(f"<strong>{self.tek+1} страница</strong>")

		if self.tek + 1 == len(self.text):
			self.swui.pushButton.setEnabled(False)


	def click_but_back(self):
		if self.tek + 1 == len(self.text):
			self.swui.pushButton.setEnabled(True)

		self.swui.label.setText(self.text[self.tek - 1])
		self.tek -= 1
		self.swui.label_2.setText(f"<strong>{self.tek+1} страница</strong>")

		if self.tek + 1 == 1:
			self.swui.pushButton_2.setEnabled(False)


class AutoWin(QtWidgets.QWidget):
	def __init__(self):
		super(AutoWin, self).__init__()

		self.awui = aw()
		self.awui.setupUi(self)

		self.awui.pushButton.clicked.connect(self.auto)


	def auto(self):
		global surname
		global group

		if (self.awui.lineEdit.text() == '' or self.awui.lineEdit_2.text() == ''):
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText("Перепроверьте введеные данные")
			msgBox.exec()
		elif (any(map(str.isdigit, self.awui.lineEdit.text()))):
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText("Фамилия не должна состоять из цифр")
			msgBox.exec()
		else:
			surname = self.awui.lineEdit.text()
			group = self.awui.lineEdit_2.text()
			self.MainWindow = MainWindow()
			self.MainWindow.setFixedSize(800,600)
			self.MainWindow.show()
			self.hide()


class TestWin(QtWidgets.QWidget):
	def __init__(self, test = 1):
		super(TestWin, self).__init__()
		self.test = test
		self.questions = lst_que(self.test)

		random.shuffle(self.questions);
		self.tekque = 0
		self.tektime = time.time()
		self.alltime = 1

		self.lst_ans = []
		self.twui = tw()
		self.twui.setupUi(self)

		self.t = threading.Thread(name='worker', target=self.worker)
		self.t.start()


		self.twui.pushButton.clicked.connect(self.finish_que)
		self.twui.pushButton_2.clicked.connect(self.send_que)

		self.update()


	def update(self):

		self.twui.label.setText(f"Вопрос {self.tekque + 1}")

		self.twui.label_2.setText(str(self.questions[self.tekque][0]))
		self.twui.pushButton_2.setEnabled(True)
		self.twui.radioButton.setText(str(self.questions[self.tekque][1]))
		self.twui.radioButton_2.setText(str(self.questions[self.tekque][2]))
		self.twui.radioButton_3.setText(str(self.questions[self.tekque][3]))


	def send_que(self):
		if self.twui.radioButton.isChecked():
			self.lst_ans.append(1)
		elif self.twui.radioButton_2.isChecked():
			self.lst_ans.append(2)
		elif self.twui.radioButton_3.isChecked():
			self.lst_ans.append(3)
		else:
			self.lst_ans.append(0)
	
		self.tekque += 1
		self.update()

		if len(self.questions) == self.tekque + 1:
			self.twui.pushButton_2.setEnabled(False)

	def finish_que(self, x = 0):
		global surname
		global group
		self.tekque = -1
		if self.twui.radioButton.isChecked():
			self.lst_ans.append(1)
		elif self.twui.radioButton_2.isChecked():
			self.lst_ans.append(2)
		elif self.twui.radioButton_3.isChecked():
			self.lst_ans.append(3)
		else:
			self.lst_ans.append(0)


		for i in range(len(self.lst_ans)):
			if self.lst_ans[i] == self.questions[i][4]:
				self.lst_ans[i] = 1
			else:
				self.lst_ans[i] = 0
		self.hide()

		upd_res(surname, group, sum(self.lst_ans), self.test)
		if x == 0:
			msgBox = QtWidgets.QMessageBox()
			msgBox.setText(f"Ваш результат {sum(self.lst_ans)}/7")
			msgBox.exec()

		self.lst_ans.clear()


	def worker(self):
		while True:
			if self.alltime == 0:
				break
			if self.tekque == -1:
				break
			self.alltime = x = 50 - int(time.time() - self.tektime)
			if x % 60 < 10:
				self.twui.label_3.setText(str(int(x / 60)) + ':' + f'0{x % 60}')
			else:
				self.twui.label_3.setText(str(int(x / 60)) + ':' + str(x % 60))
		if self.alltime == 0:
			self.finish_que(x = 1)

	def closeEvent(self, event):
		self.finish_que()


class StatWin(QtWidgets.QWidget):
	def __init__(self):
		super(StatWin, self).__init__()
		self.stwui = stw()
		self.stwui.setupUi(self)
		self.lst = check()

		self.stwui.tableWidget.setColumnCount(4)
		self.stwui.tableWidget.setRowCount(len(self.lst))

		self.stwui.pushButton.clicked.connect(self.sbros)

		for i in range(len(self.lst)):
			for j in range(len(self.lst[i])):
				self.stwui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.lst[i][j])))


	def sbros(self):
		for i in range(len(self.lst)):
			for j in range(len(self.lst[i])):
				self.stwui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(''))
		sbrosFile()


if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	app.setStyleSheet("""
		QWidget { font-family: Comic Sans MS, cursive, sans-serif; background-color: #C8C2BC; color: black; font-size: 15px }
		QPushButton { background-color: #C8C2BC; border-radius: 8px; border: 2px solid black  }
		QLineEdit { border: 2px solid black  }
		QPushButton:hover { background: #CC9B6D; font-size: 18px; }

		QPushButton#main_pushButton_4 { border-radius: 0px; }
		QPushButton#main_pushButton_5 { border-radius: 0px; }
		QPushButton#main_pushButton_3 {  background-color: solid black;
    									
    									 border-width: 2px;
   										 border-color: beige; }
		   

		QLabel#main_label_2 { border-style: solid; border-width: 1px; border-color: black; }
		QLabel#main_label_3 { border-style: solid; border-width: 1px; border-color: black; }
		QLabel#main_label_4 { border-style: solid; border-width: 1px; border-color: black; }
		QLabel#main_label_5 { border-style: solid; border-width: 1px; border-color: black; }
		QLabel#count_label { border-style: solid; border-width: 1px; border-color: black; }
		""");
	app.setWindowIcon(QtGui.QIcon('img/icon/icon.jpg'))
	win = AutoWin()
	win.setFixedSize(300,200)
	win.show()
	sys.exit(app.exec())