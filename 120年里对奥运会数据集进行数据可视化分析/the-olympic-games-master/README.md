# The Olympic Games
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/104630_f712e9a3_7541825.png "屏幕截图.png")

## 项目介绍
* 数据分析期末项目——120年里对奥运会数据集进行数据可视化分析
* 项目人：张瑜婷
* 时间：2021.06.28

## 数据介绍
* 从1896年雅典奥运会至2016年里约热内卢奥运会120年的奥林匹克运动会的历史数据。
* athlete_events.csv：参赛运动员基本生物数据和以及获取奖牌结果。
* 数据展示：
![数据展示](https://images.gitee.com/uploads/images/2021/0628/103943_4299c3b4_7541825.png "屏幕截图.png")

## 数据分析方案
1. 分析主题：
*  奥运会运动项目分析
*  参赛者基本信息分析
*  获奖情况分析
2. 分析工具：
* 主要运用python和数据包处理数据
* 利用matplotlib、plotly、pyecharts将数据作成可视化图表


## 数据准备
#### 1.导入模块
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from plotly.graph_objs import *
import colorlover as cl

from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

import seaborn as sns
import random
import datetime
import warnings
```
#### 2.利用describe()函数对df对象进行统计变量
```
df.describe()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/105305_e1d56359_7541825.png "屏幕截图.png")
###### 从以上数据可了解到，运动员的平均年龄为25岁，平均身高175cm，平均体重70kg
#### 3.查看各列数据中的空值数量
```
df.isnull().sum()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/105618_9f6b3f51_7541825.png "屏幕截图.png")

#### 4.数据清洗
##### 对Age、Herght、Weight列数据以平均值填充空值处理
```
def change_na(x):
    return x.fillna(x.mean(),inplace=True)
change_na(df['Age'])
change_na(df['Height'])
change_na(df['Weight'])
```
---------------------------------------------------
## 数据计算处理
#### 【词云图】数据处理
1. 分组统计:计算参加Sport的数量
```
Sport参与量=df.groupby(by="Sport")["Sport"].count()
```
2. 用for循环合并数据
```
data=[z for z in zip(Sport参与量.index,Sport参与量)]
```
3. series转换为df并降序处理
```
df_sport = pd.DataFrame({'Sport':Sport参与量.index, '参与数':Sport参与量.values})
df_sport = df_sport.sort_values('参与数',ascending=False).head()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/110445_385615c3_7541825.png "屏幕截图.png")

#### 【柱状图】数据处理
1. 数据筛选
```
df_Athletics=df[df['Sport'].str.contains('Athletics')]
df_Gymnastics=df[df['Sport'].str.contains('Gymnastics')]
df_Swimming=df[df['Sport'].str.contains('Swimming')]
```
2. 数据统计计算
```
Athletics参与数=df_Athletics.groupby(by="NOC")["NOC"].count()
Gymnastics参与数=df_Gymnastics.groupby(by="NOC")["NOC"].count()
Swimming参与数=df_Swimming.groupby(by="NOC")["NOC"].count()
```
3. 重组数据
```
# 将series对象转换为dataFrame
df_A = pd.DataFrame({'国家':Athletics参与数.index, '参与数':Athletics参与数.values})
df_G = pd.DataFrame({'国家':Gymnastics参与数.index, '参与数':Gymnastics参与数.values})
df_S = pd.DataFrame({'国家':Swimming参与数.index, '参与数':Swimming参与数.values})
# 将df进行降序处理
df_A = df_A.sort_values('参与数',ascending=False).head()
df_G = df_G.sort_values('参与数',ascending=False).head()
df_S = df_S.sort_values('参与数',ascending=False).head()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/110938_c6cf5a76_7541825.png "屏幕截图.png")

#### 【饼图】数据处理
1. 删除完全相同的数据
```
Sex=df.drop_duplicates()
```
2. 分别计算参赛选手性别F、M的数量
```
Sex1=Sex.groupby(by="Sex")["Sex"].count()
# 将series转换为df
Sex_1 = pd.DataFrame({'Sex':Sex1.index, '人数':Sex1.values})
```
#### 【箱型图】数据处理
```
# 数据抽取并输出
M年龄数据=df[df["Sex"]=="M"]["Age"].to_list()
F年龄数据=df[df["Sex"]=="F"]["Age"].to_list()
Age_data=[M年龄数据,F年龄数据]
gender=["男","女"]
```
#### 【面积图】数据处理
1.  按区间切分数据
```
# 将“Year”数据输出列表
year = df['Year'].to_list()
# 设置切分区域
listBins = [1895,1915,1935 ,1955,1975,1995,2016]
# 设置切分后对应标签
listLabels = ['第一个','第二个','第三个','第四个','第五个','第六个']
# 利用pd.cut进行数据离散化切分
df['20Years'] = pd.cut(year,bins=listBins,labels=listLabels) # bins:切分区域
```
2. 以'Name','Year'为条件进行重复项删除
```
一年参与 = df.drop_duplicates(['Name','Year'],keep='first') # ‘keep’保留第一次出现的数据
```
3. 按划分年份计算男参赛者数量
```
def gender_to_numric(x):
    if x=='M':
        return 1
    if x =="F":
        return 0

