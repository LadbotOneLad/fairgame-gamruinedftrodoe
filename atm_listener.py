import serial
import time

# Note: In Termux, USB-serial devices usually map to /dev/ttyUSB0 or /dev/ttyACM0
# You may need to grant Termux USB permissions or run with root if required by your Android ROM.
SERIAL_PORT = '/dev/ttyUSB0' 
BAUD_RATE = 115200

print("🚀 Starting Termux ATM Monitor...")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Allow connection to settle
    print(f"Connected to ESP32 on {SERIAL_PORT}")

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"[ESP32]: {line}")
            
            # Look for the pulse flag from the previous Arduino script
            if "DEPOSIT DETECTED!" in line:
                print("💰 Termux verified deposit event! Launching game task...")
                # EXECUTE YOUR TERMUX / ANDROID GAME COMMAND HERE
                
except KeyboardInterrupt:
    print("\nStopping Monitor.")
except Exception as e:
    print(f"Error: {e}")
