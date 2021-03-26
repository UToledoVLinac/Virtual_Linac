import numpy as np
from scipy import interpolate
import os
import matplotlib.pyplot as plt

measured_data = '6FFF_profile_X30cm.txt'
path = os.getcwd()
measured_path = os.path.join(path, measured_data)
measured_data_array = np.loadtxt(measured_path)
x_measured = measured_data_array[:, 0]
y_measured = measured_data_array[:, 1]
output_data = '6FFF_profile_X30_output.txt'
output_path = os.path.join(path, output_data)
output_data_array = np.loadtxt(output_path)
x_output = output_data_array[:, 0]
y_output = output_data_array[:, 1]
index_min = ''
index_max = ''
print(len(x_measured))

if x_measured[0] < -200:
    for i in range(0, len(x_measured) - 1):
        if x_measured[i] < -200 <= x_measured[i + 1]:
            index_min = i
    for j in range(0, len(x_measured) - 1):
        if x_measured[j] <= 200 < x_measured[j + 1]:
            index_max = j + 1
    print(index_max, index_min)
    x_new = x_output
    y_interp = interpolate.interp1d(x_measured[index_min:index_max],
                                    y_measured, kind='linear')
    y_measured_new = y_interp(x_new)
    y_measured_normalize = y_measured_new / max(y_measured_new)
    y_diff = (y_measured_normalize - y_output) / y_measured_normalize

    plt.plot(x_new, y_measured_normalize)
    plt.plot(x_output, y_output)
    plt.plot(x_output, y_diff)
    plt.show()

