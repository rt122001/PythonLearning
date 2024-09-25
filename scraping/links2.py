
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse

url="http://testphp.vulnweb.com/"

unvisited_internal_urls=[]#only internal urls
visited_internal_urls=[]
unvisited_internal_urls.append(url)
while len(unvisited_internal_urls)!=0:
    for iurl in unvisited_internal_urls:
        
        req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"}
        body=requests.get(iurl,headers=req_headers)

        print(f"Visiting: {iurl}")
        soup = BeautifulSoup(body.text,'html.parser')
        atags=soup.find_all('a')

        unvisited_urls=[]#includes internal and external urls
        for a in atags:
            href=a.get('href')
            if href.startswith('mailto:') or href.startswith('javascript:'):
                continue
            else:
                if iurl!=href:
                    unvisited_urls.append(href)
        
        #includes internal urls with relative urls converted to complete urls
        for uurl in unvisited_urls:
            parsed=urlparse(uurl)
            if parsed.netloc == '':
                completeurl=urljoin(url,uurl)
                if completeurl not in unvisited_internal_urls and completeurl not in visited_internal_urls:
                    unvisited_internal_urls.append(completeurl)#adding relative urls
                    #print(f"Relative to Complete URL: {completeurl}")
            elif parsed.scheme!='http' or parsed.scheme!='https': 
                continue
            else:
                if uurl not in unvisited_internal_urls and uurl not in visited_internal_urls:
                    unvisited_internal_urls.append(uurl)#adding internal urls
                    #print(f"Complete URL: {uurl}")
        unvisited_internal_urls.remove(iurl)
        print(len(unvisited_internal_urls))
        if iurl not in visited_internal_urls:
            visited_internal_urls.append(iurl)
        
        

    
    
        

