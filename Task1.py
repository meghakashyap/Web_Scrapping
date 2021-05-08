import json
import requests
from bs4 import BeautifulSoup
page  = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
text = BeautifulSoup(page.text,"html.parser")
def scrape_top_list():
    div = text.find("div",class_="lister")
    table= div.find("tbody", class_="lister-list")
    tr=table.find_all("tr")
    movie_name=[]
    movie_year=[]
    movie_rating=[]
    movie_url=[]
    movie_rank=[]
    for i in tr:
        details=i.find("td",class_="titleColumn").get_text().strip()
        # print(details)
        rank=""
        j=0
        while j<len(details):
            if "." not in details[j]:
                rank+=details[j]
            else:
                break
            j+=1
        movie_rank.append(rank)

        rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)

        name=i.find("td",class_="titleColumn").a.get_text()
        movie_name.append(name)

        year=i.find("td",class_="titleColumn").span.get_text()
        movie_year.append(year)

        url= i.find("td",class_="titleColumn").a["href"]
        url_add = "https://www.imdb.com"+url
        movie_url.append(url_add)

    movie_list=[]
    movie_dict={"Rank":"","Name":"","Year":"","Rating":"","Url":""}
    index=0
    while index<len(movie_rank):
        movie_dict["Rank"]=int(movie_rank[index])
        movie_dict["Name"]=(movie_name[index])
        movie_dict["Year"]=int(movie_year[index][1:5])
        movie_dict["Rating"]=float(movie_rating[index])
        movie_dict["Url"]=movie_url[index]
        movie_list.append(movie_dict.copy())
        index+=1
    with open("Task1.json","w+") as movie_data:
        json.dump(movie_list,movie_data,indent=4)
    return movie_list

scrape_top_list()

#task1