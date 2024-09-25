
import requests
import os
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urljoin,urlparse

def download_image(url,folder):

    req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"}
    response = requests.get(url, headers=req_headers)

    imagename=url.split('/')[-1]
    imagepath=os.path.join(folder,imagename)

    with open(imagepath, 'wb') as imgfileobject:
        imgfileobject.write(response.content)
    print(f"Image saved at {imagepath}")

#Learning: add full url to relative urls,parse urls in images
#todo: add loop for multiple urls
parser = argparse.ArgumentParser("Image parser from URL")
parser.add_argument('url',nargs='+', help='Enter the url of webpage to download images from')
args=parser.parse_args()
url=args.url

req_headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"}
body=requests.get(url,headers=req_headers)
response=body.text

soup = BeautifulSoup(response,'html.parser')
images=soup.find_all('img') #returns list with all img tags

image_list=[]
for image in images:
    image_list.append(image.get('src'))

final_image_list=[]
for image in image_list:
    img_url_parse=urlparse(image)
    if img_url_parse.netloc == '':
        final_image_list.append(urljoin(url,image))
    elif img_url_parse.netloc!=url:
        continue
    else:
        final_image_list.append(image)

print(final_image_list)

for image_url in final_image_list:
    download_image(image_url,'imageparse_images')



