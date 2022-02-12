from smbus2 import SMBus
from mlx90614 import MLX90614
import time
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
#print(dir(sensor))
#exit(1)
while True:
    print("Ambient Temperature :", sensor.get_ambient())
    print("Object Temperature :", sensor.get_object_1())

    time.sleep(0.1)
bus.close()
