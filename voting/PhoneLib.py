import serial
import time
class Phone:
    def open(self ,com):
        self.ser = serial.Serial(com, 9600, timeout=5)
    def SetParameter(self):
        self.ser.write("AT\r".encode())
        time.sleep(1)
        d = "AT+CNMI=1,2,0,0,0\r"
        self.ser.write(d.encode())
        time.sleep(1)
    def ReadLine(self):
        data = self.ser.readline()
        return data.decode()
    def Dial(self,Number):
        self.ser.write("AT\r".encode())
        time.sleep(1)
        d="ATD{};\r".format(Number)
        self.ser.write(d.encode())
        time.sleep(1)
    def Sms(self,Number,Msg):
        self.ser.write("AT\r".encode())
        time.sleep(1)
        d="AT+CMGF=1\r"
        self.ser.write(d.encode())
        time.sleep(1)
        d = "AT+CMGS=\"{}\"\r".format(Number)
        self.ser.write(d.encode())
        time.sleep(1)
        d = "{}{}\r".format(Msg,chr(26))
        self.ser.write(d.encode())
        time.sleep(1)

    def close(self):
        self.ser.close()
''' 
P=Phone()
P.open('COM6')

n=input("Enter Mobile No:")
#P.Dial(n)
msg=input("Enter Msg:")
P.Sms(n,msg)

P.SetParameter()
while True:
   data=P.ReadLine()
   if(data.startswith("+CMT")):
    i=data.index(' ');
    L=data[i+1:].split('\"')

    print(L)
    msg=P.ReadLine()
    print(msg)

   time.sleep(0.5)



input()
'''








