import kivy	
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
#These modules are in python for site request and taking data from the site
import requests
import json

#Fonts used
LabelBase.register(name="Quake",
	fn_regular="Coaster Quake.otf")

LabelBase.register(name="Might",
	fn_regular="Mighty Brush.ttf")

LabelBase.register(name="Lutuna",
	fn_regular="LuTuna.ttf")

LabelBase.register(name="Maxwell",
	fn_regular="Maxwell Leonard.ttf")

#kivy display structure
class Start(BoxLayout):
	def get_started(self):
		user_text=self.ids.my_text
		upd_label=self.ids.my_label
	
		response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+user_text.text+'&appid=963938936256d2c752e95cfd9ec74ac8')

		json_obj = response.json()

		for item in json_obj['weather']:
			upd_label.text=item['main']



class WeatherApp(App):
	def build(self):
		return Start()

if __name__ == "__main__":
	WeatherApp().run()