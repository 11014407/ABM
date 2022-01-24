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
	def __init__(self, players = 6, environment)
		self.scheduler = RandomActivation(self)
		self.environment = 0
		for i in range(players):
			reluctance = np.randomint(0, 10)
			social_aptitude = np.randomint(0, 10)
			self.new_agent(i, reluctance, social_aptitude)
		self.players = i


	def new_agent(self, roomnumber, reluctance, social_aptitude):
		agent = Student(roomnumber, reluctance, social_aptitude)
		self.scheduler.add(agent)
		self.players += 1

	def remove_agent(self, agent):
		self.scheduler.remove(agent)
		self.players -= 1

	def step(self):
		for i in range(self.players):
			agents = self.scheduler._agents
			agent_keys = list(agents.keys())
			for key in agent_keys:
				if key in agents:
					agents[key].step()
	
	def run_model(self, step_total):
		for i in range(step_total):
			self.step()