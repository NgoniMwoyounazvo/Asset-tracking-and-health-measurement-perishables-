from gps import *
import time
from datetime import datetime

running = True

# Create or open the CSV file for writing the collected data
with open('gps_log.csv', 'a') as file, open('error_log.txt', 'a') as error_file:
    # Check if the file is empty, and if so, write the header
    if file.tell() == 0:
        file.write("Timestamp;Longitude;Latitude;Speed (km/h)\n")

    def get_position_data(gps, csv_file):
        nx = gps.next()

        if nx['class'] == 'TPV':
            # Extract GPS infos
            latitude = getattr(nx, 'lat', "Unknown")
            longitude = getattr(nx, 'lon', "Unknown")
            speed = getattr(nx, 'speed', "Unknown")

            # Store the current date/time
            dateTimeObj = datetime.now()
            timestamp = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
            
            print("{}; Latitude: {}; Altitude: {}".format(timestamp, latitude, altitude))


            # Write the data to the CSV file
            csv_file.write(f"{timestamp};{longitude};{latitude};{speed*3.6}\n")
            print(f"Data written to CSV: {timestamp}, lon={longitude}, lat={latitude}, speed={speed*3.6} km/h")

    # Tell gpsd we are ready to receive messages
    gpsd = gps(mode=WATCH_ENABLE | WATCH_NEWSTYLE)

    try:
        print("Application started!")
        while running:
            # Call the function to extract and append GPS data
            get_position_data(gpsd, file)
            # Delay the program for 1 second
            time.sleep(1)

    # If the user presses Ctrl+C, the program will stop running
    except KeyboardInterrupt:
        running = False

