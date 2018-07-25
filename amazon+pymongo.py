from selenium import webdriver
from pyquery import PyQuery as pq
import pymongo


def get_pq(url):
	options = webdriver.FirefoxOptions()
	options.add_argument('-headless')
	html = webdriver.Firefox(firefox_options=options) # set headless model 
	html.get(url)
	doc = html.page_source
	doc = pq(doc)
	html.close()
	# print(doc)
	return doc


def get_source(doc):
	uls = doc('#container #mainResults li').items()
	# print(uls)
	all_data = []
	for lis in uls:
		data = {}
		data['data-asin'] = lis.attr('data-asin')
		data['img'] = lis('img').attr('src')
		data['name'] = lis('h2').attr('data-attribute')
		data['price'] = lis('.sx-price.sx-price-large').text().replace(' ',',')
		data['start'] = lis('.a-icon-alt').text()
		all_data.append(data)
	return all_data


get_doc = get_pq("https://www.amazon.com/b?node=2407748011&page=2")
get_data = get_source(get_doc)
# with open("/home/just_study/Desktop/sth/amazon2.txt", 'w+') as f:
# 	for i in get_data:
# 		f.write(repr(i))  # 将对象转化为供解释器读取的形式,返回一个对象的 string 格式。
# 		f.write('\n')
MONGO_URL = 'localhost'
MONGO_Db = 'amazon'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_Db]
try:
	for i in get_data:
		db[MONGO_COLLECTION].insert(i)
	print('nice')
except Exception as e:
	print('fuck!!!!!!')
