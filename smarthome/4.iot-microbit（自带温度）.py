from microbit import *
import Obloq

IP="192.168.0.103"
PORT="8080"
SSID="jys16f"
PASSWORD="zjjys.16"

uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=pin2, rx=pin1)

while Obloq.connectWifi(SSID,PASSWORD,10000) != True:
  display.show(".")

display.scroll(Obloq.ifconfig())
Obloq.httpSet(IP,PORT) 

while True:
    
  errno,resp=Obloq.get("input?id=1&val="+str(temperature()),10000) 
  if errno == 200:
    display.scroll(resp)
  else:
    display.scroll(str(errno))
  sleep(1000*5)