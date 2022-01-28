import numpy as np
import pandas as pd
import random
from mesa import Model
from agent import Student
from mesa.time import RandomActivation

class Kitchen(Model):
	"""
	The model for the kitchen cleaning PD game
	"""
	def __init__(self, n_agents = 6):
		self.n_agents = n_agents
		self.min_cf = -10
		self.max_cf = 10
		self.cf = 9
		self.deterioration = 1
		self.agentlist = []
		for i in range(n_agents):
			reluctance = np.random.randint(0, 10)
			social_aptitude = np.random.randint(0, 10)
			self.new_agent(i, reluctance, social_aptitude)



	def new_agent(self, roomnumber, reluctance, social_aptitude):
		agent = Student(roomnumber, reluctance, social_aptitude, self.max_cf, self.cf, 0, self.n_agents)
		self.agentlist.append(agent)
		# self.scheduler.add(agent)
		self.n_agents += 1

	def remove_agent(self, agent):
		self.agentlist.remove(agent)
		self.n_agents -= 1

	def step(self):
		
		choices = []
		for player in self.agentlist:
			player.step()
			choices.append(player.choice)

		if 'cooperate' in choices: 
			self.cf = self.max_cf
		else: 
			if self.cf > self.min_cf: 
				self.cf -= self.deterioration

		for player in self.agentlist:
			if player.choice == 'defect': 
				player.sp = 0 # nog aanpassen!
			else: 
				player.sp = 0
			player.update_rewards(self.cf, self.n_agents, player.sp)

	def run_model(self, step_total):
		for i in range(step_total):
			self.step()
			print(self.cf)