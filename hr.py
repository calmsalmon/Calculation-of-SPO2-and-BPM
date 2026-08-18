import pandas as pd
import numpy as np
from scipy.signal import find_peaks, detrend

def calculate_hr(data, hr_tail):
    df = pd.Dataframe(data).astype(float)
    df.columns = ['times', 'green', 'red', 'ir', 'ambient']

    # Remove dips
    df = df[df["green"] > 70000].reset_index(drop=True)

    # Remove baseline from signal
    df['green'] = detrend(df["green"])

    peaks, properties = find_peaks(df['green'], height=-70000, distance=10)
    
    # Calculate bpm based on distance between 2 beats 
    peak_difference = np.diff(peaks)
    bpm = 60 / (peak_difference / 25)

    if hr_tail[0] != None:
        tail = tail[0]

        # Calculate the difference between the last peak of the last sample
        # and the first peak of the current sample
        first_difference = tail + peaks[0]

        # Calculate bpm for first peak
        first_bpm = 60 / (first_difference / 25)
        bpm = np.concatenate([first_bpm], bpm)

    # Get tail for next sample
    tail = len(df) - peaks[-1]
    
    return bpm, tail
