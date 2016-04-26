#! python3
import webbrowser, sys, requests, bs4, os, re
##from selenium import webdriver

url = 'http://www.tv.com/shows'
urll = 'http://www.tv.com'
season1 = "/season-1"
dec2010 = "/decade/2010s/page"
##os.makedirs('series', exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    for i in range(1,20):
        res = requests.get(url + dec2010+str(i))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
    

        for link in soup.find_all("div", class_="info"):
            serie = link.find("h4")
            serielink = serie.find('a').get('href')
            ##print(serie.find('a').contents[0])
            serieresult = requests.get(urll+serielink+season1)
            seriesoup = bs4.BeautifulSoup(serieresult.text,"html.parser")
            for seasonlinks in seriesoup.find_all("li", class_="filter"):
                if( re.findall("season",str(seasonlinks.find('a').get('href')))):
                    ##print(seasonlinks.find('a').get('href'))
                    seasonresult = requests.get(urll+seasonlinks.find('a').get('href'))
                    seasonsoup = bs4.BeautifulSoup(seasonresult.text,"html.parser")
                    serietitling = seasonsoup.find("h1")
                    for episode in seasonsoup.find_all("div", class_="no_toggle _clearfix"):
                        title = episode.find("a", class_="title")
                        epi = episode.find("div", class_="ep_info")
                        date = episode.find("div", class_="date")
                        epinummer = str(epi.contents[0])
                        serietitlingg= serietitling.contents[0].split(" - ")
                        seriename = serietitlingg[0]
                        season = serietitlingg[1]
                        ##print(seriename.contents[0])
                        print(seriename)
                        print(season)
                        print(epinummer.strip('\n\r\t'))
                        print(title.contents[0])
                        if(date.text):
                            print(date.contents[0])



##        for link in soup.find_all(text='Ep Guide'):
##            serie = requests.get(urll+ link.parent.get('href'))
##            print(link.parent.get('href'))
##            seriesoup = bs4.BeautifulSoup(serie.text, "html.parser")
##            for serielink in seriesoup.find_all("div", class_="no_toggle_left"):
##               title = serielink.find("div", class_="title")
##               epi = serielink.find("div", class_="ep_info")
##               epinummer = str(epi.contents[0])
##               print(epinummer.strip('\n\r\t'))














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
        
        
