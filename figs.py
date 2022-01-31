from model import Kitchen
import numpy as np
import matplotlib.pyplot as plt


def __main__():
    print("plotting different starting values")
    for i in [-10, -5, 0, 5, 10]:
        model = Kitchen(cf=i)
        model.run_model(20)
        plt.plot(model.cfdata)
    plt.legend(["-10", "-5", "0", "5", "10"])
    plt.savefig("figs/plot_startingvalues.png", dpi=300)

    print("plotting different deteriorations")
    cf = 9
    for i in [0, 2, 4, 6]:
        model = Kitchen(cf=cf, deterioration=i)
        model.run_model(20)
        plt.plot(model.cfdata)
        print(model.cfdata)
    plt.legend(["0", "2", "4", "6"])
    plt.savefig("figs/plot_deteriorations_startcf{}.png".format(cf), dpi=300)

if __name__ == "__main__":
    __main__()

