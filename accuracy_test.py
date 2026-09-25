import pandas as pd
import math

# Get Apple Watch data
file_name = 'NAME'
apple_watch_data = pd.read_csv('apple_watch_data/' + file_name)

# Get device data
spo2_data = pd.read_csv('device_data/spo2.csv')
hr_data = pd.read_csv('device_data/hr.csv')

spo2_diff = []
hr_diff = []

spo2_RMS = []
hr_RMS = []

# Calculate differences between measurements 
def get_difference():
    spo2_diff['diff'] = apple_watch_data['spo2'] - spo2_data['spo2']
    hr_diff['diff'] = apple_watch_data['hr'] - spo2_data['hr']

    spo2_diff['data'] = apple_watch_data['spo2']
    hr_diff['data'] = apple_watch_data['hr']

    return spo2_diff, hr_diff

# Calculate Abosulte Mean Squared Error
def calculate_accuracy():
    spo2_diff, hr_diff = get_difference()

    spo2_RMS['sqr'] = spo2_diff['diff'] * spo2_diff['diff']
    ### Turn csv into actual pyton list
    sum = spo2_RMS['sqr'].str.sum

    mean = sum / len(spo2_RMS['sqr'])
    spo2RMS = math.sqrt(mean)


    # Do same for heart rate
    hr_RMS['sqr'] = hr_diff['diff'] * hr_diff['diff']
    ### Turn csv into actual pyton list
    sum = hr_RMS['sqr'].str.sum

    mean = sum / len(hr_RMS['sqr'])
    hrRMS = math.sqrt(mean)

    return spo2RMS, hrRMS

RMS, hRMS = calculate_accuracy()

# Print results
print(f"The Root Mean Squared for SPO2 is: {RMS}")
print(f"The Root Mean Squared for Heart Rate is: {hRMS}")