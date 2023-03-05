import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import signal


# read in data
dataset = pd.read_csv('//')
df = pd.DataFrame(dataset, columns=['Time', 'Voltage'])

# voltage cuts off at 1023. Multiply by 5/1023 to get a baseline

df['Time'] = df['Time'] / 1000
time = df['Time']
df['Voltage'] = df['Voltage'] * (5 / 1023)
voltage = df['Voltage'] - 2.5


# RMS EMG
rms_emg = np.sqrt(np.mean(np.square(df), axis=1))
df['RMS EMG'] = rms_emg


# EMG Frequency
fft = np.fft.fft(rms_emg)
psd = np.abs(fft) ** 2
freq = np.fft.fftfreq(len(rms_emg), 1.0 / 1200)


# Power Spectrum
f, psd_1 = signal.welch(voltage, fs=1200, nperseg=256, noverlap=128)


# Plotting
fig_1, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(time, voltage)
ax1.set_title('Raw Data')
ax2.plot(time, rms_emg)
ax2.set_title('Root Mean Square')

fig_2, (ax3, ax4) = plt.subplots(1, 2)
ax3.plot(freq, psd)
ax3.set_title('Frequency (Hz)')
ax4.plot(f, psd_1)
ax4.set_title('Power Spectral Density')


plt.show()
