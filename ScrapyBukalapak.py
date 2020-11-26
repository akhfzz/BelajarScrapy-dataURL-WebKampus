from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import pandas as pd 
import json
import csv


def SeleniumPractice(element): 
	Drive = webdriver.Chrome(executable_path = "chromedriver.exe")
	Drive.get("https://www.bukalapak.com/")
	search = Drive.find_element_by_name(element)
	search.send_keys("sepatu")
	search.send_keys(Keys.RETURN)
	print(search)
	Drive.quit()
SeleniumPractice("search[keywords]")

def Scrapy(word):
	write = csv.writer(open("Scrapy.csv","w", newline=""))
	header = ["ID", "Keyword", "Thumbnail", "Update", "URL"]
	write.writerow(header)

	url_bl = "https://api.bukalapak.com/trends/{}".format(word)
	variable_param = {
		"access_token" : "WW0C8BB2z2jbciMrhWAPRInAR6SfbTcXUY4FZ3kl39RkAQ"
	}

	procces_req = requests.get(url_bl, params=variable_param).json()
	#print(procces_req.status_code)
	product_tar = procces_req["data"]
	for req in product_tar:
		#print(req)
		product_id = req["id"]
		product_keyword = req["keyword"]
		product_thumbnail = req["thumbnail_url"]
		product_update = req["updated_at"]
		product_url = req["url"]
		return ("Id:",product_id, "Keyword:",product_keyword,"Thumbnail:", product_thumbnail,
			"Update Product:",product_update, "URL:",product_url)
		write = csv.writer(open("Scrapy.csv","a", newline=""))
		key = [product_id,product_keyword,product_thumbnail,product_update,product_url]
		write.writerow(key)

pandas = pd.read_csv("Scrapy.csv", sep=",")
print(pandas)
print(Scrapy("keyword"))
