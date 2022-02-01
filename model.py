import numpy as np
import pandas as pd
import random
from mesa import Model
from agent import Student
from mesa.time import RandomActivation

from agent_types import *

class Kitchen(Model):
	"""
	The model for the kitchen cleaning PD game
	"""
	def __init__(self, cleaning_mode, n_agents = 6, sp_mode = "none"):
		self.n_agents = n_agents
		self.min_cf = -10
		self.max_cf = 10
		self.cf = 0
		self.deterioration = 1
		self.agentlist = []
		self.cleaning_mode = cleaning_mode
		self.sp_mode = sp_mode

		# matrix for awarded rewards
		self.player_rewards = []

		self.matrix = np.zeros((21,self.n_agents))
		self.run_number = 0
		for i in range(n_agents):
			reluctance = np.random.randint(0, 10)
			social_aptitude = np.random.randint(0, 10)
			self.new_agent(i, reluctance, social_aptitude)
		# print(self.n_agents)



	# def new_agent(self, roomnumber, reluctance, social_aptitude):
	# 	agent = Student(roomnumber, reluctance, social_aptitude, self.max_cf, self.cf, 0, self.n_agents)
	# 	self.agentlist.append(agent)
	# 	self.n_agents += 1

	def new_agent(self, roomnumber, reluctance, social_aptitude):
		chance = np.random.uniform()
		# print(chance)
		if(chance < 0.2):
			agent = Slob(roomnumber, reluctance, social_aptitude, self.max_cf, self.cf, 0, self.sp_mode, self.n_agents)
		elif(chance > 0.8):
			agent = NeatFreak(roomnumber, reluctance, social_aptitude, self.max_cf, self.cf, 0, self.sp_mode, self.n_agents)
		else:
			agent = Student(roomnumber, reluctance, social_aptitude, self.max_cf, self.cf, 0, self.sp_mode self.n_agents)
		# print(type(agent))
		self.agentlist.append(agent)
		# self.scheduler.add(agent)

	def remove_agent(self, agent):
		self.agentlist.remove(agent)
		self.n_agents -= 1

	def step(self):
		
		# add row to reward list
		self.player_rewards.append([])

		choices = []
		matrix_loop = 0
		choice_list = []

		for player in self.agentlist:
			player.step()

			choices.append(player.choice)
			if player.choice == 'cooperate':
				choice_list.append(0)
			else :
				choice_list.append(1)

			# print(player.player_status)

			if player.player_status == 0:
			
				self.remove_agent(player)
				self.new_agent(1,1,1)
				self.n_agents += 1
	
		# calculate number of cooperators and proportion of cooperators
		n_cooperators = choices.count('cooperate')
		p_cooperators = n_cooperators/self.n_agents
  
		# calculate social punishment
		if self.social_punishment == "none":
			sp = 0
			predict_sp = 0
		elif self.social_punishment == "mode1":
			if self.n_agents != n_cooperators:
				sp = self.max_cf - (self.max_cf - self.cf) / (self.n_agents - n_cooperators)
			else:
				sp = 0
	

		# make actual reward matrix to grant to agents: 
		if n_cooperators > 0:
			reward_matrix = np.array([[self.max_cf - (self.max_cf - self.cf) / n_cooperators, self.cf],
                             		  [self.max_cf - sp, self.cf]])
		else: 
			reward_matrix = np.array([[0, self.cf],
                             		  [self.max_cf, self.cf]])


		if self.cleaning_mode == 'full': 
			# option 1: kitchen is cleaned fully if one agent cooperates.
			if n_cooperators > 0: 
				self.cf = self.max_cf
			else: 
				if self.cf > self.min_cf: 
					self.cf -= self.deterioration

		if self.cleaning_mode == 'proportional': 
			# option 2: increase in cf is proportional to number of agents that cooperate, namely 
			# the difference between max_cf and the current state times the proportion of cooperators.

			if n_cooperators > 0:
				self.cf += (self.max_cf - self.cf)*p_cooperators
				self.cf = int(self.cf)
			else: 
				if self.cf > self.min_cf: 
					self.cf -= self.deterioration
     
		# update predicted social punishment
		if self.sp_mode == "mode1":
			predict_sp = self.max_cf - self.cf

		# sla rewards op in self.player_rewards
		for player in self.agentlist:
			if player.choice == 'defect': 
				player.sp = 0 # nog aanpassen!
				# Punishment
				if n_cooperators == 0: 
					self.player_rewards[-1].append(reward_matrix[1,1])
				# Temptation
				else: 
					self.player_rewards[-1].append(reward_matrix[1,0])
			
			else:
				player.sp = 0
				# Sucker
				if n_cooperators == 0: 
					self.player_rewards[-1].append(reward_matrix[0,1])
				# Reward
				else: 
					self.player_rewards[-1].append(reward_matrix[0,0]) 

			# update reward matrix of player
			player.update_rewards(self.cf, self.n_agents, predict_sp)
		

		self.matrix = np.delete(self.matrix,0,axis = 0)
		self.matrix = np.insert(self.matrix,20,choice_list, axis = 0)

		if self.run_number == 20:
			 
			person = 0
		
			for element in self.matrix[10]:

				ccp = 1

				if element == 0:
					ccp = 0
				
				new_matrix = self.matrix.copy()
				new_matrix = np.delete(new_matrix,person,1)
	
				total_nr_previous = 0

				for i in range(0,9):
					for j in new_matrix[i:]:
						total_nr_previous += j
				
				total_nr_after = 0

				for i in range(11,20):

					for j in new_matrix[i:]:
						total_nr_after += j

				difference = total_nr_after - total_nr_previous

				current_player = self.agentlist[person]
				current_player.update_rewards(self.cf,self.n_agents,current_player.sp, ccp)

				person += 1

		self.run_number += 1
		print(self.cf)


	def run_model(self, step_total):
		for i in range(step_total):
			self.step()
		self.player_rewards = np.array(self.player_rewards)
		# print(self.player_rewards)
			
	
	