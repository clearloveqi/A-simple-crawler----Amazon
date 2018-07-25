from selenium import webdriver
from pyquery import PyQuery as pq


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


def get_url(doc):
	urs = doc('#zg_browseRoot ul li').items()
	# print(urs)
	urls = []
	for i in urs:
		get = {}
		get['href'] = i('a').attr('href')
		get['name'] = i.text()
		urls.append(get)
	return urls


with open('/home/just_study/Desktop/sth/zg_bs_tab.txt', 'r') as f:
	reads = f.readlines()
	for i in reads:  
		# print(type(i))  # 注意：此时i为str类型
		t = eval(i)  # eval讲str转换为dict
		# print(type(i))  # 此时i为dict
		# print(t['href'])
		href = []
		name = []
		href.append(t['href'])
		name.append(t['name'])
		for us in href:
			url = str(us)
			get_doc = get_pq(url)
			get_urls = get_url(get_doc)
			# for x in get_urls:
			# 	with open('/home/just_study/Desktop/sth/zg_bs_tab.txt', 'a+') as f:
			# 		f.write(repr(x))
			# 		f.write('\n')
			# 此处两种方式结果是不一样的
			# open在for循环之中的时候，每次都是清空之后打开文件写入文本，所以只会有最后一个
			url_name = '/home/just_study/Desktop/sth/'+str(name)+'.txt'
			with open(url_name, 'w+') as f:
				for x in get_urls:
					f.write(repr(x))
					f.write('\n')
