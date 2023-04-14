import datetime

from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_entered_at_formatted_duration(self):
        return self.entered_at.strftime('%d %b %Yг. %H:%M')

    def get_visit_duration(self):
        if self.leaved_at:
            leaved_at = self.leaved_at.timestamp()
            entered_at = self.entered_at.timestamp()
            return (leaved_at - entered_at) // 3600
        else:
            return 0

    def get_visit_formatted_duration(self):
        if self.leaved_at:
            return self.leaved_at - self.entered_at
        else:
            return 'В хранилище'

    def get_current_visit_formatted_duration(self):
        local_time = timezone.localtime()
        return local_time - self.entered_at

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
