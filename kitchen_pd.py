from model import Kitchen
import matplotlib.pyplot as plt
import numpy as np

def __main__(): 
    # Initialize model
    model = Kitchen(cf = 0,cleaning_mode = "proportional",n_agents= 12, sp_mode="mode1", remove_player = True, learning_mode = True, variable_rows = 1)
    
    # Run the model
    model.run_model(365)
    cleanliness = model.cf_list
    x = np.linspace(0,365,365)
    
    # Plot cleanliness factor
    plt.plot(x,cleanliness,'r-')
    plt.xlabel('Timestep')
    plt.ylabel('Cleanliness factor')
    plt.show()


if __name__ == "__main__":
     __main__()