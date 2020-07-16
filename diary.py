import os
import sys
import File
import pygame
import datetime

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
		self.rb_background_music.clicked.connect(self.play_music)
		self.pb_time.clicked.connect(self.add_time)
		self.pb_choose_file.clicked.connect(self.get_file_path)
		#初始化文件路径
		self.diary_file_path=None
		self.music_file=None
		#初始化变量
		self.music_play_num=0
		

	def play_music(self):
		#QMessageBox.information(self, "提示", "该功能尚不可用")
		#如果音乐路径不是空的
		if self.music_file!=None:
			if self.rb_background_music.isChecked()==True:
				if self.music_play_num==0:
					try:
						self.music_play_num=self.music_play_num+1
						pygame.mixer.init()
						track = pygame.mixer.music.load(self.music_file)
						pygame.mixer.music.play()
					except:
						QMessageBox.warning(self,"注意","请重新选择音乐文件")
				else:
					self.music_play_num=self.music_play_num+1
					pygame.mixer.music.unpause()
			else:
				pygame.mixer.music.pause()
		else:
			#获取音乐路径
			self.music_file = QFileDialog.getOpenFileName(caption="选择音乐文件", filter="(*.mp3 *wav)")
			try:
				self.music_play_num=self.music_play_num+1
				pygame.mixer.init()
				self.music_file = self.music_file[0]
				track = pygame.mixer.music.load(self.music_file)
				pygame.mixer.music.play()
			except:
				QMessageBox.warning(self,"注意","请重新选择音乐文件")
				self.music_play_num=self.music_play_num+1
				pygame.mixer.init()
				self.music_file = self.music_file[0]
				track = pygame.mixer.music.load(self.music_file)
				pygame.mixer.music.play()
			

	def add_time(self):
		if self.diary_file_path != None:
			time_str = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
			self.pte_diary.setPlainText(self.pte_diary.toPlainText()+"\n"+"\n"+time_str)
		else:
			QMessageBox.warning(self, "注意", "请先选择日记文件")


	def read_file(self):
		#past_diary=File.Read_Diary(self.diary_file_path[0])
		#print(past_diary,"\n")
		#self.pte_diary.setPlainText(past_diary)
		read_file_content=''
		with open(self.diary_file_path[0],'r') as read_file_content:
			self.pte_diary.setPlainText(read_file_content.read())


	def get_file_path(self):
		self.diary_file_path = QFileDialog.getOpenFileName(caption="选择文件", filter="(*.txt)")
		if self.diary_file_path[0]:
			self.read_file()
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