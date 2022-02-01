from model import Kitchen
import numpy as np


def __main__():
	model = Kitchen(cleaning_mode='full', step_total = 20, sp_mode="none")
	model.run_model(20)

if __name__ == "__main__":
    __main__()