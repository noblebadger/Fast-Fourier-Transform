# Fast-Fourier-Transform
A C++ Implementation of the Fast Fourier Transform. Written using the radix 2 Cooley and Tukey Aglorithm. Also includes graphing in python.

# file overview
+ fft.cpp : the main and only C++ file needed for the fast fourier transform
+ data.txt : contains the output of the last fft run
+ plot.py : python code to plot the contents of data.txt

# dependencies:
+ plot.py requires the 'matplotlib' for graphing
easy to obtain by pip:
	python -m pip matplotlib
or
	py -m pip matplotlib
+ (if using windows) must have the visual studio c++ tools

# compilation:
linux/mac:
	simply run: 
	g++ fft.cpp -o fft
windows:
	1. type 'C++' into desktop search bar e.g cortana for windows 10
	2. select 'Visual C++ [YEAR] [32/64 bit] Command prompt'
	(if this doesn't work try 'Developer command prompt for VS [YEAR]')
	3. navigate to the source code folder
	4. run:
	cl fft.cpp
	5. you should now have an fft.exe in the folder

# to run:
linux:
	./fft
windows:
	fft.exe

# to graph:
	python plot.py data.txt
or 
	py plot.py data.txt

TWEAKING:
The 'samples' variable in Main can be changed for a higher upper bound
sampling frequency; it must be size 2^n. The signal itself can also
be changed on line 165.
