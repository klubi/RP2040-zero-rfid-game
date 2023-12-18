import utime
from machine import Pin, I2C
from mfrc522 import MFRC522
from ssd1306 import SSD1306_I2C


i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
oled = SSD1306_I2C(128, 32, i2c)

reader1 = MFRC522(spi_id=0, sck=6, miso=4, mosi=7, cs=5, rst=26)
reader2 = MFRC522(spi_id=1, sck=10, miso=8, mosi=11, cs=9, rst=27)


global_one = ""
global_two = ""


def display(line1="", line2=""):
    global global_one
    global global_two
    global_one = global_one if line1 == "" else line1
    one = line1 if line1 != "" else global_one
    global_two = global_two if line2 == "" else line2
    two = line2 if line2 != "" else global_two
    oled.fill(0)
    oled.text("1: {}".format(one), 0, 0)
    oled.text("2: {}".format(two), 0, 17)
    oled.show()


def read_reader(reader):
    reader.init()
    hexId = ""
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            hexId = hex(int.from_bytes(bytes(uid), "little", False)).upper()
            print("Card detected {}  uid={}".format(hexId, reader.tohexstring(uid)))
    return hexId


try:
    display()

    print("\nPlease place card on reader\n")

    while True:

        hexId = read_reader(reader1)
        display(line1=hexId)
        hexId = read_reader(reader2)
        display(line2=hexId)

        utime.sleep_ms(50)

except KeyboardInterrupt:
    pass
