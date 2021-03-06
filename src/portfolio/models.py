from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.utils.timezone import now  

class Module(models.Model):
    title   = models.CharField(max_length=64)
    icon    = models.CharField(max_length=64)
    url     = models.CharField(max_length=64)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Project(models.Model):
    title   = models.CharField(max_length=64)
    icon    = models.CharField(max_length=64)
    url     = models.CharField(max_length=64)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title       = models.CharField(max_length=64)
    date        = models.date = models.DateTimeField(default=timezone.now)
    paradigm    = models.ForeignKey('Paradigm', on_delete=models.CASCADE, null=True)
    @property
    def get_months(self):
        delta: timedelta = now() - self.date
        months = delta.days / (365.2425/12)
        return months

    def __str__(self):
        return self.title

class Education(models.Model):
    title   = models.CharField(max_length=64)
    icon    = models.CharField(max_length=64)
    url     = models.CharField(max_length=64)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class Paradigm(models.Model):
    icon    = models.CharField(max_length=64)
    PARADIGM_CHOICES = (
        ('SE', 'Software Engineering'),
        ('WD', 'Web Development'),
        ('GM', 'Graphics and Media'),
        ('FW', 'Frameworks'),
    )
    paradigm = models.CharField(
        max_length=2,
        choices=PARADIGM_CHOICES,
    )

    def __str__(self):
        return self.get_paradigm_display()
