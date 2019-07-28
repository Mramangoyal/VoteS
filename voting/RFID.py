import serial
class RFID:
    def open(self):
        self.ser = serial.Serial('COM13', 9600, timeout=5)

    def ReadLine(self):
        data = self.ser.read(12)
        print(data.decode(), end='\n')

    def close(self):
        self.ser.close()

h = RFID()
h.open()

h.ReadLine()

input()
h.close()