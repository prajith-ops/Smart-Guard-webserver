from django.contrib import admin

from .models import *

admin.site.register(Lock)
admin.site.register(UserLockAccess)
admin.site.register(SensorData)
admin.site.register(Alert)