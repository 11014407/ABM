from operator import mod
from model import Kitchen
import matplotlib.pyplot as plt
import numpy as np

def __main__(): 
    timesteps = 366
    model_runs = 100
    avg_prop = np.zeros(timesteps+1)
    avg_full = np.zeros(timesteps+1)

    for _ in range(model_runs):
        model1 = Kitchen(cleaning_mode = "proportional")
        model1.run_model(timesteps)
        avg_prop += model1.cfdata
        model = Kitchen(cleaning_mode='full')
        model.run_model(timesteps)
        avg_full += model.cfdata

    avg_prop = avg_prop/model_runs
    plt.plot(range(timesteps+1), avg_prop, label="Proportional cleaning, average cf: {}".format(np.round(np.mean(avg_prop)), 3))
    avg_full = avg_full/model_runs
    plt.plot(range(timesteps+1), avg_full, label="Full cleaning, average cf: {}".format(np.round(np.mean(avg_full)), 3))

    plt.xlabel('Timestep')
    plt.ylabel('Cleanliness')
    plt.legend()
    plt.savefig("figs/plot_full_vs_proportional_avg{}runs.png".format(model_runs), dpi=300)
    plt.show()
    plt.clf()

    # model = Kitchen(sp_mode='none', cleaning_mode='proportional')
    # model.run_model(366)
    # plt.plot(range(366+1), model.cfdata)
    # model = Kitchen(sp_mode = "mode1", cleaning_mode='proportional')
    # model.run_model(366)

    # plt.plot(range(366+1), model.cfdata)
    # plt.xlabel('Timestep')
    # plt.ylabel('Cleanliness')
    # plt.legend(["no Social punishment", "with Social punishment"])
    # plt.savefig("figs/social_punishment.png", dpi=300)
    # # plt.show()
    # plt.clf()

    # model = Kitchen(sp_mode = "mode1", cleaning_mode='proportional')
    # model.run_model(366)
    # plt.plot(range(366+1), model.cfdata)
    # # model = Kitchen(sp_mode = "mode1", cleaning_mode='proportional', ostracization = "yes")
    # # model.run_model(366)
    # plt.savefig("figs/proportionalcleaning.png", dpi=300)
    # plt.clf()

    # print("plotting different starting values")
    # for i in [-10, -5, 0, 5, 10]:
    #     model = Kitchen(cf=i, cleaning_mode = "proportional")
    #     model.run_model(366)
    #     plt.plot(model.cfdata)
    # plt.legend(["-10", "-5", "0", "5", "10"])
    # plt.savefig("figs/plot_startingvalues_cleanmodeproportional.png", dpi=300)
    # plt.clf()

    # print("plotting different deteriorations")
    # cf = 9
    # for i in [0, 2, 4, 6]:
    #     model = Kitchen(cf=cf, deterioration=i, cleaning_mode = "proportional")
    #     model.run_model(30)
    #     plt.plot(model.cfdata)
    # plt.legend(["0", "2", "4", "6"])
    # plt.savefig("figs/plot_deteriorations_startcf{}.png".format(cf), dpi=300)
    # plt.clf()

    # start_cf = 0
    # timesteps = 366
    # model_runs = 100
    # avg_ost = np.zeros(timesteps+1)
    # avg_no_ost = np.zeros(timesteps+1)
    # for _ in range(model_runs):
    #     model1 = Kitchen(cf=start_cf, cleaning_mode = "proportional")
    #     model1.run_model(timesteps)
    #     avg_ost += model1.cfdata
    #     model2 = Kitchen(cf=start_cf, cleaning_mode = "proportional", ostracization="yes")
    #     model2.run_model(timesteps)
    #     avg_no_ost += model2.cfdata

    # avg_ost = avg_ost/model_runs
    # plt.plot(range(366+1), avg_ost, label="No Ostracization, average cf: {}".format(np.round(np.mean(avg_ost)), 3))
    # avg_no_ost = avg_no_ost/model_runs
    # plt.plot(range(366+1), avg_no_ost, label="Ostracization, average cf: {}".format(np.round(np.mean(avg_no_ost)), 3))
    # plt.xlabel('Timestep')
    # plt.ylabel('Cleanliness')
    # # plt.title("The average cleanliness over 366 days with and without ostracization, {} model runs".format(model_runs))
    # plt.legend()
    # plt.savefig("figs/ostracization_average{0}runs_startcf{1}_notitle.png".format(model_runs, start_cf), dpi=300)
    # plt.show()
    # plt.clf()

if __name__ == "__main__":
     __main__()