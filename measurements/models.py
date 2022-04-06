from django.db import models

# Create your models here.

class Measurements(models.Model):
    download = models.DecimalField(decimal_places=5, max_digits=20)
    upload = models.DecimalField(decimal_places=5, max_digits=20)
    latency = models.IntegerField()
    test_time = models.DateTimeField(auto_now_add=True)
    server = models.ForeignKey("Server", related_name="server", on_delete=models.CASCADE)

    def datepublished(self):
        return self.test_time.strftime("%d %B, %Y || %H:%M:%S")

class Server(models.Model):
    url = models.URLField(max_length=500)
    lat = models.DecimalField(decimal_places=5, max_digits=20)
    lon = models.DecimalField(decimal_places=5, max_digits=20)
    city = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    cc = models.TextField(max_length=3)
    sponsor = models.TextField(max_length=200)
    id = models.IntegerField(primary_key=True)
    host = models.TextField(max_length=200)
    download = models.IntegerField()
    latency = models.DecimalField(decimal_places=5, max_digits=20)

class Settings(models.Model):
    WEEK_DAYS = (
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Fr', 'Friday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
        ('Al', 'All'),
    )
    interval = models.IntegerField()
    day = models.CharField(max_length=2, choices=WEEK_DAYS, default="Al")
    fixedtime = models.TimeField()
    use_fixedtime = models.BooleanField(default=False)

