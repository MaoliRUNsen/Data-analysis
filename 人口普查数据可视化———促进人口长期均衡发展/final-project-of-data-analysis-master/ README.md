# 数据分析描述
- 项目人：钟莉
- 项目名称：人口普查数据可视化———促进人口长期均衡发展
- 时间：2021/07/01

## 一、数据源：raw_data 基本栏位的概述

> [国家统计局](http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/)
- 由于第七次人口普查数据并未完全公布，只发布了8个全国人口普查公报。有表格数据的只有4个公报。
- 因此，我在以下4个公报中，抓取了6个表格数据，并导出csv文件到data文件夹中。
>>1. [第七次全国人口普查公报（第三号）](http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/qgrkpcgb/202106/t20210628_1818822.html)
>>2. [第七次全国人口普查公报（第四号）](http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/qgrkpcgb/202106/t20210628_1818823.html)
>>3. [第七次全国人口普查公报（第五号）](http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/qgrkpcgb/202106/t20210628_1818824.html)
>>4. [第七次全国人口普查公报（第六号）](http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/qgrkpcgb/202106/t20210628_1818825.html)

## 二、数据分析目标
### 2.1目标
- 人口问题始终是我国面临的全局性、长期性、战略性问题，我们必须要准确了解当前人口变化的趋势性特征。
- 加强人口发展的前瞻性、战略性研究，为推动高质量发展、有针对性地制定人口相关战略和政策、促进人口长期均衡发展提供强有力的统计信息支持。
- 调整完善人口政策，推动人口结构优化，促进人口素质提升。
- 同时，为未来行业发展提供新方向，比如：老龄化问题严重，未来应更加注重老年人健康医疗行业等。  

