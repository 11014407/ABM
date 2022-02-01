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
		self.player_status = 5
		self.n_agents = n_agents
		self.choice = 'no_games_played'
		self.reward_matrix = np.array([[max_cf - (max_cf - cf)/n_agents, cf], [max_cf - sp, cf]])

	def update_rewards(self, cf, n_agents, sp, difference = 0, ccp = 1):
		if ccp == 1:

			self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents) + difference / 5, cf + difference / 5], [self.max_cf - sp, cf]])

		else :
			self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents), cf ], [self.max_cf - sp +  difference / 5, cf + difference / 5]])


	def play(self):
		"An instance of the prisoners dilemma"

		choice_index = np.argmax(self.reward_matrix)
		if choice_index == 0 or choice_index == 1: 
			self.choice = 'cooperate'
			self.player_status += 1
		else: 
			self.choice = 'defect'
			self.player_status -= 1

	def step(self):
		"A step in the model"
		choice = self.play()
		return choice

