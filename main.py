import serial
import hr
import spo2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Edit the variables below to the correct settings    
COMPORT = 'COM3'
BAUDRATE = 9600
MAX_POINTS = 100

connection = serial.Serial(COMPORT, BAUDRATE, timeout=0.1)   

# Initilize values with fixed size
x_values = list(range(MAX_POINTS))
spo2_values = deque([0.0] * MAX_POINTS, maxlen=MAX_POINTS)
hr_values = deque([0.0] * MAX_POINTS, maxlen=MAX_POINTS) 

def read_serial():    
    # Read 25 samples (1 second)
    lines = []
    for _ in range(25):
        raw_line = connection.readline()

        # Ensures the data exists and skips if there is an error
        if raw_line:
            try:
                decoded = raw_line.decode("utf-8").strip()

                if decoded:  
                    lines.append(decoded)

            except UnicodeDecodeError:
                pass 

    return lines 


def update(frame):   
    data = read_serial()

    # Ensures the data exists
    if data:
        heart_rate = hr.calculate_hr(data)
        spoxygen = spo2.calculate_spo2(data)

        # Add current values into data list 
        spo2_values.append(spoxygen)
        hr_values.append(heart_rate)

    # Inject the updated queue directly into the plot line
    spo2_line.set_ydata(list(spo2_values))
    hr_line.set_ydata(list(hr_values))
    
    return spo2_line, hr_line,

# Create and display graph
fig, ax = plt.subplots()
ax.set_xlim(0, MAX_POINTS - 1)
ax.set_ylim(-0, 200)  # Adjust this to match your expected Y data range

# Create a blank line plot to update dynamically
spo2_line, = ax.plot(x_values, list(spo2_values), color="tab:blue", lw=2, label='SPO2')
hr_line, = ax.plot(x_values, list(hr_values), color="tab:green", lw=2, label='Heart Rate')

ax.set_title("SPO2 and HR Live Visual")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="upper left")

ani = animation.FuncAnimation(
    fig, update, interval=1000, blit=True, cache_frame_data=False
)

plt.show()
