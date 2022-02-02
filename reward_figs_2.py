from model import Kitchen
import matplotlib.pyplot as plt
import numpy as np

def __main__(): 

    model = Kitchen(cleaning_mode='full')
    model.run_model(366)

    average_reward = np.mean(model.player_rewards, axis = 1)
    plt.plot(range(366+1), model.cfdata)
    model = Kitchen(cleaning_mode='proportional')
    model.run_model(366)

    average_reward = np.mean(model.player_rewards, axis = 1)
    plt.plot(range(366+1), model.cfdata)
    plt.xlabel('Timestep')
    plt.ylabel('Cleanliness')
    plt.legend(["Full cleaning", "proportional cleaning"])
    plt.savefig("figs/plot_full_vs_proportional.png", dpi=300)
    # plt.show()
    plt.clf()


    model = Kitchen(sp_mode='none', cleaning_mode='proportional')
    model.run_model(366)
    plt.plot(range(366+1), model.cfdata)
    model = Kitchen(sp_mode = "mode1", cleaning_mode='proportional')
    model.run_model(366)

    plt.plot(range(366+1), model.cfdata)
    plt.xlabel('Timestep')
    plt.ylabel('Cleanliness')
    plt.legend(["no Social punishment", "with Social punishment"])
    plt.savefig("figs/social_punishment.png", dpi=300)
    # plt.show()
    plt.clf()



    model = Kitchen(sp_mode = "mode1", cleaning_mode='proportional')
    model.run_model(366)
    plt.plot(range(366+1), model.cfdata)
    # model = Kitchen(sp_mode = "mode1", cleaning_mode='proportional', ostracization = "yes")
    # model.run_model(366)
    plt.savefig("figs/proportionalcleaning.png", dpi=300)
    plt.clf()

    # plt.plot(range(366+1), model.cfdata)
    # plt.xlabel('Timestep')
    # plt.ylabel('Cleanliness')
    # plt.legend(["no ostracization", "ostracization"])
    # plt.savefig("figs/ostracization.png", dpi=300)
    # plt.show()

    print("plotting different starting values")
    for i in [-10, -5, 0, 5, 10]:
        model = Kitchen(cf=i, cleaning_mode = "proportional")
        model.run_model(366)
        plt.plot(model.cfdata)
    plt.legend(["-10", "-5", "0", "5", "10"])
    plt.savefig("figs/plot_startingvalues_cleanmodeproportional.png", dpi=300)
    plt.clf()

    print("plotting different deteriorations")
    cf = 9
    for i in [0, 2, 4, 6]:
        model = Kitchen(cf=cf, deterioration=i, cleaning_mode = "proportional")
        model.run_model(30)
        plt.plot(model.cfdata)
    plt.legend(["0", "2", "4", "6"])
    plt.savefig("figs/plot_deteriorations_startcf{}.png".format(cf), dpi=300)
    plt.clf()

    print("plotting N cooperators")

if __name__ == "__main__":
     __main__()