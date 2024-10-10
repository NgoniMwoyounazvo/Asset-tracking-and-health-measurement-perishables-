import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import csv

# Suppress warnings
GPIO.setwarnings(False)

rfid = SimpleMFRC522()
read_ids = set()
seen_before = set()

unique_csv_file = 'unique_tags.csv'
duplicate_csv_file = 'duplicate_tags.csv'

# Open CSV files in write mode and write header
with open(unique_csv_file, mode='w', newline='') as unique_csv:
    unique_writer = csv.writer(unique_csv)
    unique_writer.writerow(['ID', 'Text'])

with open(duplicate_csv_file, mode='w', newline='') as duplicate_csv:
    duplicate_writer = csv.writer(duplicate_csv)
    duplicate_writer.writerow(['ID', 'Text'])

while True:
    id, text = rfid.read()
    
    # Check if the ID is not in the set, then print and add it to the set
    if id not in read_ids:
        print("New RFID Tag Detected:")
        print("ID:", id)
        print("Text:", text)

        # Write data to the unique CSV file
        with open(unique_csv_file, mode='a', newline='') as unique_csv:
            unique_writer = csv.writer(unique_csv)
            unique_writer.writerow([id, text])
        
        read_ids.add(id)
        seen_before.discard(id)  # Remove from seen_before if it was there before
    else:
        if id not in seen_before:
            print("Duplicate RFID Tag Detected. Ignoring.")
            seen_before.add(id)