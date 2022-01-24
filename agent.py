import numpy as np
import pandas as pd
import random
from mesa import Agent

class Student(Agent):
	"""
	A student which has to decide to clean the kitchen or not
	"""
	def __init__(self, room, reluctance, social_aptitude):
		self.room = room
		self.reluctance = reluctance
		self.social_aptitude = social_aptitude.


	def play(self):
		"An instance of the prissoners dillema"
		#if(x en y):
		#	defect
		#else:
		#	cooperate



	def step(self):
		"A step in the model"
		self.play(