一年参与['gender_M'] = 一年参与['Sex'].apply(gender_to_numric)
M = 一年参与.groupby("20Years").gender_M.sum()
M.sort_values(ascending =False)
df_m = pd.DataFrame({'20Years':M.index, '男性参赛者数量':M.values})
```
4. 按划分年份计算女参赛者数量
```
def gender_to_numric(x):
    if x=='M':
        return 0
    if x =="F":
        return 1

一年参与['gender_F'] = 一年参与['Sex'].apply(gender_to_numric)
F = 一年参与.groupby("20Years").gender_F.sum()
F.sort_values(ascending =False)
df_f = pd.DataFrame({'20Years':F.index, '女性参赛者数量':F.values})
```
5. 合并df
```
df_mf = pd.merge(df_m,df_f,on='20Years',how='left')
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/111856_d35a65a7_7541825.png "屏幕截图.png")

#### 【叠加、水平柱状图】数据处理
1. 统计各国家奖牌获取数
```
# 以NOC为分组条件对获取的总奖牌数、Gold数、Silver数、Bronze数进行统计
Medal_data = df.groupby(by="NOC")["Medal"].count()
Gold_data=(df[df["Medal"]=='Gold']).groupby(by="NOC")["Medal"].count()
Silver_data=(df[df["Medal"]=='Silver']).groupby(by="NOC")["Medal"].count()
Bronze_data=(df[df["Medal"]=='Bronze']).groupby(by="NOC")["Medal"].count()
# 将series转换为df
df_Medal = pd.DataFrame({'国家':Medal_data.index, 'Total':Medal_data.values})
df_Gold = pd.DataFrame({'国家':Gold_data.index, 'Gold':Gold_data.values})
df_Silver = pd.DataFrame({'国家':Silver_data.index, 'Silver':Silver_data.values})
df_Bronze = pd.DataFrame({'国家':Bronze_data.index, 'Bronze':Bronze_data.values})
# 对df_Medal以'Total'进行降序处理
df_Medal = df_Medal.sort_values('Total',ascending=False).head(10)
# 对df_Gold以'Gold'进行降序处理
df_Gold排 = df_Gold.sort_values('Gold',ascending=False).head()
```
2. merge（）合并数据
```
# 利用merge()函数指定how方式合并数据
df_合并 = pd.merge(df_Medal,df_Gold)
df_合并 = pd.merge(df_合并,df_Silver)
df_合并 = pd.merge(df_合并,df_Bronze)
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/112135_1a2bdfd5_7541825.png "屏幕截图.png")

#### 【折线图】数据处理
1. 以“Year”列数据进行排序（升序）
```
df0=df.sort_values(by="Year",ascending=True)
```
2. 筛选、分组统计、合并数据，空值处理
```
# 筛选包含USA、URS、GER三个国家的数据
df_USA=df0[df0['NOC'].str.contains('USA')]
df_URS=df0[df0['NOC'].str.contains('URS')]
df_GER=df0[df0['NOC'].str.contains('GER')]
# 以年份为条件进行获取金牌数的分组统计
USA_data=(df_USA[df_USA["Medal"]=='Gold']).groupby(by="Year")["Medal"].count()
URS_data=(df_URS[df_URS["Medal"]=='Gold']).groupby(by="Year")["Medal"].count()
GER_data=(df_GER[df_GER["Medal"]=='Gold']).groupby(by="Year")["Medal"].count()
# 将series转换为df
USA = pd.DataFrame({'Year':USA_data.index, 'USA_Gold':USA_data.values})
URS = pd.DataFrame({'Year':URS_data.index, 'URS_Gold':URS_data.values})
GER = pd.DataFrame({'Year':GER_data.index, 'GER_Gold':GER_data.values})
# 以merge函数的how方法合并三个df
df_合 = pd.merge(USA,URS,how='left')
df_合 = pd.merge(df_合,GER,how='left')
# 对df_合以0填充进行空缺值处理
df_合['URS_Gold'] = df_合['URS_Gold'].fillna(0)
df_合['GER_Gold'] = df_合['GER_Gold'].fillna(0)
```
3.  转换数据类型为'int32'
```
df_合['USA_Gold'] = df_合['USA_Gold'].astype('int32' , errors='ignore' )
df_合['URS_Gold'] = df_合['URS_Gold'].astype('int32' , errors='ignore' )
df_合['GER_Gold'] = df_合['GER_Gold'].astype('int32' , errors='ignore' )
df_合['Year'] = df_合['Year'].astype('int32' , errors='ignore' )
```
-------------------------------------------------------------------------
## 数据可视化分析
###  奥运会运动项目分析
### 1.运动项目汇总【词云图】
```
运动项目 = (
    WordCloud()
    # 添加图名称、数据、字体的随机大小、图像类型
    .add("运动项目",data,word_size_range=[6,100],shape="diamond")
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="运动项目汇总", title_textstyle_opts=opts.TextStyleOpts(font_size=25)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
)

