import math

def shujia(dianjia,zhekou,shuliang):
	zongjia=0

	if shuliang>0:
		zongjia = dianjia*zhekou*shuliang+3+0.75*(shuliang-1)
	else:
		return("shuliangbihefa")
	return zongjia

shujia1 = shujia(30,0.8,20)
shujia2 = shujia(1,0.9,100)
shujia3 = shujia(100,0.5,20)
shujia4 = shujia(100,0.5,0)
print(shujia1,shujia2,shujia3,shujia4)