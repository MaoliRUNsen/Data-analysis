# 数据分析期末项目
## 项目介绍
- 项目名称：2021中国大学排名分析
- 项目简介：利用Pandas，plotly和pychart对中国大学综合排名数据进行可视化分析，让用户可根据院校类型（综合，理工，师范，农业，林业）为检索点进行大学信息查询，并提供不同省市大学数量与总分的对比分析图。
- 数据源：[软科数据](https://www.shanghairanking.cn/rankings/bcur/202111)—2021中国大学排名
## 问题表述
- 用户画象：待填报志愿的高考生
- 用户任务：了解大学信息以进行志愿填报
- 用户痛点（需求）：不了解大学的排名及各指标的得分，不了解同类型院校的排名，不清楚各省市大学的数量与排名
- 增长/益点：pandas分析，给用户提供
## 解决方案表述
- 一句话概括：利用pandas+pyechart+plotly，对大学排名信息（数据源）进行清洗与可视化，帮助高考生更好地了解大学信息以进行志愿填报
- 数据流程图DFD
![输入图片说明](https://images.gitee.com/uploads/images/2021/0702/061456_2535978b_7603827.png "1.png")
- IDEO三要素

|Viability商业可行性|此项目提供全国大学排名信息，帮助高考生更好地选择心仪合适的大学；本项目的可视化图表主要来自pyechart与plotly，均为免费的开源库，降低数据分析的成本|
|--|--|
|Feasibility技术可行性|pyechart与plotly可以生成丰富且美观的可视化图表与交互图表，并且调用难度低|
|Desirability用户可欲性|此项目可以提供丰富的可视化图表与交互图表，让用户可以更直观地看到数据的呈现形态；并且操作简单，学习成本低，方便用户使用|
## 数据分析流程及成果
- 首先导入数据分析基本模块pandas和数据源

```
import pandas as pd
# 读csv文件
df = pd.read_csv('C:/Users/喜东东/Desktop/daxue/中国大学综合排名2021.csv', encoding='gb2312')
df
```
输出：
![输入图片说明](https://images.gitee.com/uploads/images/2021/0702/071326_b6f367b4_7603827.png "微信图片_20210702071309.png")
- 仔细观察表格数据，发现数据存在空值NaN。其实不管有没有空值，都要先查看数据类型及缺失值，所以

```
## 查看数据类型
df.info()
```
- 输出：
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 582 entries, 0 to 581
Data columns (total 17 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   排名       582 non-null    int64  
 1   升/降      566 non-null    float64
 2   学校名称     582 non-null    object 
 3   英文名称     582 non-null    object 
 4   省市       582 non-null    object 
 5   类型       582 non-null    object 
 6   总分       582 non-null    float64
 7   办学层次     100 non-null    float64
 8   学科水平     100 non-null    float64
 9   办学资源     100 non-null    float64
 10  师资规模与结构  100 non-null    float64
 11  人才培养     100 non-null    float64
 12  科学研究     100 non-null    float64
 13  服务社会     100 non-null    float64
 14  学术人才     100 non-null    float64
 15  重大项目与成果  100 non-null    float64
 16  国际竞争力    100 non-null    float64
dtypes: float64(12), int64(1), object(4)
memory usage: 77.4+ KB
```
- 不难发现，在582条数据里，升/降，办学层次，学科水平，师资规模与结构，人才培养，科学研究，服务社会，学术人才，重大项目与成果，国际竞争力中都存在缺失值。为了后面更好地进行数据可视化，要先将全部空值进行填充，这里填充为0，用的是fillna的方法

```
## 将全部缺失的数据填充为0
df.fillna(0, inplace=True)
```
![输入图片说明](https://images.gitee.com/uploads/images/2021/0702/084917_71b2a5cf_7603827.png "e28362c93cdd4c83955c1d598b32dbd.png")
- 初步清洗完后，我希望可以以院校类型为参数，对大学进行分类，在这基础上再进行各省市间数量和分数的对比，以达到数据加值的目的。
- 首先看看院校类型有哪些

```
#院校类型
类型名称 = list(df.类型.dropna().unique())
类型名称
```

输出：

```
['综合', '理工', '师范', '农业', '林业']
```


- 将它们设为参数，再用groupby和agg的方法进行大学数量与平均分的分组聚合，实现交互，下面以”理工“类型为例：

```
def i(the_type):
    dfs = df.query("类型=='{}'".format(the_type))
    df_summary = dfs.groupby("省市").agg({"学校名称":"count","总分":"mean"}).sort_values(by = "总分", ascending = False)
    df_summary.columns=['学校名称','平均分']
    return df_summary 
i('理工') 
```
输出：
![输入图片说明](https://images.gitee.com/uploads/images/2021/0702/233452_36c5b3ab_7603827.png "对单词.png")
- 然后就是可视化啦，用的是iplot的方法，直接在ipython notebook里面生成图片，鼠标悬浮图表还能告诉用户相关的数值

```
#可视化
def i(the_type):
    dfs = df.query("类型=='{}'".format(the_type))
    df_summary = dfs.groupby("省市").agg({"学校名称":"count","总分":"mean"}).sort_values(by = "总分",ascending = False )
    df_summary.columns=['学校名称','平均分']
    fig = dfs.iplot(kind="bar", x="省市", y="总分", asFigure=True)
    return fig
i('理工') 
```
输出：
![输入图片说明](https://images.gitee.com/uploads/images/2021/0702/234145_524cc1e4_7603827.png "达到.png")


 **这就是整个项目大致的数据思路和核心功能，还有其他一些分析过程，可视化图表和flask网页搭建可在ipynb文档查看，这里不作细节介绍，下面展示一些可视化图表和flask网页。** 


- 各省市大学数量地图分布
![输入图片说明](https://images.gitee.com/uploads/images/2021/0702/235738_f9e60eb4_7603827.png "顶顶顶v.png")

- 各省市大学平均分柱状图
![输入图片说明](https://images.gitee.com/uploads/images/2021/0702/235937_3136edba_7603827.png "dd.png")

- 各省市大学数量和平均分
![输入图片说明](https://images.gitee.com/uploads/images/2021/0703/000032_a568f26d_7603827.png "受损的.png")

- flask网页搭建
![输入图片说明](https://images.gitee.com/uploads/images/2021/0703/000332_6d3c37ad_7603827.png "dd dd.png")








