import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import csv

GPIO.setwarnings(False)
rfid = SimpleMFRC522()

try:
    tracked_ids = {}  # Dictionary to store RFID tag IDs and their associated fruits

    while True:
        print("Select option for the fruit tracker you would like to register...")

        # Assuming 1 represents cards and 2 represents keychains
        rfid_type = input("Enter 1 for apple, 2 for banana, 3 for orange, 4 for lemon, 5 for lime, 6 for strawberry, 7 for blueberry, 8 for peach, 9 for plum, 10 for cherry, 11 for grape tracker: ")

        if rfid_type in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            break  # Exit the loop if the input is valid

        print("Invalid input. Please enter a number between 1 and 11.")

    fruits = {
        "1": "apples",
        "2": "bananas",
        "3": "oranges",
        "4": "lemons",
        "5": "limes",
        "6": "strawberries",
        "7": "blueberries",
        "8": "peaches",
        "9": "plums",
        "10": "cherries",
        "11": "grapes"
    }

    fruit_name = fruits[rfid_type]

    print(f"Waiting for {fruit_name} to be placed near tag reader...")
    rfid_id, _ = rfid.read()

    if rfid_id not in tracked_ids:
        tracked_ids[rfid_id] = fruit_name

        # Writing data to CSV file
        with open('fruit_tracker_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([rfid_id, fruit_name])
        
        print(f"Written data for tracker {rfid_type} ({fruit_name}) with RFID tag ID {rfid_id}")
    else:
        existing_fruit = tracked_ids[rfid_id]
        print(f"RFID tag ID {rfid_id} is already associated with {existing_fruit}. It cannot be recorded under a different fruit.")

finally:
    GPIO.cleanup()
