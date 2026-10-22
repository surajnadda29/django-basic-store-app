from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myfunc(request):
    data={"name":"shalini","skills":["Python","Gen AI","Java","Machine Learning"]}
    return render(request,"index.html",context=data)
#     business logic  model  data   manipulation ready as required by frontend deve and pass data to frontend
