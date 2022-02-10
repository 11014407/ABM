from model import Kitchen
import matplotlib.pyplot as plt
import numpy as np

'''
Global sensitivity analysis of every module within the system.
	BATCH_AMOUNT: size of the batch
	TIME_STEPS: number of steps the model runs
	x: array of 365 time steps for the x-axis'''

BATCH_AMOUNT = 50
TIME_STEPS = 365
x = np.linspace(0, TIME_STEPS, TIME_STEPS)

# Matrix filled with 365 rows and 50 columns
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))

# Run the model
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cleaning_mode = "full", cf = 0,  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column
	print(i)

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
# Plot the error
plt.plot(x, mean_array, label = "full baseline")
plt.fill_between(x, mean_array -err, mean_array+err)

'''
Run the system with module variation.
'''
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cleaning_mode = "proportional", cf = 0,  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)



plt.plot(x, mean_array, label = "proportional")
plt.fill_between(x, mean_array -err, mean_array+err)



full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0, cleaning_mode = "full",  sp_mode="mode1", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))



mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "Social punishment")
plt.fill_between(x, mean_array -err, mean_array+err)



full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "full", sp_mode="none", remove_player = True, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))



mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "ostracization")
plt.fill_between(x, mean_array -err, mean_array+err)

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "full", sp_mode="none", remove_player = False, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column


mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "Learning")
plt.fill_between(x, mean_array -err, mean_array+err)

# Show the plot
plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()

'''
Do the same for different module variations
'''

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)



plt.plot(x, mean_array, label = "proportional baseline")
plt.fill_between(x, mean_array -err, mean_array+err)




full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional", sp_mode="mode1", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)



plt.plot(x, mean_array, label = "social punishment")
plt.fill_between(x, mean_array -err, mean_array+err)
plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()


full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)



plt.plot(x, mean_array, label = "proportional baseline")
plt.fill_between(x, mean_array -err, mean_array+err)

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = True, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column



mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))



mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "ostracization")
plt.fill_between(x, mean_array -err, mean_array+err)
plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)



plt.plot(x, mean_array, label = "proportional baseline")
plt.fill_between(x, mean_array -err, mean_array+err)

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column


mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "Learning")
plt.fill_between(x, mean_array -err, mean_array+err)

plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)


plt.plot(x, mean_array, label = "proportional baseline")
plt.fill_between(x, mean_array -err, mean_array+err)
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = True, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "Learning and ostracization")
plt.fill_between(x, mean_array -err, mean_array+err)

plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)

plt.plot(x, mean_array, label = "proportional baseline")
plt.fill_between(x, mean_array -err, mean_array+err)

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="mode1", remove_player = False, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "Learning and social punishment")
plt.fill_between(x, mean_array -err, mean_array+err)

plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)

plt.plot(x, mean_array, label = "proportional baseline")
plt.fill_between(x, mean_array -err, mean_array+err)
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="mode1", remove_player = True, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "social punishment and ostracization")
plt.fill_between(x, mean_array -err, mean_array+err)

plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()
full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)

plt.plot(x, mean_array, label = "proportional baseline")
plt.fill_between(x, mean_array -err, mean_array+err)

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cf = 0,cleaning_mode = "proportional", sp_mode="mode1", remove_player = True, learning_mode = True)
	model_base.run_model(TIME_STEPS)
	column = np.array(model_base.cf_list)
	full_matrix[:, i] = column

mean_array = np.array([])
err_array = np.array([])
for i in range(TIME_STEPS):
	mean_array = np.append(mean_array, np.mean(full_matrix[i]))
	std = np.std(full_matrix[i])
	err = 1.96*std/np.sqrt(TIME_STEPS)
	err_array = np.append(err_array, err)
plt.plot(x, mean_array, label = "All modules")
plt.fill_between(x, mean_array -err, mean_array+err)




plt.xlabel("Time steps")
plt.ylabel("mean cleanliness factor")
plt.legend()
plt.show()