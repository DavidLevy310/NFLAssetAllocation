from scrapy.exporters import CsvItemExporter

class WriteItemPipeline(object):
    def __init__(self):
        self.filename = 'SpiderNFLWins.csv'
    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.fields_to_export = ['Year','Team_Name','Win_Pct','Pts_For','Pts_Agst']
        self.exporter.start_exporting()
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
