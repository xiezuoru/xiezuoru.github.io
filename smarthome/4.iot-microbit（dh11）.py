from microbit import *
import Obloq
import dht11
#DH11接在pin16

IP="192.168.43.184"
PORT="8080"
SSID="jf"
PASSWORD="20040404"

uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=pin2, rx=pin1)

while Obloq.connectWifi(SSID,PASSWORD,10000) != True:
  display.show(".")

display.scroll(Obloq.ifconfig())
Obloq.httpSet(IP,PORT) 

while True:
  temp,hum=dht11.read(16)
  errno,resp=Obloq.get("input?id=1&val="+str(temp),10000) 
  if errno == 200:
    display.scroll(resp)
  else:
    display.scroll(str(errno))
  sleep(1000*5)