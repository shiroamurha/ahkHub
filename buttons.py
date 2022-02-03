import os
from time import sleep



class button1():

	def __init__(self, arg=None):

		self.arg = arg

		if self.arg == None:

			self.name = 'textbox.exe'
			self.path = rf'{os.path.dirname(os.path.realpath(__file__))}\\src\\{self.name}'

			return
		else:
			raise 'tome'


	def run(self):
		os.system(f'start {self.path}')

	def exit(self):
		os.system(f'taskkill /im {self.name}')




