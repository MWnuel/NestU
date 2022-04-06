from django.contrib import admin
from .models import Settings, Measurements
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('interval', 'day', 'fixedtime', 'use_fixedtime')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Measurements)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('download', 'upload', 'latency', 'test_time')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True
