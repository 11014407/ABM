from model import Kitchen
import matplotlib.pyplot as plt
from SALib.sample import saltelli
from agent import Student
from agent_types import *
from mesa.batchrunner import BatchRunner
from SALib.analyze import sobol
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

BATCH_AMOUNT = 50
TIME_STEPS = 365
SAMPLE_AMOUNT = 30
x = np.linspace(0, TIME_STEPS, TIME_STEPS)

model_reporters = {"Cleaning factor" : lambda m: m.cf}
data = {}
samples = np.linspace(-10, 10, SAMPLE_AMOUNT)

batch = BatchRunner(Kitchen, max_steps = TIME_STEPS, iterations = BATCH_AMOUNT, variable_parameters = {'cf': samples}, model_reporters = model_reporters, display_progress = True)

batch.run_all()
data[var] = batch.get_model_vars_dataframe()