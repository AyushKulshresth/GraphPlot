import pandas as pd
from .models import PrimarySchools
from django.db.models import Count

def enter_details():
    data = pd.read_csv('primaryschool.csv')
    if PrimarySchools.objects.count():
        return
    for row in data.iterrows():
        if(row[1]["name"] != '' and row[1]["moi"] != '' and row[1]["cat"] != '' and row[1]["district_name"] != ''):
            tup = PrimarySchools(name = row[1]["name"], language = row[1]["moi"], category = row[1]["cat"], district = row[1]["district_name"])
            tup.save()
        # print(row)
            
def school_per_district():
    query_set = PrimarySchools.objects.values('district').annotate(dCount = Count('district'))
    # print(query_set)
    res_dict = []
    temp = {"x": [],
            "y": []}
    for res in query_set:
        temp["x"].append(res["district"])
        temp["y"].append(res["dCount"])
    res_dict.append(temp)
    # print(res_dict)
    return res_dict

def school_cat_per_district():
    res_dict = {}
    query_set = PrimarySchools.objects.values('district', 'category').order_by().annotate(cCount = Count("id"))
    # print(query_set)
    for res in query_set:
        if res["category"] in res_dict:
            res_dict[res["category"]].append({
                "district": res["district"],
                "cCount": res["cCount"]
            })
        else:
            res_dict[res["category"]] = [{
                "district": res["district"],
                "cCount": res["cCount"]
            }]
    print(res_dict)
    return res_dict

def language_per_district():
    res_dict = {}
    query_set = PrimarySchools.objects.values('district', 'language').order_by().annotate(cCount = Count("id"))
    # print(query_set)
    for res in query_set:
        if res["language"] in res_dict:
            res_dict[res["language"]].append({
                "district": res["district"],
                "cCount": res["cCount"]
            })
        else:
            res_dict[res["language"]] = [{
                "district": res["district"],
                "cCount": res["cCount"]
            }]
    print(res_dict)
    return res_dict