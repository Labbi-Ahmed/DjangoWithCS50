from django.shortcuts import render
import datetime
# Create your views here.

info = {
    "name":"Labbi Ahmed",
    "roll": "1610676135",
    "age": 29,
    "Gender": "Male"
}

def index(request):
    now = datetime.datetime.now()
    value = {"month":now.month, "year":now.year, "day":now.day, "Time": now.time,"info":info}
    return render(request,"newyear/index.html",value)