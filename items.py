import scrapy

class NFLTeam (scrapy.Item):
	Team_Name = scrapy.Field()
	Year = scrapy.Field()
	QB_Spend = scrapy.Field()
	RB_Spend = scrapy.Field()
	WR_Spend = scrapy.Field()
	TE_Spend = scrapy.Field()
	OL_Spend = scrapy.Field()
	DL_Spend = scrapy.Field()
	LB_Spend = scrapy.Field()
	DB_Spend = scrapy.Field()
	ST_Spend = scrapy.Field()
	Active_Payroll = scrapy.Field()