运动项目.render_notebook()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/112859_09c4a02c_7541825.png "屏幕截图.png")
```
【词云图】数据分析：
1.字体越大说明出现的频率越高，即表明该运动项目越多人参与。

2.由图可得，最多人参与的运动项目分别是是Athletics（田径运动）、Gymnastics（体操）、Swimming（游泳）
```
### 2.三大热门项目的各国家参与数对比 【柱状图】
```
# 三个柱状图同理
plt.figure(figsize=(16,8))
plt.rcParams['font.sans-serif']=['SimHei'] #解决中文乱码
x=df_A['国家']
height=df_A['参与数']
plt.grid(axis="y", which="major")  # 生成虚线网格
#x、y轴标签
plt.xlabel('国家')
plt.xticks( fontsize=20)
plt.ylabel('参与数')
plt.yticks( fontsize=20)
#图表标题
plt.title('Athletics的国家参与数对比',fontsize=20)
plt.bar(x,height,width = 0.5,align='center',color = 'b',alpha=0.5,bottom=0.8)
#设置每个柱子的文本标签,format(b,',')格式化销售额为千位分隔符格式
for a,b in zip(x,height):
    plt.text(a, b,format(b,','), ha='center', va= 'bottom',fontsize=18,color = 'k',alpha=0.9)
#图例
plt.legend(['参与数'])
plt
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/113131_d98d88bc_7541825.png "屏幕截图.png")
```
【Athletics】国家参与数对比数据分析：

1.在第一热门项目Athletics中，历年来参与次数最多的国家是United States

