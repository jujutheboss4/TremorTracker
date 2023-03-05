import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy


# Read in data sets and sort by name
dataset_1 = pd.read_csv('/path/to/file')
df_1 = pd.DataFrame(dataset_1, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])
dataset_2 = pd.read_csv('/path/to/file')
df_2 = pd.DataFrame(dataset_2, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])

# Define where the time, voltage, and gyro_z is and pre-process data
df_1['Time'] = df_1['Time'] / 1000
time_1 = df_1['Time']
df_1['Voltage'] = df_1['Voltage'] * (5 / 1023)
voltage_1 = df_1['Voltage'] - 2.5

gyro_z_1 = df_1['Gyro-Z']
gyro_z_1 = - gyro_z_1

df_2['Time'] = df_2['Time'] / 1000
time_2 = df_2['Time']
df_2['Voltage'] = df_2['Voltage'] * (5 / 1023)
voltage_2 = df_2['Voltage'] - 2.5

gyro_z_2 = df_2['Gyro-Z']
gyro_z_2 = - gyro_z_2

# Signal variation
# Find peaks and valleys
peaks, _ = scipy.signal.find_peaks(gyro_z_1)
valleys, _ = scipy.signal.find_peaks(-gyro_z_1)

peaks_y = gyro_z_1[peaks]
valleys_y = gyro_z_1[valleys]

# Determine peak and vally averages
avg_peaks = np.sum(peaks_y) / len(peaks_y)
avg_valleys = np.sum(valleys_y) / len(valleys_y)

# Determine the average amplitude
avg_amp = np.abs(avg_peaks - avg_valleys)
print(avg_amp)

# plot the data
plt.plot(gyro_z_1)
plt.plot(peaks, gyro_z_1[peaks], "x")
plt.xlabel('Time (s)')
plt.ylabel('Gyroscopic Z-Angle (Deg)')
plt.plot(valleys, gyro_z_1[valleys], "x", color='red')
plt.show()
