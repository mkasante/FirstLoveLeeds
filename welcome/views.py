from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render_to_response
from django.template import RequestContext

from member.models import Member, Attendance, AcademicInstitution
from event.models import Event, EventType

import datetime, re, os, requests



# Create your views here.
@login_required
def index(request):

	context = {}

	return render (request, 'newsfeed.html', context)


# 
@login_required
def _get_birthdays(request):
	now = datetime.datetime.now()
	members = Member.objects.all()

	member_dob = []
	for x in members:
		if x.date_of_birth != None:
			dob_month = x.date_of_birth.month
			dob_day = x.date_of_birth.day
			dob_year = x.date_of_birth.year

			if ((int(dob_month) == now.month)
				and int(dob_day) >= now.day):
				remaining_day = int(dob_day) - now.day 
				age = now.year - int(dob_year)

				member_dob.append((x, age, remaining_day))


	context = {
		'member_dob': member_dob
	}

	return render (request, '_partial/_birthdays.html', context)

@login_required
def _get_firsttimers(request):
	now = datetime.datetime.now()
	last30days = now - datetime.timedelta(days = 60)
	first_timers = Member.objects.filter(attendance_status__status = "First Timer", first_attended__gte = last30days).order_by('-first_attended')[:12]

	context = {
		'first_timers': first_timers
	}

	return render (request, '_partial/_firsttimers.html', context)


@login_required
def _get_evangelismlist(request):
	now = datetime.datetime.now()
	last30days = now - datetime.timedelta(days = 60)
	evangelism = Member.objects.filter(attendance_status__status = "Evangelism", last_modified__gte = last30days).order_by('-last_modified')[:12]

	context = {
		'evangelism': evangelism
	}

	return render (request, '_partial/_evangelism.html', context)


@login_required
def _get_outreachlist(request):
	now = datetime.datetime.now()
	last30days = now - datetime.timedelta(days = 60)
	outreach = Member.objects.filter(attendance_status__status = "Outreach", last_modified__gte = last30days).order_by('-last_modified')[:12]

	context = {
		'outreach': outreach
	}

	return render (request, '_partial/_outreach.html', context)