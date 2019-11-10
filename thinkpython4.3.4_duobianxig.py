import turtle
import math

def duobianxin(bob,length,n):

	for i in range(n):
		bob.fd(length)
		bob.lt(360/n)
	#bob.lt(3.6)

bob1 = turtle.Turtle()
bob1.speed(-1)


r = 50
bianshu = 10

bianchang = (2*math.pi*r)/bianshu

duobianxin(bob1,bianchang,bianshu)

#for i in range(1,900,2):
#	duobianxin(bob1,i,1000)


#turtle.mainloop()





