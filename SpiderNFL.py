from scrapy import Request
from scrapy import Spider
from SpiderNFL.items import NFLTeam
import re

class SpiderNFL(Spider):
	name = 'SpiderNFL'
	allowed_urls = ['https://www.spotrac.com/']
	start_urls = ['https://www.spotrac.com/nfl/']
	
	def parse(self, response):
		text = response.xpath('//div[@class="teamoption"]/a/@href').extract()

#Subset list to start at position 3:
		text = text[2::]

#Keep every 6th Element including the first:
		text = text[::6]

#Iterate through team URL to add in all years
		years = [2013,2014,2015,2016,2017,2018]

		team_year_url = []
		
		for i in text:
			for year in years:
				mod_url = i + str(year) 
				team_year_url.append(mod_url)
		for url in team_year_url:
			yield Request(url=url, callback=self.parse_result_page)

	def parse_result_page(self, response):

		Team_Name = response.xpath('//*[@id="main"]/header/div[2]/h1/text()').extract_first()
		Team_Name = Team_Name.split()
		Team_Name.pop(-1)
		Team_Name = ' '.join(Team_Name)
		Year = response.xpath('//*[@id="sidebar"]/section[1]/header/h2/text()').extract_first()
		Year = Year.split()
		Year = Year[1]
		QB_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[3].replace('$','').replace(',',''))
		RB_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[4].replace('$','').replace(',',''))
		WR_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[5].replace('$','').replace(',',''))
		TE_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[6].replace('$','').replace(',',''))
		OL_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[7].replace('$','').replace(',',''))
		DL_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[8].replace('$','').replace(',',''))
		LB_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[9].replace('$','').replace(',',''))
		DB_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[10].replace('$','').replace(',',''))
		ST_Spend = int(response.xpath('//*[@class="parent"]/td[3]/text()').extract()[11].replace('$','').replace(',',''))
		Active_Payroll = QB_Spend+RB_Spend+WR_Spend+TE_Spend+OL_Spend+DL_Spend+LB_Spend+DB_Spend+ST_Spend

		item = NFLTeam()
		item['Team_Name']=Team_Name
		item['Year']=Year
		item['QB_Spend']=QB_Spend
		item['RB_Spend']=RB_Spend
		item['WR_Spend']=WR_Spend
		item['TE_Spend']=TE_Spend
		item['OL_Spend']=OL_Spend
		item['DL_Spend']=DL_Spend
		item['LB_Spend']=LB_Spend
		item['DB_Spend']=DB_Spend
		item['ST_Spend']=ST_Spend
		item['Active_Payroll']=Active_Payroll

		yield item

