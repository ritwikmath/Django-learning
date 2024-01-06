from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
import calendar
from django.urls import reverse
from django.template.loader import render_to_string

def index(request):
    return render(request, "challanges/challange.html", {
        "months": calendar.month_name,
        "title": "List of months",
        "header": "Month list",
        "css": "style.css"
    })

def monthly_challange(request, month):
    capitalized_month = month.capitalize()
    if not list(calendar.month_name).__contains__(capitalized_month):
        response_text = render_to_string("404.html")
        return HttpResponseNotFound(response_text)
    search = request.GET.get("search")
    return render(request, "challanges/monthly_challanges.html", {
        "month": capitalized_month,
        "search": search
    })

def monthly_challange_by_number(request, month):
    try:
        month_name = calendar.month_name[month]
        return HttpResponseRedirect(reverse("monthly-challange", args=[month_name]))
    except IndexError:
        return HttpResponseNotFound("Month is not supported")