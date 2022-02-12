from prometheus_client import Gauge, start_http_server
import time

g = Gauge('sensor_temp', 'Sensor temprature')

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        g.inc()
        time.sleep(1)