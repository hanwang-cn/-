# NUM1是CH1的振幅，NUM2是CH2的振幅
# PHI1是CH1的初相位，PHI2是CH2的初相位
# 直接修改这四个参数即可获得莉萨如图形
# 文件的执行需要numpy和matplotlib的支持，没有相关支持的话需要安装。
# 推荐使用PyCharm（有安装Anaconda）执行该文件。

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (5,5))
x=[]
y=[]
a=np.linspace(-6*(np.pi),6*(np.pi),120000)
def f1(x):
    y=np.sin(NUM1*x+PHI1)
    return y
def f2(x):
    y=np.sin(NUM2*x+PHI2)
    return y
for i in a:
    x.append(f1(i))
    y.append(f2(i))
plt.plot(x,y)
plt.title("Lissajous Figures")
plt.xlabel('CH1')
plt.ylabel('CH2')
plt.xlim((-1,1))
plt.ylim((-1,1))
plt.show()