### 2.2流程介绍
![流程介绍](https://images.gitee.com/uploads/images/2021/0704/000252_ee96b55d_7541808.png "流程介绍.png")
1. 首先，利用pandas库中的read_html方法抓取 **国家统计局** 网页中的表格型数据    
此处列举几个：
```
# 各地区人口构成
url='http://www.stats.gov.cn/tjsj/tjgb/rkpcgb/qgrkpcgb/202106/t20210628_1818822.html'
df_人口= pd.read_html(url)[1]
df_人口
```

2. 使用DataFrame对象中的loc属性和iloc属性进行数据抽取、数据的增加、修改和删除、索引设置，以获得最有价值、整洁的数据       
此处列举几个：

```
# 修改列标题
df_人口.columns = ['地区','人口数(人)','2020年比重(%)','2010年比重(%)']
# 删除行数据
df_人口.drop(index=[0,1],inplace=True)
# 更新索引
df_人口构成 =df_人口.dropna().reset_index(drop=True)

```
3. 安装Pyecharts以及相关模块，可参考以下链接
4. 根据实际情况，进一步数据分析
5. 不断调整可视化图表内容
6. 最后导出

## 三、数据分析结果价值宣言
1. 数据表明：广东省的常住人口数量最多，人口密度由黑河—腾冲线划分开，黑河—腾冲线以东占了全国96%的人口。

2. 2010至2020年广东人口增长了2千多万，黑龙江人口负增长500多万。进一步说明了人口向经济发达区域、城市群进一步集聚。

3. 注:性别比是在种群层面上研究的问题，是指族群中雄性（男性）对雌性（女性）的比率。   
数据表明，广东省的男女比例失衡最严重。东北三省的男女比例最为均衡，还出现了性别比99%的情况。    
其实，这也可以看出，劳动力流失问题。    
中国，已经成为世界上出生性别比失衡较为严重、持续时间较长的国家。

4. 国际上通常把60岁以上的人口占总人口比例达到10%，或65岁以上人口占总人口的比重达到7%作为国家或地区进入老龄化社会的标准。    
65岁及以上人口的比例超过10％表明老龄化已经非常严重了。     
然而，中国人口总数中的65岁及以上人口已经占了13.50%，老龄化非常严重。因此，国家发布三胎政策以缓解老龄化问题。

5. 北京是全国的文化中心，人才的聚集地。上海是全国的经济中心，发展历史悠久，对于人才也非常有吸引力。     
名牌大学、重点大学，也有集中扎堆的现象，主要分布在北京、上海。  

6. 北京、上海、广州、深圳是中国的超一线城市，对于人才引进都应非常重视。      
然而，广东省主要是在改革开放后经济才迅速发展，与北京、上海相比，人才资源明显不足。广东省仍需加强人才政策实施。

7. 老龄化形成的原因是多方面的。    
①有年轻劳动力流失流入问题。    
②医疗水平提高，人类寿命普遍提高。     
③新中国建立后，生育潮爆发。     
④人们生育意愿不高等。

8. 我国经济发达区域，近十四年新生人口占比较低，一方面有计划生育政策的原因，同时人们生育意愿不高等原因存在。

9. 我国15岁及以上人口平均受教育年限都在增长。充分表明了我国人们越来越重视教育，科教兴国战略实施有效，民族是非常有希望的。

## 四、数据分析结果可视化
### 4.1可视化模块介绍
- pyecharts可视化图表模块

```
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import matplotlib
from warnings import filterwarnings

import pandas as pd
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Grid
from pyecharts.charts import Pie
from pyecharts.charts import Scatter
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType
from pyecharts.globals import ThemeType, CurrentConfig
from pyecharts.faker import Faker

from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.NTERACT

from pyecharts.commons.utils import JsCode
```
### 4.2 flask网站搭建：可视化展示的结果以及数据故事的阐述
#### 4.2.1全国人口分布_地图
![1](https://images.gitee.com/uploads/images/2021/0704/001354_18d04eca_7541808.png "1.png")

#### 4.2.2中国十年增长人数_折线图
![2](https://images.gitee.com/uploads/images/2021/0704/001936_b883adfb_7541808.png "2.png")

#### 4.2.3全国人口年龄占比_饼状图
![3](https://images.gitee.com/uploads/images/2021/0704/002007_071e93d1_7541808.png "3.png")

#### 4.2.4老龄化程度对比图_柱状图、折线图
![4](https://images.gitee.com/uploads/images/2021/0704/002330_800a38c8_7541808.png "4.png")

#### 4.2.5新生一代对比图_柱状图、折线图
![5](https://images.gitee.com/uploads/images/2021/0704/002340_7adecc4e_7541808.png "5.png")

#### 4.2.6各地区人口性别构成_地图
![6](https://images.gitee.com/uploads/images/2021/0704/003634_5f5bdd92_7541808.png "6.png")

#### 4.2.7 各地区每10万人口中拥有的各类受教育程度人数_地图
![7](https://images.gitee.com/uploads/images/2021/0704/002409_c4d0632b_7541808.png "7.png")

#### 4.2.8北上广三地大学学历人数比较图_柱状图
![8](https://images.gitee.com/uploads/images/2021/0704/002419_79ec5bf2_7541808.png "8.png")

#### 4.2.9各地区15岁及以上人口平均受教育年限对比图
![9](https://images.gitee.com/uploads/images/2021/0704/002428_4f02e8b7_7541808.png "9.png")

## 五、参考链接：
1. [Python基于pandas爬取网页表格数据](https://www.jb51.net/article/186304.htm)
2. [pyecharts安装使用](https://www.jianshu.com/p/092323335b2d)
3. [pyecharts绘制地图可视化](https://www.cnblogs.com/-wenli/p/12264572.html)
4. [干货 | 使用pyecharts绘制交互式动态地图](https://zhuanlan.zhihu.com/p/83231415)
5. [from example.commons import Faker报错问题](https://www.cnblogs.com/supershuai/p/12248071.html)
6. [数据分析可视化（四）|Pyecharts制作地图的几种方法评析](https://cloud.tencent.com/developer/article/1666746)
7. [pyecharts快速上手（二）：初始化、标题、图例、提示框配置](https://blog.csdn.net/jewely/article/details/104384494)
8. [不同的 Notebook 环境有自己不同的渲染要求](https://pyecharts.org/#/zh-cn/notebook)
9. [Python绘制饼状图之可视化神器pyecharts](https://blog.csdn.net/weixin_47723732/article/details/113885493)
10. [画图时给y轴赋值使用yaxis_data时报错](https://blog.csdn.net/IT_SoftEngineer/article/details/107427069)
11. [python pyecharts数据可视化 玫瑰图、柱形图、饼图、环图](https://cloud.tencent.com/developer/article/1699670) 
12. [pyecharts](https://pyecharts.org/#/zh-cn/notebook)
13. [pyecharts 如何给柱形图的每个柱子设置不同颜色](http://wegocoding.top/article/pyecharts/)
14. [样式使用](https://v3.bootcss.com/examples/navbar-static-top/#)
15. [python数据分析——pyecharts折线图全解（小白必看）](https://blog.csdn.net/weixin_42241770/article/details/108393930)
16. [用pyecharts作图如何隐藏数值标签等数据](https://blog.csdn.net/w15059001146/article/details/106148259)     

- （悄咪咪说一句：两个 README.md文件一样的，能在线看哪个就看.....时不时说我`该文件疑似存在违规内容，无法显示`
- 数据分析ipynb文档在 _第七次人口普查数据_文件夹里
1. [抓取数据.ipynb](https://gitee.com/zhongli_07/final-project-of-data-analysis/blob/master/%E7%AC%AC%E4%B8%83%E6%AC%A1%E4%BA%BA%E5%8F%A3%E6%99%AE%E6%9F%A5%E6%95%B0%E6%8D%AE/%E6%8A%93%E5%8F%96%E6%95%B0%E6%8D%AE.ipynb)
2. [数据分析可视化.ipynb](https://gitee.com/zhongli_07/final-project-of-data-analysis/blob/master/%E7%AC%AC%E4%B8%83%E6%AC%A1%E4%BA%BA%E5%8F%A3%E6%99%AE%E6%9F%A5%E6%95%B0%E6%8D%AE/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%8F%AF%E8%A7%86%E5%8C%96.ipynb)