2.国家参与数排名依次为：United States（USA）、Great Britain(GBR)、France(FRA)、Germany(GER) 、Canada(CAN)
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/113206_90939aac_7541825.png "屏幕截图.png")
```
【Gymnastics】国家参与数对比数据分析：

1.在第二热门项目Gymnastics中，历年来参与次数最多的国家是United States

2.国家参与数排名依次为：United States（USA）、France(FRA)、Italy(ITA)、Hungary(HUN)=Japan(JPN)
```
![
](https://images.gitee.com/uploads/images/2021/0628/113235_43df918f_7541825.png "屏幕截图.png")
```
【Swimming】国家参与数对比数据分析：

1.在第一热门项目Athletics中，历年来参与次数最多的国家是United States

2.国家参与数排名依次为：United States（USA）、Great Britain(GBR)、Australia(AUS)、Canada(CAN)、Japan(JPN)
```
##### 从三个柱状图中可以看到，United States同时是三大热门运动项目中参与最多的国家

###  参赛者基本信息分析
### 1.120年中参加奥运会的男女比例【饼图】
```
plt.figure(figsize=(16,8))  # 设置图像大小
labels = Sex_1['Sex'].to_list()  # 设置标签与数据
values = Sex_1['人数'].to_list()
colors = ['lightcoral','lightskyblue']   # 每一个标签饼图的颜色
explode = [0.1, 0]     # 哪一块内容需要脱离饼图凸显, 可选值0-1
plt.pie(
    values,
    textprops={'color':'#34495e',   #文本颜色
                   'fontsize':18,    #文本大小
                   'fontfamily':'Microsoft JhengHei',  },
    labels=labels,
    colors=colors,
    explode=explode,
    startangle=80,
    shadow=True,
    autopct='%1.2f%%')   # autopct='%1.1f%%'表示显示百分比
plt.rcParams['font.sans-serif']=['SimHei']   #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   #用来正常显示负号
plt.title('120年中参加奥运会的男女比例',fontsize=22) 
plt.legend(loc=4)
plt.show()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/113550_c473c681_7541825.png "屏幕截图.png")
```
【饼图】数据分析：

1.从图中我们可以看到，女性占比（F）27.57%远小于男性（M）72.43%

2.在120年里，奥运会参赛者中，男性参赛者远多于女性。
```
### 2.奥运会男女参赛者的年龄分布【箱型图】
```
from plotly.offline import iplot
y_f = df[df['Sex'] == 'F'].Age
y_m = df[df['Sex'] == 'M'].Age
trace_0 = Box(y = y_m,name="男性年龄分布")
trace_1 = Box(y = y_f,name="女性年龄分布")
data = [trace_0,trace_1]
layout = Layout(title = '奥运会男女参赛者的年龄分布')
fig = Figure(data = data,layout = layout)
iplot(fig)
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/113732_19f8ae8b_7541825.png "屏幕截图.png")
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/113808_49a90071_7541825.png "屏幕截图.png")
```
【箱型图】数据分析：

1.在男性的年龄分布中，最大年龄参赛者为97岁，最小年龄参赛者为10岁。

2.在女性的年龄分布中，最大年龄参赛者为74岁，最小年龄参赛者为11岁。
```
### 3.120年间男、女参赛者数量变化趋势【面积图】
```
x = df_mf['20Years']
y1 = df_mf['男性参赛者数量']
y2 = df_mf['女性参赛者数量']
fig = plt.figure(figsize=(12,8))   # # 设置画布大小
plt.stackplot(x,y1,y2,colors=['#F4A460','#F5DEB3'])
plt.legend(['男性参赛者数量','女性参赛者数量'],loc=6)
plt.xlabel('每20年为一个单位')   # 设置x轴标题
plt.xticks( fontsize=18)
plt.yticks( fontsize=16)
plt.title('120年间男、女参赛者的数量变化趋势')  # 设置标题
plt.show()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/113958_7ba4b426_7541825.png "屏幕截图.png")
```
【面积图】数据分析：

