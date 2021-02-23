#akhmadfaizal
#192102002

from bs4 import BeautifulSoup
import pandas as pd 
import json, re, requests
import numpy as np
from pandas import ExcelFile


class Praktikkum():
	def __init__(self,link):
		self.link = link 

	def ExtractLink(self):
		get_text = requests.get(self.link).text
		proses = BeautifulSoup(get_text,"lxml")
		get = proses.find_all("a", href=True)

		df = pd.DataFrame()

		for fafa in get:
			conv = str(fafa)
			regex = re.findall("http[s][:]//+[\w\.][a-z]{2,7}.[A-Za-z0-9]{2,8}[\.][a-z]{2,3}.[\w\.]..[A-Za-z0-9]{2,9}",conv)
			df = df.append({"link":regex},ignore_index=True)

		df.to_excel("data_baru.xlsx", sheet_name="Sheet1")
		print(df)

	def perayapan(self):
		get_data = requests.get(self.link).text
		scrapy = BeautifulSoup(get_data,"lxml")
		get = scrapy.find_all("div",{"class":"desc_nhl"})
		
		df = pd.DataFrame()

		for take in get:
			if str(take.find("h2")) != "None":
				title = take.find("h2").get_text()
			if str(take.find("span",{"class":"labdate f11"})) != "None":
				date = take.find("span",{"class":"labdate f11"}).get_text()
				date = date.replace("detikSport","")
				date = date.replace("  ","")
				date = date.replace("\n","")
				date.replace("  |   ","")
			df = df.append({"tanggal": date, "judul":title},ignore_index=True)
		print(df)
		df.to_excel("data_baru.xlsx", sheet_name="Sheet2")

	def Json(self):
		get_json = requests.get(self.link).text
		cuplik = BeautifulSoup(get_json, "lxml")
		get = cuplik.find_all("script",{"type":"text/javascript"})

		i = 0 

		for p in get :
			if i == 8:
				page = str(p)
				page = page.replace("window.crumb = {};", "")
				page = page.replace("<script type=\"text/javascript\">", "")
				page = page.replace("</script>","")
				page = page.replace("window.isNewAddress = true;", "")
				page = page.replace("window.isNewAddress = false;", "")
				page = page.replace("window.pageModel =", "")
				page = page.replace("// }","")
				page = page.replace(" ","")
				page = page.replace('"success":true};', '"success":true}')
				page = page[:-1].replace("\n", "") + page[-1:]
						
				data = json.loads(page)
			i += 1

		data_json = pd.DataFrame()
		for post in data["data"]["paragraphs"]:
			title = post["Content"]["mem_title"]
			price = post["Content"]["price"]
			data_json = data_json.append({"judul":title, "harga":price},ignore_index=True)
		data_json.to_excel("data_baru.xlsx", sheet_name="Sheet3")
		print(data_json)	

link_1 = "https://sport.detik.com"
link_2 = "https://www.jd.id/search?keywords=gopro"

obj = Praktikkum(link_1)
obj.ExtractLink()