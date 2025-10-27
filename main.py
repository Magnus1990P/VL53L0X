import time
from machine import Pin, I2C
import VL53L0X

sdaPIN=Pin(14)
sclPIN=Pin(15)
i2c_bus = I2C(0, sda=sdaPIN, scl=sclPIN, freq=10000)
time.sleep(0.1)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c_bus)

tof.set_Vcsel_pulse_period(VL53L0X.PRE_RANGE_TYPE, 12)
tof.set_Vcsel_pulse_period(VL53L0X.FINAL_RANGE_TYPE, 14)


while True:
# Start ranging
    tof.start()
    distance = tof.read()
    print(distance)
    tof.stop()