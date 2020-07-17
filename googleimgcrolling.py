#from google_images_download import google_images_download   #importing the library
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

#serch = input('찾는 사진')
url = f'https://www.google.com/search?q=먹방&tbm=isch'

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup =BeautifulSoup(html, 'html.parser')

img = soup.select("div.bRMDJf img")
imgurl = []
n = 100

for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

for i in imgurl:
    urlretrieve(i, "./"+str(n)+".jpg")
    n+=1

driver.close()

#response = google_images_download.googleimagesdownload()   #class instantiation

#arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
#paths = response.download(arguments)   #passing the arguments to the function
#print(paths)   #printing absolute paths of the downloaded images