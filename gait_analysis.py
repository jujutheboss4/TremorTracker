import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# file names
normal = ''
parkinsons = ''
dataset_1 = pd.read_csv(normal)
df_1 = pd.DataFrame(dataset_1, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])
dataset_2 = pd.read_csv(parkinsons)
df_2 = pd.DataFrame(dataset_2, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])
# organization of time data from ms to seconds of normal walk
df_1['Time'] = df_1['Time'] / 1000
time_1 = df_1['Time']
# changing of bits (2^10) to 5 volts; bring starting voltage back to 0V by subtraction of 2.5
df_1['Voltage'] = df_1['Voltage'] * (5 / 1023)
voltage_1 = df_1['Voltage'] - 2.5
# gyroscopic data for the z-axis of normal walk
gyro_z_1 = df_1['Gyro-Z']
# flip across x-axis since gyroscope is facing opposite of body
gyro_z_1 = -gyro_z_1
# organization of time data from ms to seconds of Parkinson's walk
df_2['Time'] = df_2['Time'] / 1000
time_2 = df_2['Time']
# changing of bits (2^10) to 5 volts; bring starting voltage back to 0V by subtraction of 2.5
df_2['Voltage'] = df_2['Voltage'] * (5 / 1023)
voltage_2 = df_2['Voltage'] - 2.5
# gyroscopic data for the z-axis of Parkinson's walk
gyro_z_2 = df_2['Gyro-Z']
# flip across x-axis since gyroscope is facing opposite of body
gyro_z_2 = -gyro_z_2

# lines 33 - 57 are for normal data
# find gradient of gyro-z for finding peak
# after passing the baseline starting point, muscle activation begins until peak of angular data
derivative_1 = np.gradient(gyro_z_1, time_1)
pos_der_1 = np.where(derivative_1 > 0)[0]
# create new array for points where muscle activation should occur
activation_should_occur_1 = []
for position_1 in pos_der_1:
    if gyro_z_1[position_1] >= 0:
        activation_should_occur_1.append(position_1)
# create new array for points where muscle activation should not occur and count how many points there are
activation_should_not_occur_1 = []
for index in range(len(derivative_1)):
    if index not in activation_should_occur_1:
        activation_should_not_occur_1.append(index)
count_activation_should_not_occur_1 = len(activation_should_not_occur_1)
# consider 100% above average voltage as muscle activation
starting_voltage_1 = np.mean(voltage_1)
points_outside_count_1 = 0
# count points where muscle is activated when activation shouldn't occur
for points_1 in activation_should_not_occur_1:
    if abs(gyro_z_1[points_1]) >= 2 * starting_voltage_1:
        points_outside_count_1 += 1
# find the percentage of activation outside correct zones
percent_activation_outside_1 = points_outside_count_1 / count_activation_should_not_occur_1

# lines 59 - 83 are for Parkinson's data
# find gradient of gyro-z for finding peak
# after passing the baseline starting point, muscle activation begins until peak of angular data
derivative_2 = np.gradient(gyro_z_2, time_2)
pos_der_2 = np.where(derivative_2 > 0)[0]
# create new array for points where muscle activation should occur
activation_should_occur_2 = []
for position_2 in pos_der_2:
    if gyro_z_2[position_2] >= 0:
        activation_should_occur_2.append(position_2)
# create new array for points where muscle activation should not occur and count how many points there are
activation_should_not_occur_2 = []
for index in range(len(derivative_2)):
    if index not in activation_should_occur_2:
        activation_should_not_occur_2.append(index)
count_activation_should_not_occur_2 = len(activation_should_not_occur_2)
# consider 100% above average voltage as muscle activation
starting_voltage_2 = np.mean(voltage_2)
points_outside_count_2 = 0
# count points where muscle is activated when activation shouldn't occur
for points_2 in activation_should_not_occur_2:
    if abs(gyro_z_2[points_2]) >= 2 * starting_voltage_2:
        points_outside_count_2 += 1
# find the percentage of activation outside correct zones
percent_activation_outside_2 = points_outside_count_2 / count_activation_should_not_occur_2

# find percent difference from percent activation outside correct zones for both normal and Parkinson's data
percent_difference_numerator = np.abs(percent_activation_outside_1 - percent_activation_outside_2) * 100
percent_difference_denominator = (percent_activation_outside_1 + percent_activation_outside_2) / 2
percent_difference = percent_difference_numerator / percent_difference_denominator

# print
print(percent_difference)
