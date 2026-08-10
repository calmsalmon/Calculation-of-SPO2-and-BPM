import pandas as pd

def calculate_ac_dc(data):
    # DC (average of signal)
    dc = data.mean()

    # AC
    ac = data - dc

    return ac, dc


# calculate SPO2
def calculate_spo2(data):
    df = pd.DataFrame(data).astype(float)
    df.columns = ['green', 'ir', 'red', 'ambient']

    df['red'] = df['red'] - df['ambient']
    df['ir'] = df['ir'] - df['ambient']

    ac_red, dc_red = calculate_ac_dc(df['red'])
    ac_infrared, dc_infrared = calculate_ac_dc(df['ir'])

    ratio_of_ratios = (ac_red / dc_red) / (ac_infrared / dc_infrared)

    spo2 = 110 - 25 * ratio_of_ratios

    return spo2
