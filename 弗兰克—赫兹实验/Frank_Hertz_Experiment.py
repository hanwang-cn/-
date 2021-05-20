from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import openpyxl
import numpy as np

plt.figure(figsize = (6.5,6.5))
book = openpyxl.load_workbook(r'C:/?/?/?/?/data.xlsx') # 替换成自己的路径
sheet = book['Data_Manual']
colunm_A_values = [cell.value for cell in sheet['A']]
column_B_values = [cell.value for cell in sheet['B']]
x = np.array(column_B_values)
y = np.array(colunm_A_values)
x_new = np.linspace(x.min(), x.max(), 300000)
y_smooth = make_interp_spline(x, y)(x_new)
plt.plot(x_new, y_smooth, c='black')
plt.plot(column_B_values, colunm_A_values, linestyle = '-', alpha = 0.5, marker = 'o',markersize = 6, c='red')
plt.title('Frank-Hertz Experiment', fontsize = 18)
plt.xlabel('Voltage (V)', fontsize = 12)
plt.ylabel('Electric current (x10^-9 A)', fontsize = 12)
plt.grid(linestyle ='-.')
plt.show()
