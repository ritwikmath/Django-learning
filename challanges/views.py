from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import calendar

def monthly_challange(request, month):
    if not list(calendar.month_name).__contains__(month.capitalize()):
        return HttpResponseNotFound(f"{month} month not supported")
    return HttpResponse(f"{month}")
