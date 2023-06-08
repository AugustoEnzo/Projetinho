# import scrapy
# import json
# from pymongo.mongo_client import MongoClient
#
# def get_database():
#     # Provide the mongodb atlas url to connect python to mongodb using pymongo
#     CONNECTION_STRING = "mongodb+srv://leocfacca:F7kE6Sihp13Og46a@cluster0.ui7eplp.mongodb.net/"
#
#     # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#     client = MongoClient(CONNECTION_STRING)
#
#     # Create the database for our example (we will use the same database throughout the tutorial
#     return client['Crawler']
#
# dbname = get_database('Crawler')
# collection_name = dbname["Marcas"]
#
#
# class BlogSpider(scrapy.Spider):
#     name = 'blogspider'
#     start_urls = ['https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter=L']
#
#     def parse(self, response):
#         brand_list = []
#         for title in response.css('rankingNames'):
#             brand = yield {'title': title.css('::text').get()}
#             brand_list = {'Brand Name': brand}
#             brand_list.append(brand)
#         with open('./brand_list.json', 'w') as f:
#             json.dump(brand_list, f)
#         with open('./brand_list.json', 'r') as f:
#             brand = json.load(f)
#             collection_name.insert_many(brand)
#
#         for next_page in response.css('a.next'):
#             yield response.follow(next_page, self.parse)
