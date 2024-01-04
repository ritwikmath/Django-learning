from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import calendar

def monthly_challange(request, month):
    if not list(calendar.month_name).__contains__(month.capitalize()):
        return HttpResponseNotFound(f"{month} month not supported")
    return HttpResponse(month)

def monthly_challange_by_number(request, month):
    try:
        month_name = calendar.month_name[month]
        return HttpResponse(month_name)
    except IndexError:
        return HttpResponseNotFound("Month is not supported")