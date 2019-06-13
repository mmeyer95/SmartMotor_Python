# SmartMotor Control in Python

In order to control a SmartMotor with Python, you must be able to open a serial port, then write to and read from it.
Then, commands are the same as those used in SMI, as outlined in the [Developer's Guide.](https://www.animatics.com/downloads/top%20level/4.%20Manuals/c.%20Programming%20Information%20and%20Command%20Reference/SmartMotor%20Developers%20Guide.pdf) 

Some necessary part of the code:

1. Import serial library ["Import serial"]
2. Open serial port ["ser = serial.Serial(port ='COM3', 
                    baudrate = 9600, 
                    parity = serial.PARITY_NONE, 
                    stopbits = serial.STOPBITS_ONE, 
                    bytesize = serial.EIGHTBITS,timeout=1)"]
3. Define the message to send, either in hex code, or byte [b'message ']
4. Send the message ["ser.write(message)"]
5. Read back the response ["line = ser.readline()" or "resp = ser.read(x)" where x is the # of bytes]
6. Close the serial port ["ser.close()"]

Because SmartMotors use a carriage return (\r) as a terminating character, readline() must be used wih a timeout. Otherwise, the program will wait forever for a new line character (\n).

To leave out the terminating character from the return message, you can use: "line = line[0:len(line)-1]"

Outgoing messages must be terminated with either "\r" or a space.
