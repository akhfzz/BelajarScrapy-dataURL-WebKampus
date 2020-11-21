from bs4 import BeautifulSoup
import pandas as pd 
import json, random, re, requests

class Unjaya():
	def __init__(self,kampus):
		self.kampus = kampus

	def to_url(self):
		Univ_list = []
		total = 0
		while total < 1 :
			link_kampus = "https://unjaya.ac.id/unjaya-berhasil-luluskan-508-"+self.kampus+"-dengan-wisuda-daring/"
			page_website = requests.get(link_kampus).content
			read_bs4 = BeautifulSoup(page_website,"lxml")
			finding = read_bs4.find_all("body")
			for find in finding:
				tags = find.find_all("script")
				total+=1
				for hastag in tags:
					Univ_list.append(hastag.get("src"))
		for data in Univ_list:
			print(data)
		return Univ_list
param = "mahasiswa"
show = Unjaya(param)
show.to_url()



