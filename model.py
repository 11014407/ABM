import numpy as np
import random
from mesa import Model
from agent import *

class Kitchen(Model):
	"""
	The model for the kitchen cleaning PD game
	"""
	def __init__(self, cf, cleaning_mode, n_agents = 12, sp_mode = "none", remove_player = False, learning_mode = True, variable_rows = 21):
		'''
		Initializes a Kitchen with a certain environment.
		ARGS:
			-cf: The current cleanliness factor of the shared kitchen.
			-cleaning_mode: every agent cleans it's own part of kitchen or entire kitchen(Full)
			-n_agents : number of agents in the system.
			-sp_mode: either with or without social punishment.
			-remove_player: system with or without ostracization.
			-learning_mode: with or without learning.
			-variable_rows: number of rows(at least 3) on what the agent bases its forward learning.
		'''
		# Check if variable rows has a valid entry
		if variable_rows < 3 or variable_rows % 2 == 0:
			print('Error : variable rows should be uneven and higher than 2') 
			exit()
		
		if n_agents < 2:
			print('Error: Number of agents should be at least 2')
			exit()
		
		if cf < -10 or cf > 10:
			print('Error: Cleanliness factor out of bounds of min value and max values.' )
			print('should be between -10 and 10')
			exit()

		# Initialize all model properties
		self.ostracization = remove_player
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
		self.variable_rows = variable_rows
	
		# Matrix for awarded rewards
		self.player_rewards = []
  
		# Creates matrix later used for learning
		self.matrix = np.zeros((variable_rows,self.n_agents))
		self.run_number = 0
  
		# Checks which agent type to initialize.
		for i in range(n_agents):
			check = i%3
			self.new_agent(i, check)

	def new_agent(self, roomnumber, check):
		'''
  		Creates three different agents types, each with its own incentive to clean
		ARGS: 
			-roomnumber: includes an id for every seperate agent
			-check: checks which type of agent to create
		'''
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
		'''
  		Removes agent
		ARGS:
			-agent: agent to remove from system
		'''
		self.agentlist.remove(agent)
		self.n_agents -= 1

	def remove_player(self, player):
		'''
  		Checks whether player status is so low as to remove player from the system
		ARGS:
			-player: player potentionally to be removed from the system
		'''
		if player.player_status == 0:
			room = player.room
			self.remove_agent(player)
   
			# replace removed player with new player
			check = random.randint(0, 2)
			self.agent_type_list.remove(player.id)
			self.new_agent(player.room, check)
			self.n_agents += 1
			self.run_number_list.append(self.run_number)
			
	def social_punishment(self,n_cooperators):
		'''
  		Includes social punishment in payoff matrix of agent when defecting
		ARGS:
			-n_cooperators: number of cooperators, if zero no punishment is included.
		output: Returns social punishment as float.
		'''
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
		'''
  		Updates the state of the kitchen
		ARGS:
			-n_cooperators: number of cleaning cooperators
			-p_cooperators: number of cooperators in proportional method
		'''
		if self.cleaning_mode == 'full': 
			# Option 1: kitchen is cleaned fully if only one agent cooperates.
			if n_cooperators > 0: 
				self.cf = self.max_cf
			else: 
				if self.cf > self.min_cf: 
					self.cf -= self.deterioration

		if self.cleaning_mode == 'proportional': 
			# Option 2: increase in cf is proportional to number of agents that cooperate, namely 
			# The difference between max_cf and the current state times the proportion of cooperators.
			if n_cooperators > 0:
				self.cf += (self.max_cf - self.cf)*p_cooperators
				self.cf = int(self.cf)
			else: 
				if self.cf > self.min_cf: 
					self.cf -= self.deterioration
	
	def backwards_learning(self, sp):
		'''
  		Backwards learning is a learning method in which the agent learns how
    	his own choices affected the other agents' choosing behaviour and 
		updates it's payoff matrix based on this.
		ARGS:
			-sp: Social punishment
		'''
		total = 0
		
		for i in self.matrix:
			for j in i:
				total += j
		
		number_player = 0
  
		for player in self.agentlist:
			column_total = sum(self.matrix[:,number_player])
			
			# Introduce negative incentive
			if column_total > total / self.n_agents:
				update = (column_total * self.n_agents - total) / self.n_agents
				player.update_rewards(self.cf,self.n_agents, sp, update)
				
			number_player += 1

	def forwards_learning(self, sp):
		'''
  		Forward learning is a learning method that checks if own percentage 
		of cooperation is higher than that of others and updates payoff matrix
		ARGS:
			-sp: social punishment
		'''
		person = 0	
		
		for element in self.matrix[int((self.variable_rows - 1)/2)]:
			ccp = 0
   
			if element == 1:
				ccp = 1
    
			new_matrix = self.matrix.copy()
			new_matrix = np.delete(new_matrix,person,1)

			total_nr_previous = 0
			# Checks all rows before the middle one
			for i in range(0,(int(((self.variable_rows -1))/ 2)) - 1):
				for j in new_matrix[i]:
					total_nr_previous += j
			
			total_nr_after = 0
			# Checks rows after middle one
			for i in range(int((self.variable_rows - 1)/ 2) + 1,self.variable_rows - 1):
				for j in new_matrix[i]:
					total_nr_after += j
			
			# Calculate the difference
			difference = total_nr_after - total_nr_previous
			current_player = self.agentlist[person]
			current_player.difference_list.append(difference)
			incentive = current_player.incentive(self.run_number,self.variable_rows)
			current_player.update_rewards(self.cf, self.n_agents, sp ,difference = incentive, ccp = ccp)

			person += 1

	def give_player_rewards(self, player, n_cooperators, sp):
		'''
  		Gives players rewards or punishments based on cooperation or defection
		ARGS:
			-player: agent to receive reward or punishment.
			-n_cooperators: number of cooperators.
			-sp: social punishment
		'''
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
			self.player_rewards[-1].append(reward_matrix[0,0]) 

	def options(self, player, student_options, neat_options, slob_options):
		'''
  		Checks for all types of agent if they cooperate
		ARGS:
			student_options: empty list which will later receive choices of students.
			neat_options: empty list which will later receive choices of neatfreaks.
			slob_options: empty list which will later receive choices of slobs.
		output: Returns three integer values.
		'''
		if player.id == 'Student' and player.choice == 'cooperate':
			student_options += 1

		if player.id == 'NeatFreak' and player.choice == 'cooperate':
			neat_options += 1

		if player.id == 'Slob' and player.choice == 'cooperate':
			slob_options += 1

		return student_options, neat_options, slob_options

	def step(self):
		'''
  		Step function goes through all steps all agents need to complete in one time step 
		of the game of cleaning the kitchen
		'''
		# Add row to reward list and initializes lists and values.
		self.player_rewards.append([])
		choices = []
		matrix_loop = 0
		choice_list = []
		neat_options = 0
		slob_options = 0
		student_options = 0
		
		# Runs a single instance of the prisoners dillema and looks at all player choices.
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
		
		# Calculate number of cooperators and proportion of cooperators
		n_cooperators = choices.count('cooperate')
		p_cooperators = n_cooperators/self.n_agents

		# Update the social punishment values and the cleaniness factor.
		sp = self.social_punishment(n_cooperators)
		self.cleaning(n_cooperators,p_cooperators)

		# Update predicted social punishment
		if self.sp_mode == "mode1":
			predict_sp = self.max_cf - self.cf
		else:
			predict_sp = 0

		# Save player rewards
		for player in self.agentlist:
			self.give_player_rewards(player, n_cooperators, predict_sp)
   
			# Update reward matrix of player
			if self.ostracization == True:			
				self.remove_player(player)
    
			player.update_rewards(self.cf, self.n_agents, predict_sp)

		# Updates matrix, where 1 signifies cooperation and 0 defection.
		self.matrix = np.delete(self.matrix,0,axis = 0)
		self.matrix = np.insert(self.matrix,self.variable_rows - 1,choice_list, axis = 0)
  
		if self.learning_mode == True:
			self.backwards_learning(predict_sp)
			if self.run_number > self.variable_rows:
				# Learning is initialized only after matrix has entirely been replaced by players' choices
				self.forwards_learning(predict_sp)
    
		self.run_number += 1
		
	def run_model(self, step_total):
		'''
  		Runs model for the step total
		ARGS:
			-step_total: total number of steps the entire system runs
		'''
		self.cfdata = [self.cf]
  
		for i in range(step_total):
			self.step()
   
			# Save agent types and cleanliness factor
			self.slob_list.append(self.agent_type_list.count('Slob'))
			self.student_list.append(self.agent_type_list.count('Student'))
			self.neatfreak_list.append(self.agent_type_list.count('NeatFreak'))
			self.cf_list.append(self.cf)
			self.cfdata.append(self.cf)
   
		# Save all player rewards
		self.player_rewards = np.array(self.player_rewards)