import requests
import json
from bs4 import BeautifulSoup
from Task1 import scrape_top_list
# year_dict={}
def group_by_year(movies):
    year_dict={}
    # main_list=[]
    for i in movies:
        main_list=[]
        for j in movies:
            if i["Year"]==j["Year"]:
                main_list.append(i)
                year_dict[i["Year"]] =main_list
            # main_list.append(year_dict)

    with open("Task2.json","w+") as file:
        json.dump(year_dict,file,indent=4)        
        check=json.dumps(year_dict,indent=4)    
    return main_list

group_by_year(movies=scrape_top_list())
#task 2