import serial
import time
from datetime import datetime

# Set up the serial line
ser = serial.Serial('COM11', 9600)  # Change 'COM3' to the correct port for your Arduino
time.sleep(2)  # Wait for the serial connection to initialize

num_channels = 4

# Function to get the current time formatted as a string for the filename
def get_current_time_str():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Function to create a new file with the current timestamp in the filename
def create_new_file():
    filename = f'voltage_data_{get_current_time_str()}.txt'
    file = open(filename, 'w')
    # Write the header row
    file.write("Date\tMonth\tYear\tHour\tMinute\tSecond" + "".join([f"\tVoltage{i+1}"for i in range(num_channels)]) + "\n")
    return file

# Initial file creation
file = create_new_file()
start_time = datetime.now()

try:
    while True:
        # Read the voltage data from the serial port
        line = ser.readline().decode('utf-8').strip()
        voltages = line.split('\t')
        
        # Get the current time
        current_time = datetime.now()
        date = current_time.day
        month = current_time.month
        year = current_time.year
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        
        # Write the data to the file in columnar format
        data = f"{date}\t{month}\t{year}\t{hour}\t{minute}\t{second}"+ "".join([f"\t{voltage}"for voltage in voltages]) + "\n\n"
        file.write(data)

        print(data.strip())
           
        # Check if an hour has passed
        if (hour-start_time.hour>=1 ):
            # Close the current file
            file.close()
            # Create a new file
            file = create_new_file()
            # Update the start time
            start_time = current_time
    
        
        # Sleep for 1 second before reading again
        time.sleep(1)

except KeyboardInterrupt:
    print("Data collection stopped.")

finally:
    # Ensure the file is closed when the script is interrupted
    file.close()
    # Close the serial port
    ser.close()
