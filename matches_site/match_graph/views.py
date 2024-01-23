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
    # data = pd.read_csv('matches.csv')
    # data_list = data["team1"].tolist()
    # print(data["team1"].tolist())
    # get_info()
    # bar_graph = data.groupby("season")["id"].count().to_dict()
    # # print(bar_graph)
    # new_dict = {}
    # for keys, values in bar_graph.items():
    #     if "x" not in new_dict:
    #         new_dict["x"] = [keys]
    #     else:
    #         new_dict["x"].append(keys)

    #     if "y" not in new_dict:
    #         new_dict["y"] = [values]
    #     else:
    #         new_dict["y"].append(values)

    # print(new_dict)
    # new_dict = json.dumps(new_dict)
    # fig.savefig("static/plot.py")
    new_dict = services.seasons_vs_matches()
    new_dict = json.dumps(new_dict)
    return render(request, "index.html", {"bar_graph_data": new_dict, "title": "Number of matches per season"})
    
def graph2(request):
    new_dict = services.winners_per_season()
    new_dict = json.dumps(new_dict)
    return render(request, "graph2.html", {"bar_graph_data": new_dict})

