import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for reading the DO output
DO_PIN = 7  # Replace with the actual GPIO pin number
GPIO.setup(DO_PIN, GPIO.IN)

ETHYLENE_THRESHOLD = GPIO.LOW  # Replace with the actual threshold level for Ethylene gas

try:
    while True:
        # Read the state of the DO pin
        gas_present = GPIO.input(DO_PIN)

        # Determine if Ethylene gas is present or not based on the threshold
        if gas_present == ETHYLENE_THRESHOLD:
            gas_state = "Ethylene Gas Present"
        else:
            gas_state = "No Ethylene Gas"

        # Print the gas state
        print(f"Gas State: {gas_state}")

        time.sleep(5.0)  # Wait for a short period before reading again

except KeyboardInterrupt:
    print("Gas detection stopped by user")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
