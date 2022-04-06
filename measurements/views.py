from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Measurements, Server
from django.forms.models import model_to_dict
from . import measureSpeed
from . import exportCSV


def dashboard_view(request):
    if request.method == 'POST':
        if 'csv' in request.POST:
            return exportCSV.export_csv()
        elif 'speedtest' in request.POST:
            measureSpeed.measure_speed()

    measurements = Measurements.objects.select_related("server").values("upload", "download", "latency", "test_time",
                                                                        "server_id", "server__host")
    context = {"measurements": measurements}
    return render(request, 'dashboard.html', context)

def details_view(request):
    if request.method == 'POST':
        if 'csv' in request.POST:
            return exportCSV.export_csv()
        elif 'speedtest' in request.POST:
            measureSpeed.measure_speed()

    measurements = Measurements.objects.select_related("server").values("upload", "download", "latency", "test_time", "server_id", "server__host")
    context = {"measurements": measurements}
    return render(request, 'details.html', context)

def server_info(request, server_id):
    if request.method == 'POST':
        if 'csv' in request.POST:
            return exportCSV.export_csv()
        elif 'speedtest' in request.POST:
            measureSpeed.measure_speed()

    server = Server.objects.filter(id=server_id).values()
    if server:
        context = server[0]
        return render(request, "server.html", context)

    return render(request, "404.html")

def error_404(request, exception):
    return render(request, '404.html')

