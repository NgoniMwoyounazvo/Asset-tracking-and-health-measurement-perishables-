import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for reading the DO output
DO_PIN = 7  # Replace with the actual GPIO pin number
GPIO.setup(DO_PIN, GPIO.IN)

try:
    while True:
        # Read the state of the DO pin
        smoke_detected = GPIO.input(DO_PIN)

        # Determine if smoke is detected or not
        if smoke_detected == GPIO.LOW:
            smoke_state = "Smoke Detected"
        else:
            smoke_state = "No Smoke"

        # Print the smoke state
        print(f"Smoke State: {smoke_state}")

        time.sleep(5.0)  # Wait for a short period before reading again

except KeyboardInterrupt:
    print("Smoke detection stopped by user")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
