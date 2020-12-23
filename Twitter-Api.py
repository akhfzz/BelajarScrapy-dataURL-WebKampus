import tweepy
import re
from textblob import TextBlob

class Sentimental:
	def __init__(self, tagar):
		self.tagar = tagar
		self.key = "XeGTjuWHWSLc02MPzcsBkO2WW"
		self.secret_key = "UlfiJHunu4pEolKpiUS5Jt99RKwjA4Z8zwDoxEamzHe8TGfF7Z"
		self.acces_token = "1333232471790428161-SFsGH29BLJCxjJejjir9r09dm4J1Wr"
		self.acces_secret = "lSTcjemQMptqLuntz9JzVLoRW5HMh0AIXs01Opq9wDSJl"
	def ProcessScrapy(self):
		otentikasi = tweepy.OAuthHandler(self.key, self.secret_key)
		otentikasi.set_access_token(self.acces_token, self.acces_secret)
		active = tweepy.API(otentikasi)
		analys_user = active.user_timeline(id="Pilkada", count=15)
		# print(analys_user)
		cache_search = active.search(q=self.tagar,lang="id",count=400)
		#print(cache_search)
		result = []
		for tweet_user in cache_search:
			type_dict = {}

			type_dict["Tanggal post"] = tweet_user.created_at
			type_dict["User Name"] = tweet_user.user.screen_name
			type_dict["Message"] = tweet_user.text
			clean_data = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_user.text).split())
			
			analys = TextBlob(clean_data)
			try:
				analys.translate(to="en")
			except Exception as Nt:
				print(Nt)

			if analys.sentiment.polarity > 0 :
				type_dict["sentiment"] = "Positive"
			elif analys.sentiment.polarity == 0:
				type_dict["sentiment"] = "Netral"
			else:
				type_dict["sentiment"] = "Negative"
			
			result.append(type_dict)

		comment_positif = [tweet for tweet in result if tweet["sentiment"] == "Positive"]
		comment_negative = [tweet for tweet in result if tweet["sentiment"] == "Negative"]
		comment_netral = [tweet for tweet in result if tweet["sentiment"] == "Netral"]

		persentase_positif = 100*len(comment_positif)/len(result)
		persentase_negatif = 100*len(comment_negative)/len(result)
		persentase_netral = 100*len(comment_netral)/len(result)

		print("Hasil Sentiment")
		print("Persentase positif :{}".format(persentase_positif))
		print("Persentase negatif:{}".format(persentase_negatif))
		print("Persentase netral :{}".format(persentase_netral))

masukkan = input("What do u want for topic : ")
Objektiv = Sentimental(masukkan)
Objektiv.ProcessScrapy()