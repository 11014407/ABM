from model import Kitchen
import matplotlib.pyplot as plt
import numpy as np

BATCH_AMOUNT = 50
TIME_STEPS = 365
x = np.linspace(0, TIME_STEPS, TIME_STEPS)

matrix = np.zeros((4, 4))
print(matrix)
column = np.array([1, 2, 3, 4])
matrix[:, 0] = column
print(matrix)
print(matrix[0])

full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))

for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cleaning_mode = "full",  sp_mode="none", remove_player = False, learning_mode = False)
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
plt.plot(x, mean_array, label = "full baseline")
plt.fill_between(x, mean_array -err, mean_array+err)


full_matrix = np.zeros((TIME_STEPS, BATCH_AMOUNT))
for i in range(BATCH_AMOUNT):
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "full",  sp_mode="mode1", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "full",  sp_mode="none", remove_player = True, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "full",  sp_mode="none", remove_player = False, learning_mode = True)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="mode1", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = True, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = True)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = True, learning_mode = True)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="mode1", remove_player = False, learning_mode = True)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="mode1", remove_player = True, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="none", remove_player = False, learning_mode = False)
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
	model_base = Kitchen(cleaning_mode = "proportional",  sp_mode="mode1", remove_player = True, learning_mode = True)
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