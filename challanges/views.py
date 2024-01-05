from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import calendar
from django.urls import reverse
from django.template.loader import render_to_string

def index(request):
    text = ""
    for month in calendar.month_name:
        if month == "":
            continue
        text += f"<li><a href={reverse('monthly-challange', args=[month])}>{month}</a></li>" 
    return render(request, "challanges/challange.html")

def monthly_challange(request, month):
    if not list(calendar.month_name).__contains__(month.capitalize()):
        return HttpResponseNotFound(f"<span style='color:red'>{month} month not supported</span>")
    search = request.GET.get("search")
    response_content = f"""
        <h1>Selected Month is {month}</h1>
        <h3>Search value is {search or 'Empty'}</h3>
    """
    return HttpResponse(response_content)

def monthly_challange_by_number(request, month):
    try:
        month_name = calendar.month_name[month]
        return HttpResponseRedirect(reverse("monthly-challange", args=[month_name]))
    except IndexError:
        return HttpResponseNotFound("Month is not supported")