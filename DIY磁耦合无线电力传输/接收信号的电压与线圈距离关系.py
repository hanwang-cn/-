import matplotlib.pyplot as plt
import numpy as np
# from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline
plt.figure(figsize = (7,7))
x = np.array([2.35,4.73,5.97,7.24,8.47,9.25,11.23,13.21,16.51])
y = np.array([2.4,4.8,6.8,8.8,10.0,9.4,7.1,5.2,2.8])
#上面的实验数据换成自己的实验数据，就能生成图片，现在是九组实验数据。
x_new = np.linspace(x.min(),x.max(),300000) #300 represents number of points to make between T.min and T.max
y_smooth = make_interp_spline(x, y)(x_new)
plt.scatter(x, y, c='black',alpha = 0.5) 
plt.plot(x_new,y_smooth,c='red')
 
plt.rcParams['font.sans-serif'] = ['SimHei']  #SimHei黑体
plt.rcParams['axes.unicode_minus'] = False
 
plt.title("接收信号的电压与线圈距离关系", fontsize=24)#标题及字号
plt.xlabel("距离（cm）", fontsize=24)
plt.ylabel("峰-峰值（V）", fontsize=24)
plt.tick_params(axis='both', labelsize=14)#刻度大小
plt.grid(linestyle='-.')
plt.show()
 
#plt.save('squares_plot.png'（文件名）, bbox_inches='tight'（将图表多余的空白部分剪掉）)
#用它替换plt.show实现自动保存图表
