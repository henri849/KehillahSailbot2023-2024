import serial
import time
radio = serial.Serial(port='COM7', baudrate=57600, timeout=5)#.01, timeout=5

while True:
    image_data = radio.readline(300)
    time.sleep(0.1)