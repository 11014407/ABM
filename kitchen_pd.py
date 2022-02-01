from model import Kitchen
import numpy as np


def __main__():
	model = Kitchen(cleaning_mode='proportional')
	model.run_model(50)

if __name__ == "__main__":
    __main__()