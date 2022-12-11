from machine import ADC, Pin
import time
import socket
import network

TC_PIN = ADC(Pin(35))       # Pin Tencion y Compresion
DESP_PIN = ADC(Pin(34))     # Pin Desplazamiento
SIGN_PIN = ADC(Pin(32))       # Pin de Signo
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
while True:
    if SIGN_PIN.read() > 2000:
        TC_PIN_R = f'-{str(TC_PIN.read())}'
    else:
        TC_PIN_R = str(TC_PIN.read())
    DESP_PIN_R = str(DESP_PIN.read())
    adc_read = f"{TC_PIN_R} {DESP_PIN_R}"
    server.send(adc_read.encode())
    print(f"TC ADC = {TC_PIN_R} | Desp ADC = {DESP_PIN_R}")    # Read ADC value
    time.sleep(2)

server.close()


