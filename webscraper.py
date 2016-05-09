#! python3
import webbrowser, sys, requests, bs4, os, re, MySQLdb, unicodedata
##from selenium import webdriver

url = 'http://www.tv.com/shows'
urll = 'http://www.tv.com'
season1 = "/season-1"
dec2010 = "/decade/2010s/page"

##os.makedirs('series', exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)

    db = MySQLdb.connect("localhost","root","","episeries" )
    cursor = db.cursor()
    cursor.execute('DELETE FROM episodes WHERE 1')
    cursor.execute('ALTER TABLE episodes AUTO_INCREMENT = 1')
    

    
    for i in range(1,9):
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
                    serietitling = seasonsoup.find("h1",{"itemprop" : "name"})
                    for episode in seasonsoup.find_all("div", class_="no_toggle _clearfix"):
                        title = episode.find("a", class_="title")
                        epi_title = title.contents[0]
                        epi = episode.find("div", class_="ep_info")
                        date = episode.find("div", class_="date")
                        if(date.text):
                            epi_date = str(date.contents[0])
                        epinummer = epi.contents[0]
                        epinummer = epinummer.replace(u'\xa0', u' ')
                        epi_episode = str(epinummer.strip('\n\r\t'))
                        serietitlingg= serietitling.contents[0].split(" - ")
                        seriename = serietitlingg[0]
                        ##epi_title = epi_title.encode("latin-1", errors='ignore')
                        epi_title = epi_title.replace(u'\"', u'')
                        epi_title = epi_title.replace(u'\u2013', u' ')
                        epi_title = epi_title.replace(u'\u2014', u' ')
                        epi_title = epi_title.replace(u'\u2026', u'')
                        epi_title = epi_title.replace(u'\u014d', u' ')
                        epi_title = epi_title.replace(u'\u0101', u' ')
                        epi_title = epi_title.replace(u'\u02bb', u' ')
                        epi_title = epi_title.replace(u'\u016b', u' ')
                        epi_title = epi_title.replace(u'\xe9', u' ')
                        seriename = seriename.replace(u'\xe9', u' ')
                        seriename = str(seriename)
                        season = str(serietitlingg[1])
                        ##print(seriename.contents[0])
                        while True:
                            try:
                                cursor.execute('INSERT INTO episodes (title, date, season, serie, episode) VALUES("%s", "%s", "%s", "%s", "%s")' %(epi_title, epi_date, season, seriename, epi_episode))
                                db.commit()
                                break
                            except UnicodeEncodeError:
                                cursor.execute('INSERT INTO episodes (title, date, season, serie, episode) VALUES("%s", "%s", "%s", "%s", "%s")' %(epi_episode, epi_date, season, seriename, epi_episode))
                                db.commit()
                                break
                            else:
                                print("This episode is fucked up!")
                                break
                        print(seriename)
                        print(season)
                        print(epi_episode)
                        print(epi_title)
                        print(epi_date)


    db.close()

    break      
        
        
