import numpy as np

data = np.loadtxt("csv_pre.csv", delimiter=",", dtype="unicode")[:, 1]

print(data)
