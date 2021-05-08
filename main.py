import requests
import bs4
url="https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
response=requests.get(url)
# print(type(response))
# print(response.text)
file ="tem.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")
bs.prettify()

formatted_text=bs.prettify()
print(formatted_text)

with open(file,"w+") as f:
    f.write(formatted_text)

list_image=bs.find_all("img")
print(list_image)

no_of_image=len(list_image)

list_as=bs.find_all("a")
no_of_as=len(list_as)

print("number of img tags",no_of_image)
print("number of anchor tags",no_of_as)