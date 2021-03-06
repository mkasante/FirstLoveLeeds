from django.db import models
from django.contrib import admin

# Create your models here.
class Event(models.Model):
	date = models.DateTimeField()
	event = models.ForeignKey('EventType', on_delete=models.CASCADE)
	attendance_count = models.IntegerField()
	first_timers_count = models.IntegerField()
	born_again_count = models.IntegerField()
	venue = models.CharField(max_length=100, blank=True)
	room = models.CharField(max_length=100, blank=True)
	last_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.event.name

	class Meta:
		ordering = ["-date"]


class EventType(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]
