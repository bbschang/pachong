# encoding=utf8 
#抓取小说内容


import urllib.request
import chardet
import re

def get_xiaoshuo():
	html = urllib.request.urlopen("https://www.lnwow.net/html/book/63/63454/index.html").read()
	html = html.decode('utf-8')
	#print(html)
	#print(chardet.detect(html))
	#	print(html)
	reg = r'<a href="(.+?\.html)" title="'
	reg = re.compile(reg)
	xiaoshuo_urls = reg.findall(html)
	

	xiaoshuo_urls_quan = []
	for xiaoshuo_url in xiaoshuo_urls:
		xiaoshuo_urls_quan.append("https://www.lnwow.net/html/book/63/63454/"+xiaoshuo_url)
	
	print(xiaoshuo_urls_quan)

	x=0
	for file in xiaoshuo_urls_quan:
		print(file)
		urllib.request.urlretrieve(file,'%s.html'%x)
		x=x+1


get_xiaoshuo()