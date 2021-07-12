import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))


ser = serial.Serial("COM2", 9600)
print(ser.readline())
res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
     cc=str(1234)
     print(cc)
     val=cc
     firebase1 = firebase.FirebaseApplication('https://landslide-prediction-70872-default-rtdb.firebaseio.com/', None)
     
     for i in range(0,4):
             #string1="123"
             string1=str(ser.readline())
             string1=string1[9:][:-6]
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://landslide-prediction-70872-default-rtdb.firebaseio.com/'+ str(i), data)
             print(result)
     

     for i in range(0,4):
             #string2="123"
             string1=str(ser.readline())
             string1=string1[9:][:-6]
             data1 =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string2,
               'time': datetime.now().strftime("%H:%M")               
          }
             result1 = firebase1.patch('https://landslide-prediction-70872-default-rtdb.firebaseio.com/'+ str(i), data1)
             print(result1)
     res=0

