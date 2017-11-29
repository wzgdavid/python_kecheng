import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

from matplotlib.pylab import date2num
import datetime

plt.rcParams['font.sans-serif'] = ['SimHei']
hist_data = ts.get_hist_data('600848')
# 对tushare获取到的数据转换成candlestick_ohlc()方法可读取的格式
data_list = []
for dates,row in hist_data.iterrows():
    # 将时间转换为数字
    date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
    t = date2num(date_time)
    open,high,low,close = row[:4]
    datas = (t,open,high,low,close)
    data_list.append(datas)
 
# 创建子图
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
# 设置X轴刻度为日期时间
ax.xaxis_date()
plt.xticks(rotation=45)
plt.yticks()
plt.title("股票代码：601558两年K线图")
plt.xlabel("时间")
plt.ylabel("股价（元）")
mpf.candlestick_ohlc(ax,data_list,width=1.5,colorup='r',colordown='green')
plt.grid()
plt.show()