from django.db import models
from accounts.models import User
# Create your models here.

class WeightRecord(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
