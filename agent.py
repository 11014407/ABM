import numpy as np
import pandas as pd
import random
from mesa import Agent

class Student(Agent):
	"""
	A student which has to decide to clean the kitchen or not
	"""
	def __init__(self, room, reluctence_value, social_aptitude):
		self.room = room
		self.reluctence_value = reluctence_value
		self.social_aptitude = social_aptitude.


	def play(self):
		"An instance of the prissoners dillema"




	def step(self):
		"A step in the model"
		self.play()
