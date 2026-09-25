import serial
import hr
import spo2
import pandas as pd
from collections import deque

# Edit the variables below to the correct settings    
COMPORT = 'COM3'
BAUDRATE = 9600
SAMPLING_RATE = 300

connection = serial.Serial(COMPORT, BAUDRATE, timeout=0.1)   

def read_serial():    
    # Read the # of samples equal to one second (the SAMPLING_RATE)
    lines = []
    for _ in range(SAMPLING_RATE):
        raw_line = connection.readline()

        # Ensures the data exists and skips if there is an error
        if raw_line:
            try:
                decoded = raw_line.decode("utf-8").strip()

                if decoded:  
                    pieces = decoded.split(',')
                    
                    lines.append(pieces)

            except UnicodeDecodeError:
                pass 

    return lines 

spo2_data = []
hr_data = []

tail = [None]

def update_data(tail):   
    data = read_serial()

    # Ensures the data exists
    if data:
        heart_rate, hr_tail = hr.calculate_hr(data, tail) 
        spoxygen = spo2.calculate_spo2(data)

        spo2_data.append(data)
        hr_data.append(data)

    tail[0] = hr_tail
    
    return hr_tail

# Record measurements for time(in seconds)
def record(time):
    for _ in range(time):
        update_data(tail)

    return spo2_data, hr_data

fspo2, fhr = record(60)

# Save files as csv
pd.Dataframe(fspo2).to_csv('device_data/spo2.csv')
pd.Dataframe(fspo2).to_csv('device_data/hr.csv')