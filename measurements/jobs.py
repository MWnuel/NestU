from schedule import Scheduler
from . import measureSpeed
import threading
import time
from .models import Settings

def start_measure_speed():
    print("SPEEDTESTTIME")
    measureSpeed.measure_speed()

def start_scheduler(interval):
    #settings = list(Settings.objects.all().values("interval", "day", "fixedtime", "use_fixedtime"))[0]
    scheduler = Scheduler()
    #print(settings)
    #print(settings.get("interval"))
    scheduler.every(interval).minutes.do(start_measure_speed)

    scheduler.run_continuously()

def run_continuously(self, interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run

Scheduler.run_continuously = run_continuously