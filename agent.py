import numpy as np
import pandas as pd
import random
from mesa import Agent
from scipy.fftpack import cc_diff

class Student(Agent):
	"""
	A student which has to decide to clean the kitchen or not
	"""
	def __init__(self, room, reluctance, social_aptitude, max_cf, cf, sp, n_agents):
		self.room = room
		self.reluctance = reluctance
		self.social_aptitude = social_aptitude
		self.cf = cf
		self.max_cf = max_cf
		self.sp = sp
		self.n_agents = n_agents
		self.choice = 'no_games_played'
		self.reward_matrix = np.array([[max_cf - (max_cf - cf)/n_agents, cf], [max_cf - sp, cf]])

	def update_rewards(self, cf, n_agents, sp):
		self.reward_matrix = np.array([[self.max_cf - (self.max_cf - cf)/n_agents, cf], [self.max_cf - sp, cf]])


	def play(self):
		"An instance of the prisoners dilemma"

		choice_index = np.argmax(self.reward_matrix)
		# # print(choice_index)
		# matrix = np.array([[1, 1], [1, 1]])
		# print(np.argmax(matrix))
		if choice_index == 0 or choice_index == 1: 
			self.choice = 'cooperate'
		else: 
			self.choice = 'defect'

	def step(self):
		"A step in the model"
		choice = self.play()
		return choice

