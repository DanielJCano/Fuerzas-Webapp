from machine import ADC, Pin
import time
import socket
import network

ADC_PIN = ADC(Pin(35))      # create ADC object

HOST = "192.168.1.100"
PORT = 5000

routercon = network.WLAN(network.STA_IF)
routercon.active()
routercon.active(True)
routercon.connect('MERCUSYS_933A')
#routercon.connect('INNOVATIVENET1', 'I28nXWertY3322116')     # (SSID , password)
routercon.ifconfig()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
test_time = 0
while True:
    adc_read = f"{str(ADC_PIN.read())}"
    print("adc = ", adc_read)    # Read ADC value
    server.send(adc_read.encode())
    test_time += 1
    time.sleep(0.5)

server.close()


