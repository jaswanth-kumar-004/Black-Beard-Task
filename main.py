import pyedflib
import numpy as np
import matplotlib.pyplot as plt

dt = 0.001                                              # 3000 points in 30 secs = 30/3000 = 0.001 secs

fRaw = pyedflib.EdfReader('SC4001E0-PSG.edf')           # Reading .edf file

numReadings = len((fRaw.readSignal(0)[1:1000]))         # Only using 1000 data points for easy visualization
fCap = np.fft.fft(fRaw.readSignal(0)[1:1000])           # Fourier Transform is being calculated
lenFreqs = len(fCap)
freqs = (1 / (dt * lenFreqs)) * np.arange(lenFreqs)
PSD = (fCap * np.conj(fCap))/numReadings                # Getting the amplitude of the Power Spectrum

isThreshhold = PSD > 10000                              # Threshold for the Power Spectrum
newPSD = PSD * isThreshhold                             # Removing all the frequencies with low threshhold amplitude
fCap = fCap * isThreshhold
fFin = (np.fft.ifft(fCap))                              # Inverse Transform of the filtered data

plt.plot(fRaw.readSignal(0)[1:1000], 'r')               # Unfiltered Raw Data
plt.plot(np.real(fFin), 'b')                            # Filtered Final Data
plt.show()                                              # Final Plot