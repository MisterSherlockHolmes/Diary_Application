import os
import sys
import File

from PySide2.QtWidgets import*
from PySide2.QtGui import *
from ui_diary import Ui_Diary
from PySide2.QtCore import *

class MyDiaries(QMainWindow, Ui_Diary):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		#绑定信息与槽函数
		self.pb_finish.clicked.connect(self.get_content_and_write)
		self.rb_background_music.clicked.connect(self.message_music)
		self.pb_time.clicked.connect(self.message_time)
		self.pb_choose_file.clicked.connect(self.get_file_path)
		#初始化文件路径
		self.diary_file_path=None
		

	def message_music(self):
		QMessageBox.information(self, "提示", "该功能尚不可用")

	def message_time(self):
		QMessageBox.information(self, "提示", "该功能尚不可用")

	def read_file(self):
		self.pte_diary.setPlainText(File.Read_Diary(self.diary_file_path[0]))


	def get_file_path(self):
		self.diary_file_path = QFileDialog.getOpenFileName(caption="选择文件", filter="(*.txt)")
		if self.diary_file_path[0]:
			#self.read_file()
			pass
		else:
			QMessageBox.warning(self, "注意", "请重新选择日记文件")


	def get_content_and_write(self):
		diary_content=self.pte_diary.toPlainText()
		if self.diary_file_path != None:
			self.diary_file_path=self.diary_file_path[0]
			File.Save_Diary(diary_content, self.diary_file_path)
			QMessageBox.information(self, "提示", "日记已添加")
		else:
			QMessageBox.warning(self, "注意", "请先选择日记文件")
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyDiaries()
	sys.exit(app.exec_())