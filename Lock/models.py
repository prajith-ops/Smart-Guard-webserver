from django.db import models
from django.contrib.auth.models import User

class Lock(models.Model):
    status_choices=(
        ('Locked','LOcked'),
        ('Open','Open')
    )

    name=models.CharField(max_length=50)
    status=models.CharField(max_length=6,choices=status_choices,default="Locked")
    last_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    

class UserLockAccess(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    lock=models.ForeignKey(Lock,on_delete=models.CASCADE)
    access_granted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.id} -> {self.lock.id}"
    

class SensorData(models.Model):
    lock=models.ForeignKey(Lock,on_delete=models.CASCADE)
    motion=models.FloatField()
    vibration=models.FloatField()
    timestamp=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.lock.id} at {self.timestamp}"
    

class Alert(models.Model):
    alert_type_choices=(
        ('tamper','Tamper'),
        ('vibration','Vibration'),
    )

    lock=models.ForeignKey(Lock,on_delete=models.CASCADE)
    alert_type=models.CharField(max_length=50,choices=alert_type_choices)
    detected_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert {self.lock.id} - {self.alert_type} at {self.detected_time}"
