import serial
import time
radio = serial.Serial(port='COM7', baudrate=57600)#.01, timeout=5

while True:
    # radio.write(f'{time.time()}\n'.encode())
    radio.write(bytes('hello cooper', 'utf-8'))#bytes(data, 'utf-8')
    # print(time.time())
    time.sleep(1)