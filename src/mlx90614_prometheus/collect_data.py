from prometheus_client import Gauge, start_http_server
from smbus2 import SMBus
from mlx90614 import MLX90614
import time

g = Gauge('sensor_temp', 'Sensor temperature', ['probe'])


def main():
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)

    while True:
        g.labels(probe='ambient').set(sensor.get_amb_temp())
        g.labels(probe='object').set(sensor.get_obj_temp())
        time.sleep(1)

    bus.close()


if __name__ == '__main__':
    main()
