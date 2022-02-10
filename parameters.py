from model import Kitchen
from agent import *
import numpy as np
import matplotlib.pyplot as plt

'''
Global sensitivity analysis of every module within the system.
	BATCH_AMOUNT: size of the batch
	TIME_STEPS: number of steps the model runs
	x: array of 365 time steps for the x-axis
'''

BATCH_AMOUNT = 50
TIME_STEPS = 365
SAMPLE_AMOUNT = 30
x = np.linspace(0, TIME_STEPS, TIME_STEPS)
parameter = np.linspace(-10, 10, 50)

# Matrix filled with 365 rows and 50 columns
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))

# Run the model
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(0, cleaning_mode = "full",  sp_mode="none", remove_player = True, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

# Mean of the batch at every timestep
mean_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

# Error calculation of the mean
mean_array = np.array([])
err_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)

# Make plots
plt.plot(x, mean_array, label = "full baseline")
plt.fill_between(x, mean_array -err, mean_array+err, alpha = 0.2)

# Matrix filled with 365 rows and 50 columns
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))

# Create list of testing values
parameterlist = [7,11,21,19,15,25,57,43]

# Variate values of parameterlist
for i in range(len(parameterlist)):
	model_base = Kitchen(0, cleaning_mode = "full",  sp_mode="none", remove_player=True, learning_mode = True, variable_rows= parameterlist[i])
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

# Mean of the batch at every timestep
mean_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

# Error calculation of the mean
mean_array = np.array([])
err_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)

plt.plot(x, mean_array, label = "different learning rows")
plt.fill_between(x, mean_array -err, mean_array+err, alpha = 0.2)
# Make plots
plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()

for i in range(BATCH_AMOUNT):
	model_base = Kitchen(0, cleaning_mode = "full",  sp_mode="none", remove_player = True, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

# Mean of the batch at every timestep
mean_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

# Error calculation of the mean
mean_array = np.array([])
err_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)

# Make plots
plt.plot(x, mean_array, label = "full baseline")
plt.fill_between(x, mean_array -err, mean_array+err, alpha = 0.2)

# Matrix filled with 365 rows and 50 columns
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))

# Run the model
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(parameter[i], cleaning_mode = "full",  sp_mode="none", remove_player= True, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

# Mean of the batch at every timestep
mean_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

# Error calculation of the mean
mean_array = np.array([])
err_array = np.array([])

for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)

plt.plot(x, mean_array, label = "different initial cf")
plt.fill_between(x, mean_array -err, mean_array+err, alpha = 0.2)

# Make plots
plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()