import math

def sale_of_book(yuanjia,zhekou,yunfai,houzhekou,shuliang):
	zongjia = 0
	if shuliang>=1 and shuliang <=10000000000:
		zhehou = yuanjia*zhekou
		yunjia = yunfai+(shuliang-1)*houzhekou
		zongjia = shuliang*zhehou+yunjia
	else:
		return "shuliang feifa"
	return zongjia

zhongjia = sale_of_book(24.95,0.6,3,0.75,60)
zhongjia2 = sale_of_book(24.95,0.6,3,0.75,1)
zhongjia3 = sale_of_book(24.95,0.6,3,0.75,0)
zhongjia4 = sale_of_book(24.95,0.6,3,0.75,1000000000000000000)

print(zhongjia,zhongjia2,zhongjia3,zhongjia4)