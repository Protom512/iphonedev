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
		# def get_application_config(self):
			# return 'C:\Users\stkd\Documents\GitHub\iphonedev\dev\sample\ch02_07\title.ini'
		def builf_config(self,  config):
			config.setdefaults( 'section_1' , {'key_1':'123',  'key_2':'456'})

		def on_pause(self):

			return True
			
		
			
		def build(self):
			print '-------------------'
			#print self.config.get('section_1')
			print self.get_application_config()
			print self.config.get( 'section_1' , 'key_1' )
			print '-------------------'
			return Button(text=u'Hello Worldソウか' , font_name = 'C:\Users\stkd\Documents\GitHub\iphonedev\dev\sample\ch02_07\\01FLOPDESIGN.ttf')
			
if __name__ == '__main__' :
	PythoniOS() .run()