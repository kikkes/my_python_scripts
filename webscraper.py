#! python3
import webbrowser, sys, requests, bs4, os, re
from selenium import webdriver

url = 'http://www.tv.com/shows'
urll = 'http://www.tv.com'
dec2000 = "/decade/2000s/page"
dec2010 = "/decade/2010s/page"
os.makedirs('series', exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url + dec2000)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    for link in soup.find_all(text='Ep Guide'):
        serie = requests.get(urll+ link.parent.get('href'))
##        seriesoup = bs4.BeautifulSoup(serie.text, "html.parser")
##        for serielink in seriesoup.find_all("div", class_="no_toggle_left"):
##           print(serielink)     






        ##if(str(link.get('href')) !="None"):
          ##  print(link.get('href'))
        
          ##  urll = link.get('href')





            
##        if re.search("http", str(link.get('href'))):
##            urll = link.get('href')
##        result = requests.get(urll)
##        soupp = bs4.BeautifulSoup(result.text, "html.parser")
##        for linkk in soupp.find_all('a'):
##            if(str(linkk.get('href')) !="None"):
##            ##print(linkk.findAll(text=True))
##                print(linkk.get('href'))
    break      
        
        
