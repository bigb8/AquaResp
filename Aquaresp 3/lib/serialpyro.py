import serial as ser
import time


ser = ser.Serial('COM3', 115200, timeout=5)
# ser.write("#LOGO\r".encode())
# ser.write("#IDNR\r".encode())
# ser.write("#BAUD\r".encode())
# ser.write("#BAUD\r".encode())
ser.write("MEA 1 1\r".encode())
time.sleep(1)
response =  ser.readline()
sr = [i for i in response.decode().split(' ')]
print(sr)
status, dphi, umolar, mbar, airSat, tempSample, tempCase, signalIntensity, ambientLight, pressure, humidity,resistorTemp, percentO2, tempOptical, pH, ldev = sr[:16]

print(response)
print(airSat/1000.0)
ser.close()
