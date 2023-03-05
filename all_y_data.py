import matplotlib.pyplot as plt
import pandas as pd

# Read in data sets and sort by name
dataset_1 = pd.read_csv('/path/to/file')
df_1 = pd.DataFrame(dataset_1, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])
dataset_2 = pd.read_csv('/path/to/file')
df_2 = pd.DataFrame(dataset_2, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])
dataset_3 = pd.read_csv('/path/to/file')
df_3 = pd.DataFrame(dataset_3, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])
dataset_4 = pd.read_csv('/path/to/file')
df_4 = pd.DataFrame(dataset_4, columns=['Voltage', 'Gyro-X', 'Gyro-Y', 'Gyro-Z', 'Time'])

# Define where the time, voltage, and gyro_z is and pre-process data
df_1['Time'] = df_1['Time'] / 1000
time_1 = df_1['Time']
df_1['Voltage'] = df_1['Voltage'] * (5 / 1023)
voltage_1 = df_1['Voltage'] - 2.5

gyro_x_1 = df_1['Gyro-X']
gyro_y_1 = df_1['Gyro-Y']
gyro_z_1 = df_1['Gyro-Z']

df_2['Time'] = df_2['Time'] / 1000
time_2 = df_2['Time']
df_2['Voltage'] = df_2['Voltage'] * (5 / 1023)
voltage_2 = df_2['Voltage'] - 2.5

gyro_x_2 = df_2['Gyro-X']
gyro_y_2 = df_2['Gyro-Y']
gyro_z_2 = df_2['Gyro-Z']

df_3['Time'] = df_3['Time'] / 1000
time_3 = df_3['Time']
df_3['Voltage'] = df_3['Voltage'] * (5 / 1023)
voltage_3 = df_3['Voltage'] - 2.5

gyro_x_3 = df_3['Gyro-X']
gyro_y_3 = df_3['Gyro-Y']
gyro_z_3 = df_3['Gyro-Z']

df_4['Time'] = df_4['Time'] / 1000
time_4 = df_4['Time']
df_4['Voltage'] = df_4['Voltage'] * (5 / 1023)
voltage_4 = df_4['Voltage'] - 2.5

gyro_x_4 = df_4['Gyro-X']
gyro_y_4 = df_4['Gyro-Y']
gyro_z_4 = df_4['Gyro-Z']


# plot data
fig, axs = plt.subplots(1)

# plot data on each subplot
axs[0].plot(time_1, gyro_x_1, label='normal 1 x')
axs[0].plot(time_2, gyro_x_2, label='park 1 x')
axs[0].plot(time_3, gyro_x_3, label='normal 2 x')
axs[0].plot(time_4, gyro_x_4, label='park 2 x')
axs[0].legend()
axs[0].set_title('All x values')

axs[1].plot(time_1, gyro_y_1, label='normal 1 y')
axs[1].plot(time_2, gyro_y_2, label='park 1 y')
axs[1].plot(time_3, gyro_y_3, label='normal 2 y')
axs[1].plot(time_4, gyro_y_4, label='park 2 y')
axs[1].legend()
axs[1].set_title('All y values')

axs.plot(time_1, gyro_z_1, label='normal 1 z')
axs.plot(time_1, voltage_1, label='normal 1 voltage')
axs[2].plot(time_3, gyro_z_3, label='normal 2 z')
axs[2].plot(time_4, gyro_z_4, label='park 2 z')
axs.legend()
axs.set_title('All z values')

axs[1].plot(time_2, gyro_x_2, label='x')
axs[1].plot(time_2, gyro_y_2, label='y')
axs[1].plot(time_2, gyro_z_2, label='z')
axs[1].legend()
axs[1].set_title('park_walk_arm.csv')

axs[2].plot(time_3, gyro_x_3, label='x')
axs[2].plot(time_3, gyro_y_3, label='y')
axs[2].plot(time_3, gyro_z_3, label='z')
axs[2].legend()
axs[2].set_title('normal_walk_arm_v2.csv')

axs[3].plot(time_4, gyro_x_4, label='x')
axs[3].plot(time_4, gyro_y_4, label='y')
axs[3].plot(time_4, gyro_z_4, label='z')
axs[3].legend()
axs[3].set_title('park_walk_arm_v2.csv')

plt.show()







