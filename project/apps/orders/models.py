from django.db import models
from django.conf import settings

class caca(models.Model):
    name = models.CharField(requiered=True ,max_length = 100)
class model(models.Model):
    name = models.CharField(requiered = False )
    date = models.DateTimeField(auto_now_Add= True)
    foreing =models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name="sessions"
    )