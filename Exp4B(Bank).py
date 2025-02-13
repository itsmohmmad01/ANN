import numpy as np
x1=[600,780]
x2=[30000,60000]
x3=[0,1]
xn=int(input("enter credit score"))

In=int(input("enter annual income"))
xcred=(xn-min(x1))/(max(x1)-min(x1))
print(xcred)
xin=(In-min(x2))/(max(x2)-min(x2))
print(xin)

b=np.random.rand()
y=1*xcred+0.5*xin+b
if(y>0):
  print("loan is not approved")
else:
    print("loan is approved")
