import requests
import urllib.request
import time
from lxml import html
from bs4 import BeautifulSoup
import time
from win10toast import ToastNotifier


def getScore():
	response = requests.get("https://www.espncricinfo.com/series/8039/game/1144523/england-vs-new-zealand-41st-match-icc-cricket-world-cup-2019").content
	soup = BeautifulSoup(response, "html.parser")
	h2Tags = soup.find_all('div',{'class':['cscore_score']})
	print(h2Tags[0].text)
	tree = html.fromstring(response)

	team1 = str(tree.xpath('(//a[@class="app_partial"]/span[@class="cscore_name cscore_name--short"])[1]/text()')[0])
	team2 = str(tree.xpath('(//a[@class="app_partial"]/span[@class="cscore_name cscore_name--short"])[2]/text()')[0])

	bat1 = str(tree.xpath('(//table/tbody/tr/td/a[@class="long-name"])[1]/text()')[0])
	bat1Score = str(tree.xpath('(//div[@class="content"]/table/tbody/tr[1]/td)[2]/text()')[0])
	ball1 = str(tree.xpath('(//div[@class="content"]/table/tbody/tr[1]/td)[3]/text()')[0])
	
	bat2 = str(tree.xpath('(//table/tbody/tr/td/a[@class="long-name"])[2]/text()')[0])
	bat2Score = str(tree.xpath('(//div[@class="content"]/table/tbody/tr[2]/td)[2]/text()')[0])
	ball2 = str(tree.xpath('(//div[@class="content"]/table/tbody/tr[2]/td)[3]/text()')[0])

	toaster = ToastNotifier()
	toaster.show_toast(team1 +" "+team2,
                   h2Tags[0].text+'\n'+
                   bat1+"   "+bat1Score+" ("+ball1+")"+"\n"+
                   bat2+"   "+bat2Score+" ("+ball2+")",
                   duration=10)



	time.sleep(25)
	getScore()


getScore()