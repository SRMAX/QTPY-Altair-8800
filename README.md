# QTPY-Altair-8800-
A circuitpython project to create a miniature replica of the Altair 8800 computer using an Adafruit QYPY ESP32-S3.

Before the Apple and IBM PCs made microcomputers household names their was the Altair 8800. It was a microcomputer designed in 1974 by MITS and based on the Intel 8080 CPU. Interest grew quickly after it was featured on the cover of the January 1975 issue of Popular Electronics and was sold by mail order through advertisements. In wanting to bring back memories of wanting one of these I wanted to create a miniature of these for my office. I found a Raspberry Pi 3 case on Thingverse by Rabbit Engineering that would work for what I wanted with little modification. I wanted it to at least look functional by having leds light up and have switches to change the led sequences and add additional functionallity in the future.

I chose to use an Adafruit QTPY ESP32-S3, but it is overkill for this in the initial stage 1 form. I plan to add a temperature, humidity, preasure, and VOC sensor next.

The case can hold 12 leds and 6 switches. The QTPY is limited pins so I chose to use six GPIO pins each feeding two colored leds prewired with resistors to keep the board as simple as possible. The remaining 5 GPIO pins are wired through mini-switches to ground. The sixth switch in currently unused. Later this pin will be used to switch on battery power to make this board very portable.

The initial code allows you to blink the two sets of six leds in a count down counter or an asyncronous random pattern depending on the state of the switch connected to the SCK pin of the QTPY. Later versions will add diffent patterns and an all on test.

Hardware:

1 - QTPY ESP32-S3
1 - USBC cable
1 - ElectroCookie Prototype board (1/4 board)
2 - 8pin headers
12 - 3mm colored leds
12 - Mini SPST switches prewired
1 - 3D printed case base (See STL files)
1 - 3D printed case top (See STL files)
1 - 3D printed case front panel (See STL files)
1 - PDF of the front face of the Altair 8800
1 - Glue Stick and Super Glue
1 - Hot Glue and gun
1 - Small screw or bolt to attach top to case

Software:

Circuitpython 8.0.0 and associated libraries (See code files)

Installaton:

1. Print 3D parts.
2. Solder headers to prtotype board
3. Run a wire from the positive bus of the prototype board to the 3v pin on the QTPY.
4. Run a wire from the ground bus of the prototype board to the grd pin of the QTPY.
5. Connect two leds to each of the following A0, A1, A2, A3, SDA, SCL. (Use of different colors is your preference.)
6. Connect one switch to each of the following SCK, RX, MISO, MOSI, TX (NOTE: As the case gets quite crowded you should keep wires as short as possible.
7. Install the leds into the upper portion of the front face of the case. (If you want to see the counter count down then put them in the order they were wired left to right. I did the bottom left to right ant the top right to left.)
8. Glue a printout of the faceplate to the faceplate then cutout the holes for the switches.
9. Install the switches to the faceplate in the order above left to right with the last switch being the one not currently wired.
10. Insert the faceplate into the bottom of the case lifting the bottom of the faceplate over the two side tabs so the faceplate comes out the front of the case.
11. With the faceplate out the front of the case put a small amount of super glue on the two side tabs and slide the faceplate back towards the tabs and into the case so as to make good contact with the tabs. Hold in place till the glue sets. The faceplate should be inset from the front of the case about an 1/8th inch and be square.
12. Attach the board to the stands on the bottom rear of the case so as the usb connector is facing the rear. Attachment method is your preference. I use hot glue. 
13. Place top on case and, if desired, use a screw or bolt to secure it.



References:

The QTPY ESP32-S3 https://www.adafruit.com/5426

Original thingverse files from by Rabbit Engineeringhttps://www.thingiverse.com/thing:3784996

ElectroCookie Prototype board https://www.amazon.com/gp/product/B08151V9TS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1

Colored 3v-5v LEDs prewired https://www.amazon.com/dp/B07X437PVW?psc=1&ref=ppx_yo2ov_dt_b_product_details

Mini switches prewired https://www.amazon.com/dp/B08MZRB4T1?ref=ppx_yo2ov_dt_b_product_details&th=1
