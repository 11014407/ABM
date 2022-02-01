from model import Kitchen
import matplotlib.pyplot as plt
import numpy as np

def __main__(): 

    model = Kitchen(cleaning_mode='full', step_total = 20)
    model.run_model(20)

    average_reward = np.mean(model.player_rewards, axis = 1)
    plt.plot(range(20), average_reward)
    plt.xlabel('Timestep')
    plt.ylabel('Average reward')
    plt.show()

if __name__ == "__main__":
     __main__()