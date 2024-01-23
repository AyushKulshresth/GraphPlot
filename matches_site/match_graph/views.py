import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
import json
from . import services

def main(request):
    return render(request, 'head.html')

def main_page(request):
    services.enter_details()
    return render(request, 'main.html')

def index(request):
    new_dict = services.seasons_vs_matches()
    new_dict = json.dumps(new_dict)
    return render(request, "index.html", {"bar_graph_data": new_dict, "title": "Number of matches per season"})
    
def graph2(request):
    new_dict = services.winners_per_season()
    new_dict = json.dumps(new_dict)
    return render(request, "graph2.html", {"bar_graph_data": new_dict})

