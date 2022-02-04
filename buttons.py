import os
from time import sleep



class button():

	def __init__(self, name=None):

		self.name = name

		if self.name != None:

			self.path = rf'{os.path.dirname(os.path.realpath(__file__))}\\src\\{self.name}'

			return
		else:
			raise 'button recieves exec file args'


	def run(self):
		os.system(f'start {self.path}')

	def exit(self):
		os.system(f'taskkill /im {self.name}')