1. 将120年划分为6个20年，以每个20年作为一个单位对男女参赛者的数据进行分析。
2. 以上图表中展现了男、女参赛者分别占据的面积。可以看到，男参赛者数量所占面积在120年中持续大于女参赛者数量形成的面积。意味着男参赛者的数量持续高于女参赛者的数量。
3. 把握整体数据趋势。可以看到男参赛者的数据与女参赛者的数据都处于持续上升的趋势。
```
###  获奖情况分析
### 1.120年中获取奖牌数最多的Top10国家【叠加柱状图】
```
fig = plt.figure(figsize=(12,8))
plt.rcParams['font.sans-serif']=['SimHei']     # 遇到数据中有中文的时候，一定要先设置中文字体
plt.rcParams['axes.unicode_minus'] = False     # 解决坐标轴负号问题
data = df_合并
plt.bar(x=data.国家,height=data.Bronze,color='#8B4513',alpha=0.6,label='Bronze')
plt.bar(x=data.国家,height=data.Silver,bottom=data.Bronze,color='#87CEEB',alpha=0.8,label='Silver')
plt.bar(x=data.国家,height=data.Gold,bottom=data.Bronze+data.Silver,color='#FFD700',alpha=0.8,label='Gold')
plt.xticks(data.国家, fontsize=20)   #将姓名赋值给之前的x轴
plt.yticks( fontsize=18)
plt.legend(loc='upper center',ncol=3,fontsize=14)   # ncol=3是变成3列
plt.ylim([0,6000])     # 设置y轴的刻度范围
for i,j in enumerate(data.Total):
    plt.text(i,j-10,str(j),ha='center',fontsize=16)   #j-10是调整位置 但并不改变值
plt.title('120年中获取奖牌数Top10的国家', fontsize=20)
plt.grid()   #网格线
plt.show()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/114237_798b12a1_7541825.png "屏幕截图.png")
```
【叠加柱状图】数据分析：
1. 从左往右依次为获取奖牌数的国家排名。
2. 可以从图中看到USA获取奖牌数远高于其他国家，拉开较大差距，稳居第一排名。
3. 图表中每一个柱状里都将其包含的金、银、铜牌数量可视化，在了解国家获奖牌总数的同时也对其中的金银铜牌的占比有一个大概的了解。
```
### 2.120年中金牌获取最多的Top5国家 【水平柱状图】
```
fig = plt.figure(figsize=(12,8))
plt.bar(x=0,bottom=df_Gold排['国家'],height=0.5,width=df_Gold排['Gold'],orientation='horizontal',label='金牌数',color='red',alpha=0.5 )
plt.xlabel('金牌数',fontsize=20)
plt.ylabel('国家',fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(df_Gold排['国家'],rotation='45',fontsize=20)
plt.title('120年中金牌获取最多的Top5国家 ',fontsize=20,fontweight= 'bold')
plt.tight_layout()
plt.legend(loc='upper right')
for i,j in enumerate(df_Gold排['Gold']):
    plt.text(j-20,i,str(j),va='center',fontsize=20)
plt.grid()
plt.show()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/114402_6fa3c6c1_7541825.png "屏幕截图.png")
```
【水平柱状图】数据分析：
1. 从图中我们可以看到，获取金牌数最多的依次为USA、URS、GER、GBR、ITA。
2. USA在120年间获取的金牌数高达2638枚，远高于位居第二名的URS。
```
### 3.120年中金牌获取最多的Top5国家 【折线图】
```
num1=df_合['USA_Gold']
num2=df_合['URS_Gold']
num3=df_合['GER_Gold']
num4=df_合['Year']
plt.figure(figsize=(16, 8), dpi=80)   #设置图片大小
plt.plot(num4, num1, label='USA_Gold',color="#FF4500")
plt.plot(num4, num2, label='URS_Gold',color="b")
plt.plot(num4, num3, label='GER_Gold',color="g")
#设置x,y坐标
plt.xticks(num4)
plt.xticks(range(1896,2017,4))
plt.grid(alpha=0.2)   #设置网格线
plt.legend(loc="upper left",fontsize=16)
plt.title('120年间的金牌获取变化',fontsize=16)
plt.show()
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0628/114607_35ae2ab8_7541825.png "屏幕截图.png")
```
【折线图】数据分析：
1. 从水平柱状图中我们了解到获取金牌数最多的三个国家依次为USA、URS、GER。
2. 折线图展示了120年里这三个国家获取金牌的数据变化。
3. 我们可以清楚的看到，位居第一的USA并非每一次在奥运会中都是金牌获取最多的国家，但USA在120年间每一次都会获取金牌。
4. GER在120年间的奥运会里，有9次未获取金牌（1920年、1924年、1948年、1968年-1988年）。
5. URS在120年间的奥运会里，只有1952年至1988年间才获取了金牌。并在1980年获取的金牌数达到“巅峰”
```















