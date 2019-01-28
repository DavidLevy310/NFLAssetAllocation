import scrapy


class NFLWins(scrapy.Item):
	Year = scrapy.Field()
	Team_Name = scrapy.Field()
	Win_Pct = scrapy.Field()
	Pts_For = scrapy.Field() 
	Pts_Agst = scrapy.Field()