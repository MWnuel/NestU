from django.apps import AppConfig
import os

class MeasurementsConfig(AppConfig):
    name = 'measurements'

    def ready(self):
        from . import jobs

        if os.environ.get('RUN_MAIN', None) != 'true':
            jobs.start_scheduler(30)