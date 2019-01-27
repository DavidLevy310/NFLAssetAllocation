from scrapy import Request
from scrapy import Spider
from SpiderNFLWins.items import NFLWins
import re
years = [2013,2014,2015,2016,2017,2018]

class SpiderNFLWins(Spider):
	name = 'SpiderNFLWins'
	allowed_urls = ['https://www.pro-football-reference.com/']
	start_urls = ['https://www.pro-football-reference.com/years/' + str(x) for x in years]

	def parse(self, response):

		Year = response.xpath('//*[@id="meta"]/div[2]/h1/span[1]/text()').extract_first()
		AFC_Team_Name = response.xpath('//*[@id="AFC"]/tbody/tr/th/a/text()').extract()
		NFC_Team_Name = response.xpath('//*[@id="NFC"]/tbody/tr/th/a/text()').extract()
		Team_Name = AFC_Team_Name+NFC_Team_Name
		
		if Year == '2013' or Year == '2014' or Year == '2016' or Year == '2018':
			AFC_Team_Win_Pct = response.xpath('//*[@id="AFC"]/tbody/tr/td[4]/text()').extract()
			NFC_Team_Win_Pct = response.xpath('//*[@id="NFC"]/tbody/tr/td[4]/text()').extract()
			Win_Pct = AFC_Team_Win_Pct+NFC_Team_Win_Pct
			
			AFC_Pts_For = response.xpath('//*[@id="AFC"]/tbody/tr/td[5]/text()').extract()
			NFC_Pts_For = response.xpath('//*[@id="NFC"]/tbody/tr/td[5]/text()').extract()
			Pts_For=AFC_Pts_For+NFC_Pts_For
			
			AFC_Pts_Agst = response.xpath('//*[@id="AFC"]/tbody/tr/td[6]/text()').extract()
			NFC_Pts_Agst = response.xpath('//*[@id="NFC"]/tbody/tr/td[6]/text()').extract()
			Pts_Agst = AFC_Pts_Agst+NFC_Pts_Agst
		else:
			AFC_Team_Win_Pct = response.xpath('//*[@id="AFC"]/tbody/tr/td[3]/text()').extract()
			NFC_Team_Win_Pct = response.xpath('//*[@id="NFC"]/tbody/tr/td[3]/text()').extract()
			Win_Pct = AFC_Team_Win_Pct+NFC_Team_Win_Pct
			
			AFC_Pts_For = response.xpath('//*[@id="AFC"]/tbody/tr/td[4]/text()').extract()
			NFC_Pts_For = response.xpath('//*[@id="NFC"]/tbody/tr/td[4]/text()').extract()
			Pts_For=AFC_Pts_For+NFC_Pts_For
			
			AFC_Pts_Agst = response.xpath('//*[@id="AFC"]/tbody/tr/td[5]/text()').extract()
			NFC_Pts_Agst = response.xpath('//*[@id="NFC"]/tbody/tr/td[5]/text()').extract()
			Pts_Agst = AFC_Pts_Agst+NFC_Pts_Agst

		item = NFLWins()
		item['Year']=Year
		for i in range(0,32):
			item['Team_Name']=Team_Name[i]
			item['Win_Pct']=Win_Pct[i]
			item['Pts_For']=Pts_For[i]
			item['Pts_Agst']=Pts_Agst[i]

			yield item

			





