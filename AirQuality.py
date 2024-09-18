import network
import time
import urequests
from machine import Pin
from neopixel import Neopixel

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
pixels = Neopixel(8, 0, 16, "GRB")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("SSID", "PASSWORD")
time.sleep(5)
print(wlan.isconnected())
if wlan.isconnected() == True:
    for i in range(10):
        pixels.fill((0, 64, 0))
        pixels.show()
        time.sleep(0.1)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.1)
else:
        for i in range(10):
            pixels.fill((64, 0, 0))
            pixels.show()
            time.sleep(0.1)
            pixels.fill((0, 0 , 0))
            pixels.show()
            time.sleep(0.1)
while True:
    if button.value():
        aq = urequests.get("http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat=40.714272&lon=-74.005966&appid=YOUR API KEY HERE").json()
        air_quality_index = aq['list'][0]['main']['aqi']
        print("The Air Quality index is: ",str(air_quality_index))
        if air_quality_index == 1:
            for i in range(10):
                pixels.fill((0, 64, 0))
                pixels.show()
                time.sleep(0.5)
                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(0.5)
        elif air_quality_index == 2:
            for i in range(10):
                pixels.fill((51,255,255))
                pixels.show()
                time.sleep(0.5)
                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(0.5)
        elif air_quality_index == 3:
            for i in range(10):
                pixels.fill((153, 51, 255))
                pixels.show()
                time.sleep(0.5)
                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(0.5)
        elif air_quality_index == 4:
            for i in range(10):
                pixels.fill((255,153,51))
                pixels.show()
                time.sleep(0.5)
                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(0.5)
        elif air_quality_index == 5:
            for i in range(10):
                pixels.fill((255, 0, 0))
                pixels.show()
                time.sleep(0.5)
                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(0.5)
        else:
            pass
