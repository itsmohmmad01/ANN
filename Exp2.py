import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])
m=0
b=0
rate=0.01
iteration=5
n=len(x)
for i in range(iteration):
    y_pref=m*x+b
    m-=rate*(2/n)*np.sum((y_pref-y)*x)
    b-=rate*(2/n)*np.sum(y_pref-y)
    print(f"{b:2f}")
