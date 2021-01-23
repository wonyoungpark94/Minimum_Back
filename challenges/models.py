from datetime import datetime

from django.db import models
from accounts.models import User


class Challenge(models.Model):
    title: str = models.CharField(max_length=100)
    content: str = models.TextField()
    start_with: datetime = models.DateTimeField()
    end_with: datetime = models.DateTimeField()


class UserChallenge(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    fee = models.PositiveIntegerField()
    refund = models.PositiveIntegerField()
    status = models.CharField(
        max_length=1,
        choices=(
            ("f", "fail"),
            ("p", "progess"),
            ("s", "succeed"),
        ),
    )
