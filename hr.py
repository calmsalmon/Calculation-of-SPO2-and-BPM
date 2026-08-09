import pandas as pd
import numpy as np
from scipy.signal import find_peaks, detrend

def calculate_hr(green_csv):
    df = pd.read_csv(green_csv, 
                     skiprows=1,
                     header=None)
    df.columns = ['green']

    # Remove dips
    df = df[df["green"] > 70000].reset_index(drop=True)

    # Remove baseline from signal
    df['green'] = detrend(df["green"])

    peaks, properties = find_peaks(df['green'], height=-70000, distance=10)
    
    # Calculate bpm based on distance between 2 beats 
    peak_difference = np.diff(peaks)
    bpm = 60 / (peak_difference / 25)
    
    return bpm

calculate_hr('C:\\Users\\John Doe\\Desktop\\biophotonics-data-processing\\data\\green.csv')

