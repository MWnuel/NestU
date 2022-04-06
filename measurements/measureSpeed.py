from .models import Measurements, Server
import datetime,pytz
import time
import speedtest

def measure_speed():
    speed = speedtest.Speedtest()
    best_server = speed.get_best_server()
    download = speed.download()/1000000
    upload = speed.upload()/1000000
    latency = 0

    server = Server(url=best_server["url"], lat=best_server["lat"], lon=best_server["lon"], city=best_server["name"], country=best_server["country"], cc=best_server["cc"], sponsor=best_server["sponsor"], id=best_server["id"], host=best_server["host"], download=best_server["d"], latency=best_server["latency"])
    measurement = Measurements(download=download, upload=upload, latency=best_server["latency"], test_time=datetime.datetime.now(), server_id=best_server["id"])
    server.save()

    measurement.save()
