import kivy
kivy.requires('1.7.2')

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
		def build(self):
			return Button(text='Hello World!')
			
if _name_ == '_main_' :
	MyApp() .run()