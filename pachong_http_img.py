#pachong_http_jpg.py  程序用来爬取指定链接中以src开头的.jpg结尾的图片

import urllib.request
import chardet
import re


page = urllib.request.urlopen("http://www.meituba.com/yijing/18166.html")

html_code = page.read()

#print(html_code)

#print(chardet.detect(html_code))
date = html_code.decode('UTF-8')

page_file = open('page_code.txt','wb')
page_file.write(html_code)
page_file.close()

reg = r'src="(.+?\.jpg)"'
reg_img = re.compile(reg)
img_list = reg_img.findall(date)


x=0
for img in img_list:
	print(img)
	urllib.request.urlretrieve(img,'../temp/%s.jpg'%x)
	x=x+1
