import numpy as np
import pandas as pd
import random
from mesa import Agent
from scipy.fftpack import cc_diff
from agent import Student

class NeatFreak(Student):
	"""
	A student which is likely to clean the kitchen
	Estimates rewards of cleaning much higher than rewards of not cleaning
	"""
	def __init__(self, room, reluctance, social_aptitude, max_cf, cf, sp_mode, n_agents):

		self.room = room
		self.reluctance = reluctance
		self.social_aptitude = social_aptitude
		self.cf = cf
		self.max_cf = max_cf
		self.player_status = 5
		self.n_agents = n_agents
		self.choice = 'no_games_played'
		self.difference_list = []
	
  
		if sp_mode == "none":
			sp = 0
		elif sp_mode == "mode1":
			sp = self.max_cf - self.cf

		self.reward_matrix = np.array([[max_cf - (max_cf - cf)/n_agents, cf], [max_cf - sp, cf]])
 
	def update_rewards(self, cf, n_agents, sp, update = 0, ccp = 1, difference = 0):
		
		# print('neat')
		# print(difference)
		

		if ccp == 1:
			
			
			self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents) - update - difference / self.n_agents, cf - update - difference / self.n_agents], [self.max_cf - sp +  difference / 5, cf + difference / self.n_agents]])
		else:
			self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents) - update + difference / self.n_agents, cf - update + difference / self.n_agents ], [self.max_cf - sp - difference / self.n_agents, cf - difference/ self.n_agents]])

	def incentive(self, number_runs):
		incentive = np.sum(self.difference_list) / (number_runs - 20)
		return incentive


	def play(self):
		"An instance of the prisoners dilemma"
		chance = np.random.uniform()
		if chance < 0.3:
			self.choice = 'cooperate'
		else:
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


class Slob(Student):
	"""
	A student which will never clean the kitchen
	risks getting ostracized
	"""
	def __init__(self, room, reluctance, social_aptitude, max_cf, cf, sp_mode, n_agents):
		self.room = room
		self.reluctance = reluctance
		self.social_aptitude = social_aptitude
		self.cf = cf
		self.max_cf = max_cf
		self.player_status = 5
		self.n_agents = n_agents
		self.choice = 'no_games_played'
		self.difference_list = []
  
		if sp_mode == "none":
			sp = 0
		elif sp_mode == "mode1":
			sp = self.max_cf - self.cf
   
		self.reward_matrix = np.array([[max_cf - (max_cf - cf)/n_agents - 4  , cf - 4 ] , [max_cf - sp, cf]])

	def update_rewards(self, cf, n_agents, sp, update = 0, ccp = 1, difference = 0):

		# print('slob')
		# print(difference)
		
		
		

		if ccp == 1:

			self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents - 1 ) - update - difference / self.n_agents , cf - update - difference / self.n_agents - 1] , [self.max_cf - sp +  difference / 5, cf + difference / self.n_agents]])
		else:
			self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents  - 1) - update + difference / self.n_agents , cf - update + difference / self.n_agents - 1], [self.max_cf - sp - difference / self.n_agents, cf - difference/ self.n_agents]])

	def incentive(self, number_runs):
		incentive = np.sum(self.difference_list) / (number_runs - 20)
		return incentive

	def play(self):
		"An instance of the prisoners dilemma"
		# print(self.reward_matrix)
		chance = np.random.uniform()
		if chance < (1/3):
			self.choice = 'defect'
		else:
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

