import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
		icon = 'icon.png'
		title = 'ST.Python-iOS'
		def build(self):
			print '-------------------'
			print self.get_application_icon()
			print '-------------------'
			return Button(text='Hello World')
			
if __name__ == '__main__' :
	MyApp() .run()