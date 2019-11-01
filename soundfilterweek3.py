# Pseudocode/skeleton code for portion that reduces background noise

# importing necessary libraries
import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write  
from scipy import signal

# import below library for plotting
import matplotlib.pyplot as pt

# insert input wav file below
(freq, arr) = read('')

# plotting original audio
pt.plot(array) 
pt.title('Original Audio')
pt.xlabel('Frequency')
pt.ylabel('Amplitude')

fft = sp.fft(arr)

# do something with Gaussian
# make new sound

output = array # tentative

#writing to output file
write ("", freq, output)
