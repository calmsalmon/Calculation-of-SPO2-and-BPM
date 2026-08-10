import serial
import hr
import spo2

def read_serial():
    # Edit the variables below to the correct settings    
    comport = 'COM3'
    baudrate = 9600

    connection = serial.Serial(comport, baudrate, timeout=0.1)         

    # Read 25 samples (1 second)
    lines = []
    for _ in range(25):
        raw_line = connection.readline()
        lines.append(raw_line.decode().strip())

    return lines 

while True:
    data = read_serial()

    heart_rate = hr.calculate_hr(data)
    spoxygen = spo2.calculate_spo2(data)

    # To add visualization