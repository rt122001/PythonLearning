from bs4 import BeautifulSoup 
import requests
import json
import ast
import pandas as pd

#trick: convert json html text to dictionary, ast lib converts string to dict,
#learning: requests module with headers, parsing, string json parsing, pandas dataframe csv 
url="https://www.imdb.com/chart/top/"
req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"}
body=requests.get(url, headers=req_headers)

soup=BeautifulSoup(body.text,"html.parser")
scriptdata=soup.find_all('script')[2]
stringdata=scriptdata.text
dictdata=ast.literal_eval(stringdata)

for i in range (0, len(dictdata['itemListElement'])):
    print(f"{i+1}. {dictdata['itemListElement'][i]['item']['name']}")

#to csv convert
df = pd.DataFrame(columns=('S.No','Name','URL','Rating','Genre'))
for i in range(0,len(dictdata['itemListElement'])):
   df.loc[i] = [i+1,dictdata['itemListElement'][i]['item']['name'],dictdata['itemListElement'][i]['item']['url'],dictdata['itemListElement'][i]['item']['aggregateRating']['ratingValue'],dictdata['itemListElement'][i]['item']['genre']]

df.to_csv('Top_250_IMDB.csv',index=False)