import pandas as pd
from match_graph.models import Matches
from django.db.models import Count

def enter_details():
    # Matches.objects.all().delete()
    data = pd.read_csv('matches.csv')
    if Matches.objects.count():
        return
    for row in data.iterrows():
        if(row[1]["season"] != '' and row[1]["team1"] != '' and row[1]["team2"] != '' and row[1]["winner"] != ''):
            tup = Matches(season = row[1]["season"], team1 = row[1]["team1"], team2 = row[1]["team2"], winner = row[1]["winner"])
            tup.save()
        # print(row[1]["season"])

def seasons_vs_matches():
    query_set = Matches.objects.values('season').annotate(sCount = Count('season'))
    res_dict = []
    temp = {"x": [],
            "y": []}
    for res in query_set:
        temp["x"].append(res["season"])
        temp["y"].append(res["sCount"])
    res_dict.append(temp)
    # print(res_dict)
    return res_dict

def winners_per_season():
    res_dict = {}
    query_set = Matches.objects.values('season', 'winner').order_by().annotate(wCount = Count("id"))
    # print(query_set)
    for res in query_set:
        if res["season"] in res_dict:
            res_dict[res["season"]].append({
                "winner": res["winner"],
                "wCount": res["wCount"]
            })
        else:
            res_dict[res["season"]] = [{
                "winner": res["winner"],
                "wCount": res["wCount"]
            }]
    return res_dict