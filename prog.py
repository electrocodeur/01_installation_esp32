import time
from machine import Pin

print("Test d'ElectroCodeur")
p2 = Pin(2,Pin.OUT)

while True:
  p2.on()
  time.sleep_ms(1000)
  p2.off()
  time.sleep_ms(1000)