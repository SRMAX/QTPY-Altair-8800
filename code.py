import time
import board
import digitalio
import random
import adafruit_debouncer
import asyncio

def binary_counter(leds, num_leds):
    counter = 0
    while True:
        for led in leds:
            led.value = (counter & (1 << leds.index(led))) > 0
        counter += 1
        if counter == 2**num_leds:
            counter = 0
        time.sleep(0.5)
        print("counter: ", counter)
        if counter == 0:
            break
    print("Exiting binary counter")
        
async def random_lights(leds,dly):
    print("Entering random function")
    for sty in leds:
        led = random.choice(leds)
        led.value = not led.value
        await asyncio.sleep(dly)
    print("Exiting random function")

async def main():
    dly = .2
    task = asyncio.create_task(random_lights(leds,dly))
    await asyncio.gather(task)  # Don't forget "await"!

leds = [digitalio.DigitalInOut(x) for x in [board.A0, board.A1, board.A2, board.A3, board.SDA, board.SCL]]
num_leds = len(leds)
toggle_switch = digitalio.DigitalInOut(board.SCK)
toggle_switch.direction = digitalio.Direction.INPUT
toggle_switch.pull = digitalio.Pull.UP
prev_switch = toggle_switch.value
switch_state = "counter"
print("toggle_switch.value: ", toggle_switch.value)
for led in leds:
    led.direction = digitalio.Direction.OUTPUT

binary_counter(leds, num_leds)
print("Entering Loop ")


while True:
    print("switch state:",switch_state)
    print("toggle_switch.value: ", toggle_switch.value)
    if toggle_switch.value == False:
            switch_state = "random"
            print("Entered random")
            asyncio.run(main())
    else:
        print("Entered counter")
        print("toggle_switch.value: ", toggle_switch.value)
        switch_state = "counter"
        #task.cancel()
        binary_counter(leds, num_leds)
    time.sleep(0.01)
