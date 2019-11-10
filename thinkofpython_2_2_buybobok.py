import math

def shichang(jiezhou_feng,jiezhou_miao,lucheng):
	huanshuan = 1.609344
	lucheng = lucheng*huanshuan*1000
	return lucheng/(1000/(jiezhou_feng*60+jiezhou_miao))  #例：节奏是8分15秒，

print(shichang(8,15,20))
