# coding:utf-8

import os
os.environ['KIVY_NO_FILELOG'] = ''
import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.button import Button

class PythoniOS(App):
		icon = 'icon.png'
		title = 'ST.Python-iOS'

		def on_start(self):
			print '-------------------'
			print 'on_start'
			print '-------------------'
		def on_stop(self):
			print '-------------------'
			print 'on_stop'
			print '-------------------'
		def on_pause(self):
			print '-------------------'
			print 'pause'
			print '-------------------'
			return True
		def on_resume(self):
			print '-------------------'
			print 'resume'
			print '-------------------'
		def build(self):
			print '-------------------'
			print self.get_application_config()
			print self.directory
			print self.name
			print self.get_application_icon()
			print '-------------------'
			return Button(text=u'Hello Worldソウか' , font_name = 'C:\Users\stkd\Documents\GitHub\iphonedev\dev\sample\ch02_07\\01FLOPDESIGN.ttf')
			
if __name__ == '__main__' :
	PythoniOS() .run()