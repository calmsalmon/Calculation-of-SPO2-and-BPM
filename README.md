# Calculation of SPO2 and HR
A program which calculates peripheral blood oxygen saturation and beats per minute using photodiode data of green, red, infrared, and ambient light.


## Built with
The following libraries were used in Python:
- pandas
- serial
- scipy
- numpy


## Getting Started

### Prequisties
- Install all the libraries using the following command
  ```
  pp install -r requirements.txt
  ```
- Connect your Arduino to your computer and close both the Serial Monitor and Serial Plotter.

### Usage
Go onto main.py and run the program. Ensure that the COM port and baud rate is set correctly, otherwise the program will not work. Make sure your Arduino is also running a program that is sending photodiode data in the order: green, infrared, red, ambient. 
