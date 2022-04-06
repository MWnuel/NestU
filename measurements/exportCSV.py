from django.utils.encoding import smart_str
import csv
from django.http import HttpResponse
from .models import Measurements

def export_csv():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="SpeedExport.csv"'

    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    # write the headers
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Download"),
        smart_str(u"Upload"),
        smart_str(u"Latency"),
        smart_str(u"Time"),
    ])

    measurements = Measurements.objects.all().values("upload", "download", "latency", "test_time")
    counter = 0
    for measurement in measurements:
        print(measurement)
        counter+=1
        writer.writerow([
            smart_str(counter),
            smart_str(measurement["download"]),
            smart_str(measurement["upload"]),
            smart_str(measurement["latency"]),
            smart_str(measurement["test_time"]),
        ])
    return response
