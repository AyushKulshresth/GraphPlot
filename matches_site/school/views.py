from django.shortcuts import render
from . import services
from django.http import HttpResponse
import json

def main(request):
    services.enter_details()
    return render(request, 'choose.html')

def graph3(request):
    new_dict = services.school_per_district()
    new_dict = json.dumps(new_dict)
    return render(request, 'graph3.html', {"bar_graph_data": new_dict, "title": "Number of Schools per District"})

def graph4(request):
    new_dict = services.school_cat_per_district()
    new_dict = json.dumps(new_dict)
    return render(request, 'graph4.html', {"bar_graph_data": new_dict})

def graph5(request):
    new_dict = services.language_per_district()
    new_dict = json.dumps(new_dict)
    return render(request, 'graph5.html', {"bar_graph_data": new_dict})