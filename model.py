from re import S
import numpy as np
import pandas as pd
import random
from mesa import Model
from agent import *
from mesa.time import RandomActivation

class Kitchen(Model):
	"""
	The model for the kitchen cleaning PD game
	"""

	def __init__(self, cf, cleaning_mode, n_agents = 12, sp_mode = "none", remove_player = False, learning_mode = True):
		self.remove_player = remove_player
		self.n_agents = n_agents
		self.min_cf = -10
		self.max_cf = 10
		self.cf = cf
		self.deterioration = 1
		self.agentlist = []
		self.cleaning_mode = cleaning_mode
		self.sp_mode = sp_mode
		self.agent_type_list = []
		self.run_number_list = []
		self.slob_list = []
		self.student_list = []
		self.neatfreak_list = []
		self.cf_list = []
		self.neat_c = []
		self.slob_c = []
		self.student_c = []
		self.learning_mode = learning_mode
	
		# matrix for awarded rewards
		self.player_rewards = []

		self.matrix = np.zeros((21,self.n_agents))
		self.run_number = 0
		for i in range(n_agents):
			check = i%3
			self.new_agent(i, check)

	def new_agent(self, roomnumber, check):
		if check == 0:
			self.agent_type_list.append('Slob')
			agent = Agent_type(roomnumber, self.max_cf, self.cf, self.sp_mode, self.n_agents, id = 'Slob')
		if check == 1:
			self.agent_type_list.append('NeatFreak')
			agent = Agent_type(roomnumber, self.max_cf, self.cf, self.sp_mode, self.n_agents, id = 'NeatFreak')
		if check == 2:
			self.agent_type_list.append('Student')
			agent = Agent_type(roomnumber, self.max_cf, self.cf, self.sp_mode, self.n_agents, id = 'Student')
		self.agentlist.append(agent)

	def remove_agent(self, agent):
		self.agentlist.remove(agent)
		self.n_agents -= 1

	def remove_player(self, player):
		if player.player_status == 0:
			room = player.room
			self.remove_agent(player)
			check = random.randint(0, 2)
			self.agent_type_list.remove(player.id)
			self.new_agent(player.room, check)
			self.n_agents += 1
			self.run_number_list.append(self.run_number)
			
	def social_punishment(self,n_cooperators):
			# calculate social punishment
		if self.sp_mode == "none":
			sp = 0
			predict_sp = 0
		elif self.sp_mode == "mode1":
			if self.n_agents != n_cooperators:
				sp = self.max_cf - (self.max_cf - self.cf) / (self.n_agents - n_cooperators)
			else:
				sp = 0
		return sp

	def cleaning(self, n_cooperators, p_cooperators):
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
     

	
	def backwards_learning(self, sp):

		'''Backwards learning is a learning method in which the agent learns what
		 how his own choices affected the other agents' choosing behaviour and 
		 updates it's payoff matrix based on this.'''
		total = 0

		for i in self.matrix:
			for j in i:
				total += j
		
		number_player = 0
		for player in self.agentlist:
			column_total = sum(self.matrix[:,number_player])
			
			#introduce negative incentive
			if column_total > total / self.n_agents:
				
				update = (column_total * self.n_agents - total) / self.n_agents
				player.update_rewards(self.cf,self.n_agents, sp, update)
				
			
			number_player += 1

	def forwards_learning(self, sp):
		'''Forward learning is a learning method that checks if own percentage 
		of cooperation is higher than that of others and updates payoff matrix'''
		person = 0		
		for element in self.matrix[10]:
			ccp = 1
			if element == 0:
				ccp = 0
			new_matrix = self.matrix.copy()
			new_matrix = np.delete(new_matrix,person,1)

			total_nr_previous = 0

			for i in range(0,9):
				for j in new_matrix[i]:
					
					total_nr_previous += j
			
			total_nr_after = 0

			for i in range(11,20):
				for j in new_matrix[i]:
					total_nr_after += j
			
			difference = total_nr_after - total_nr_previous
			
			current_player = self.agentlist[person]
			current_player.difference_list.append(difference)
			incentive = current_player.incentive(self.run_number)
			current_player.update_rewards(self.cf, self.n_agents, sp ,difference = incentive, ccp = ccp)

			person += 1

	def give_player_rewards(self, player, n_cooperators, sp):
				# make actual reward matrix to grant to agents: 
		if n_cooperators > 0:
			reward_matrix = np.array([[self.max_cf - (self.max_cf - self.cf) / n_cooperators, self.cf],
                             		  [self.max_cf - sp, self.cf]])
		else: 
			reward_matrix = np.array([[0, self.cf],
                             		  [self.max_cf, self.cf]])

		if player.choice == 'defect': 
			# Punishment
			if n_cooperators == 0: 
				self.player_rewards[-1].append(reward_matrix[1,1])
			# Temptation
			else: 
				self.player_rewards[-1].append(reward_matrix[1,0])

		else:
			# Sucker
			if n_cooperators == 0: 
				self.player_rewards[-1].append(reward_matrix[0,1])
			# Reward
			else: 
				self.player_rewards[-1].append(reward_matrix[0,0]) 


	def options(self, player, student_options, neat_options, slob_options):
		'''Checks for all types of agent if cooperate'''
		
		
		if player.id == 'Student' and player.choice == 'cooperate':
			student_options += 1

		if player.id == 'NeatFreak' and player.choice == 'cooperate':
			neat_options += 1

		if player.id == 'Slob' and player.choice == 'cooperate':
			slob_options += 1

		return student_options, neat_options, slob_options

	def step(self):
		
		# add row to reward list
		self.player_rewards.append([])
		choices = []
		matrix_loop = 0
		choice_list = []
		neat_options = 0
		slob_options = 0
		student_options = 0
		
		for player in self.agentlist:
			player.step()
			student_options, neat_options, slob_options = self.options(player, student_options, neat_options, slob_options)
			choices.append(player.choice)
			if player.choice == 'cooperate':
				choice_list.append(1)
			else :
				choice_list.append(0)
		self.student_c.append(student_options)
		self.neat_c.append(neat_options)
		self.slob_c.append(slob_options)
		
		# calculate number of cooperators and proportion of cooperators
		n_cooperators = choices.count('cooperate')
		p_cooperators = n_cooperators/self.n_agents
  	
		sp = self.social_punishment(n_cooperators)
		self.cleaning(n_cooperators,p_cooperators)

		# update predicted social punishment
		if self.sp_mode == "mode1":
			predict_sp = self.max_cf - self.cf
		
		else:
			predict_sp = 0

		# sla rewards op in self.player_rewards
		for player in self.agentlist:
			self.give_player_rewards(player, n_cooperators, predict_sp)
			# update reward matrix of player
			if self.remove_player == True:			
				self.remove_player(player)
			player.update_rewards(self.cf, self.n_agents, predict_sp)

		# Creates matrix where 1 signifies cooperation and 0 defection.

		self.matrix = np.delete(self.matrix,0,axis = 0)
		self.matrix = np.insert(self.matrix,20,choice_list, axis = 0)
		if self.learning_mode == True:
			self.backwards_learning(predict_sp)
			if self.run_number > 20:
				self.forwards_learning(predict_sp)
		self.run_number += 1
		
	def run_model(self, step_total):
		self.cfdata = [self.cf]
		for i in range(step_total):

			self.step()

			self.slob_list.append(self.agent_type_list.count('Slob'))
			self.student_list.append(self.agent_type_list.count('Student'))
			self.neatfreak_list.append(self.agent_type_list.count('NeatFreak'))
			self.cf_list.append(self.cf)
		

			self.cfdata.append(self.cf)
		self.player_rewards = np.array(self.player_rewards)
		
			
	
	