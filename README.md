# RFID Game

This idea was inspired by a game I played with my daughter at one of kid activity locations.

[![Project Progress](https://img.youtube.com/vi/P0Ajofy28nk/0.jpg)](https://www.youtube.com/playlist?list=PLG5BY3dIqtTkJbyAdYW9bXMz5kSC7FsTJ)

- [RFID Game](#rfid-game)
  - [Hardware](#hardware)
    - [Prototype](#prototype)
    - [Plan for final assembly](#plan-for-final-assembly)
    - [Possible expansions](#possible-expansions)
  - [Setup](#setup)
    - [Pin connections](#pin-connections)

## Hardware

### Prototype

> See [img/progress](./img/progress) folder for pics from different stages of prototype.

For prototyping I used:

- [RP2040-zero ripoff from AliExpress](https://s.click.aliexpress.com/e/_DFgT0A3)
- [MINI RC522 RFID module from AliExpress](https://s.click.aliexpress.com/e/_DDcbgXb)
- [extra RFID tags](https://s.click.aliexpress.com/e/_DdyIhdj)
- [SSD1306 OLED display](https://s.click.aliexpress.com/e/_DdGpOTj)
- [400pin breadboard](https://s.click.aliexpress.com/e/_Dd8Wwep)
- [Jumper Wires](https://s.click.aliexpress.com/e/_DmMPHxt)

### Plan for final assembly

I plan on putting all of that in a small electrical junction box.  
I would like to power it with two 18650 batteries (or other 5V+ battery) via step down DC converter.  
I also plan on exposing charging port.

### Possible expansions

Other thoughts for improvements I have:

- bigger and maybe color display
- speaker (via amplifier module)
- joystick (to select game modes)
- DIP switch for writing data to tags

## Setup

> See [img/progress](./img/progress) folder for pics from different stages of prototype.
>
> Or head to [YouTube](https://www.youtube.com/playlist?list=PLG5BY3dIqtTkJbyAdYW9bXMz5kSC7FsTJ) playlist for video progress.

Code in [src](./src/) folder heavily relies on `mfrc522.py` from [THIS](https://how2electronics.com/using-rc522-rfid-reader-module-with-raspberry-pi-pico/) page.  
`main.py` is (will be) a combination of both `read.py` and `write.py` from that very same page.

I'm using `ssd1306.py` from [THIS](https://www.hackster.io/diyprojectslab/how-to-use-an-oled-display-with-raspberry-pi-pico-d9d9cb) page, mostly because I wasn't able to track down the original author.  

> If you know the authors of both `mfrc522.py` and `ssd1306.py` please let me know so I can update link!  

### Pin connections

| RC522 | SPI0 | SPI1 |
|-------|------|------|
| SDA   | GP5  | GP9  |
| SCK   | GP6  | GP10 |
| MOSI  | GP7  | GP11 |
| MISO  | GP4  | GP8  |
| IRQ   | ---  | ---  |
| GND   | GND  | GND  |
| RST   | GP26 | GP27 |
| 3v3   | 3v3  | 3V3  |

| SSD1306 | I2C |
|---------|-----|
| SDA     | GP0 |
| SCL     | GP1 |
| 5V      | 5V  |
| GND     | GND |
