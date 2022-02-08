from model import Kitchen
import matplotlib.pyplot as plt
import numpy as np

def __main__(): 


   





    average_number_slobs = []
    average_number_students = []
    average_number_neatfreaks = []
    average_neat_c_learning = []
    average_neat_c_nolearning =[]
    average_slob_c_learning = []
    average_slob_c_nolearning = []
    average_student_c_learning = []
    average_student_c_nolearning = []
    clean_1 = []
    clean_2 = []
    amount_runs = 365

    listo = []
    for j in range(amount_runs):
        average_number_slobs.append(0)
        average_number_students.append(0)
        average_number_neatfreaks.append(0)
        average_neat_c_learning.append(0)
        average_neat_c_nolearning.append(0)
        average_slob_c_learning.append(0)
        average_slob_c_nolearning.append(0)
        average_student_c_learning.append(0)
        average_student_c_nolearning.append(0)
        clean_1.append(0)
        clean_2.append(0)
        listo.append(j)


    for i in range(25):
     
        
        model = Kitchen(cf = 10,cleaning_mode='full',sp_mode = 'mode1' ,remove_player= False)
        model.run_model(amount_runs)
        cf_1_list = model.cf_list
        model_2 = Kitchen(cf = 10,cleaning_mode='full',sp_mode ='mode1',remove_player= False, learning_mode=False)
        model_2.run_model(amount_runs)
        cf_2_list = model_2.cf_list
        neat_list_learning = model.neat_c
        neat_list_nolearning = model_2.neat_c
        slob_list_learning = model.slob_c
        slob_list_nolearning = model_2.slob_c
        student_list_learning = model.student_c
        student_list_nolearning = model_2.student_c

        # plt.plot(listo,cf_1_list, 'r-', label = 'without removed players')
        # plt.plot(listo,cf_2_list, 'b-', label = 'with removed players')
        # plt.legend()
        # plt.show()

        # average_reward = np.mean(model.player_rewards, axis = 1)
        # plt.plot(range(amount_runs), average_reward)
        # plt.xlabel('Timestep')
        # plt.ylabel('Average reward')
        # plt.show()
        # print('len')
        # print(len(model.slob_list))
        for j in range(len(average_number_slobs)):
            average_number_slobs[j] +=  model.slob_list[j]
            average_number_students[j] += model.student_list[j]
            average_number_neatfreaks[j] += model.neatfreak_list[j]
            clean_1[j] += cf_1_list[j]
            clean_2[j] += cf_2_list[j]
            average_neat_c_learning[j] += neat_list_learning[j]
            average_neat_c_nolearning[j] += neat_list_nolearning[j]
            average_slob_c_learning[j] += slob_list_learning[j]
            average_slob_c_nolearning[j] += slob_list_nolearning[j]
            average_student_c_learning[j] += student_list_learning[j]
            average_student_c_nolearning[j] += student_list_nolearning[j]

    for elements in range(365):
        average_number_slobs[elements] = average_number_slobs[elements] / 25
        average_number_students[elements] = average_number_students[elements] / 25
        average_number_neatfreaks[elements] = average_number_neatfreaks[elements] / 25
        clean_1[elements] = clean_1[elements] / 25
        clean_2[elements] = clean_2[elements] / 25
        average_neat_c_learning[elements] = average_neat_c_learning[elements] / 25
        average_neat_c_nolearning[elements] = average_neat_c_nolearning[elements] / 25
        average_slob_c_learning[elements]  = average_slob_c_learning[elements] / 25
        average_slob_c_nolearning[elements] = average_slob_c_nolearning[elements] / 25 
        average_student_c_learning[elements] = average_student_c_learning[elements] / 25
        average_student_c_nolearning[elements] =  average_student_c_nolearning[elements] / 25

    plt.plot(listo,average_neat_c_learning,'r-',label = 'NeatFreak with learning')
    plt.plot(listo,average_neat_c_nolearning,'r--', label = 'NeatFreak no learning')
    plt.legend()
    plt.show()
    plt.plot(listo,average_slob_c_learning,'g-', label = 'Slob with learning')
    plt.plot(listo,average_slob_c_nolearning,'g--', label = 'Slob no learning')
    plt.legend()
    plt.show()
    plt.plot(listo,average_student_c_learning,'b-', label = 'Student with learning')
    plt.plot(listo,average_student_c_nolearning,'b--', label = 'Student no learning')
    plt.legend()
    plt.show()

    plt.plot(listo,clean_1, 'r-', label = 'without ostracization')
    plt.plot(listo,clean_2, 'b-', label = 'with ostracization')
    plt.xlabel('Timesteps')
    plt.ylabel('Cleanliness factor')
    plt.title('Average over 25 runs entire system')
    plt.legend()
    plt.savefig("figs/plot_cf_with_and_without_remove.png", dpi=300)
    plt.show()

    plt.plot(listo,average_number_slobs,'-r', label = 'slob')
    plt.plot(listo,average_number_students,'-g', label = 'normal student')
    plt.plot(listo,average_number_neatfreaks,'-b', label = 'neatfreak')
    plt.xlabel('Timesteps')
    plt.ylabel('Average number of type of agents')
    plt.title('Average over 25 runs entire system')
    plt.legend()
    plt.savefig("figs/plot_amount_agent_type_remove.png", dpi=300)
    plt.show()

if __name__ == "__main__":
     __main__()

