from sense_hat import SenseHat
from gpiozero import CPUTemperature
from time import sleep

cpu = CPUTemperature()
sense = SenseHat()

## Make the text scroll with the temperature
#while (true):
#    temperature = "%3.2f" % cpu.temperature
#    sense.show_message(temperature)
##


## Make the leds to have coloured levels
level1=(0,255,0)
level2=(0,255,255) 
level3=(0,0,255) 
level4=(255,255,0) 
level5=(255,0,0)

while 1:
    level = level1
    if (cpu.temperature >= 53):
        level = level2
        print("level2")
    if (cpu.temperature >= 57):
        level = level3
        print("level3")
    if (cpu.temperature >= 63):
        level = level4
        print("level4")
    if (cpu.temperature >= 70):
        level = level5
        print("level5")
    
    print(cpu.temperature)
    
    sense.clear(level)
    sleep(0.5)
    
