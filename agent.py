import numpy as np
import pandas as pd
import random
from mesa import Agent
from scipy.fftpack import cc_diff

class Agent_type(Agent):
	"""
	A student which has to decide to clean the kitchen or not
	"""
	def __init__(self, room, max_cf, cf, sp_mode, n_agents, id):
		'''
		Initializes an agent with it's initial values and payoff matrix.
		ARGS:
			-room: a unique id representing the student's room number.
			-max_cf: The maximum cleanliness factor of the shared kitchen.
			-cf: The current cleanliness factor of the shared kitchen.
			-sp_mode: with or without social punishment.
			-n_agents: number of agents within the system.
			-id: type of agent(Student/NeatFreak/Slob).
		'''
		self.id = id
		self.room = room
		self.cf = cf
		self.max_cf = max_cf
		self.player_status = 10
		self.n_agents = n_agents
		self.choice = 'no_games_played'
		self.difference_list = []
	
		if sp_mode == "none":
			sp = 0
		elif sp_mode == "mode1":
			sp = self.max_cf - self.cf
   
		self.reward_matrix = np.array([[max_cf - (max_cf - cf)/n_agents, cf], [max_cf - sp, cf]])

	def update_rewards(self, cf, n_agents, sp, update = 0, ccp = 1, difference = 0):

		''' 
		Different types of students have different types of reward matrices
		ARGS:
			-cf: current state of the kitchen.
			-n_agents: number of agents .
			-sp: social punishment.
			-update: Learning method based on backwards learning.
			-ccp: 1 in case player cooperates in middle row of matrix and 0 if defect.
			-difference: Learning method based on backwards learning.
		'''
		if self.id == 'Student' or self.id == 'NeatFreak':
		
			if ccp == 1:
				
				self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents) - update + difference / self.n_agents, cf - update + difference / self.n_agents], [self.max_cf - sp -  difference / self.n_agents, cf - difference / self.n_agents]])
			else:
				self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents) - update - difference / self.n_agents, cf - update - difference / self.n_agents ], [self.max_cf - sp + difference / self.n_agents, cf + difference/ self.n_agents]])

		else:
			if ccp == 1:
				self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents - 1 ) - update + difference / self.n_agents , cf - update + difference / self.n_agents - 1] , [self.max_cf - sp -  difference / self.n_agents, cf - difference / self.n_agents]])
			else:
				self.reward_matrix = np.array([[(self.max_cf - (self.max_cf - cf)/n_agents  - 1) - update - difference / self.n_agents , cf - update - difference / self.n_agents - 1], [self.max_cf - sp + difference / self.n_agents, cf + difference/ self.n_agents]])

		
	def incentive(self, number_runs):
		incentive = np.sum(self.difference_list) / (number_runs - 20)
		return incentive

	def play(self):
		'''play function checks what the best option is for every player.
			Additionally a random factor for neatfreaks and slobs has been 
			to automatically cooperate or defect.
		'''
		#"An instance of the prisoners dilemma"

		
		choice_index = np.argmax(self.reward_matrix)

		if self.id == 'NeatFreak':
			if random.random() < 0.33:
				choice_index = 1

		if self.id == 'Slob':
			if random.random() < 0.33:
				choice_index = 2
		
		if choice_index == 0 or choice_index == 1: 
			self.choice = 'cooperate'
			self.player_status = 5 
		else: 
			self.choice = 'defect'
			self.player_status -= 1

	def step(self):
		'''A step in the model'''
		choice = self.play()
		return choice

