import time
import board
import adafruit_dht
from datetime import datetime

# Initializing the DHT device, with the data pin it is connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)

# Creating or opening the CSV file for writing the collected data
with open('temperature_and_humidity_log.csv', 'a') as file, open('error_log.txt', 'a') as error_file:
    # Check if the file is empty, and if so, write the header
    if file.tell() == 0:
        file.write("Timestamp;Temperature (°C);Humidity (%)\n")
    
    while True:
        try:
            # Assigning variable names
            temperature = dhtDevice.temperature
            humidity = dhtDevice.humidity

            # Checking if the readings are valid (sometimes DHT sensors may return None)
            if temperature is not None and humidity is not None:
                # Getting the current timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Printing the values with timestamp
                print("{}; Temperature: {}°C; Humidity: {}%".format(timestamp, temperature, humidity))

                # Writing the data to the CSV file namely "temperature_and_humidity_log.csv"
                file.write("{};{}°C;{}%\n".format(timestamp, temperature, humidity))
                file.flush()  # Flush the buffer to ensure data is written immediately
        #if the returned output or error does not fall in any category
        except RuntimeError as error:
            # Log the error to a error_log.txt file
            error_message = "{} - Error reading sensor data: {}\n".format(datetime.now(), error)
            error_file.write(error_message)
            error_file.flush()
            continue

        # Allow delays between the recording of the data
        time.sleep(10.0)