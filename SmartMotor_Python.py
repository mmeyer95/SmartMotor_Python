'''Python program to communicate with SmartMotor
Meredith Meyer
6/12/2019

Import serial library'''
import serial
import time

print("PROGRAM START.")

'''Define & open serial port COM3 -- Changes based on PC'''
ser = serial.Serial(port ='COM3', 
                    baudrate = 9600, 
                    parity = serial.PARITY_NONE, 
                    stopbits = serial.STOPBITS_ONE, 
                    bytesize = serial.EIGHTBITS,timeout=1
)

'''You can write messages in hex code directly 
with the serial.Serial.write() command'''
message = [0x52, 0x50, 0x41, 0x20] #RPA
ser.write(message)

'''And you can read back the responde with the serial.Serial.readline() command.
readline() must be used with a timeout, because SmartMotors use a \r character,
and readline() depends on \n to indicate the end of a line.'''
line = ser.readline() #read 8 bytes

if line!=None:
    print("Using readline(), Position= ",line)
else:
    print("No response received.")
    
'''Other commands can be sent over the serial port, such as motion commands'''
message = [0x50, 0x72, 0x54, 0x3D, 0x31, 0x30, 0x30, 0x30, 0x20] #PT=0 \n
ser.write(message)
message = [0x47, 0x20] #G \n
ser.write(message)

'''Alternatively, ASCII commands can be sent, and Python takes care of converting to bytes
with (b'string') '''
print("Waiting for move...")
time.sleep(10) #wait for move to finish
ser.flush() #clear the serial terminal
ser.write(b'RPA ') #RPA
'''Alternatively to reading lines, you can read back a certain # of bytes from the port.
You will notice the carriage return is no longer reported back with this command.
However, the \r character may then end up in the next line you read out.'''
print("Using read(), Position= ",ser.read(8))
print("The next line is: ",ser.readline())

'''Close the serial port-- if port is not closed, 
you may run into a permission error in Python the next time you run your program'''
ser.close() 
print("PROGRAM END.")
