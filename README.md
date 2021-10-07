# Black-Beard-Task

Steps
-----
(Note : Only 1000 Data Points are only being processed to produce a faster result)

- The given .edf file is read and stored
- The Fourier Transform is being calculated to give the Power Spectrum
- The Amplitude of the Power SPectrum is calculated at various frequencies
- Frequencies with a very lows Power Spectrum can be considered as noise and thus removed
- Inverse Fourier Transform is done to get the filtered clean signal


Regarding the DeepSleepNet Model the Python version used is 3.5.4 but the Python I'm using in my PC is 3.9 and so the Tensorflow was not working properly. Unfortunately in the given time constraint and due to exams I was not able to do the final part of the task. 
