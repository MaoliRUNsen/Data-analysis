# Python数据分析期末项目展示
* 项目制作者：[**邬晓婧**](https://gitee.com/wu_xiao_jing)
* 时间：2021.06.20-2021.07.03
* [ **gitee项目文档链接** ](https://gitee.com/wu_xiao_jing/python-final)
* [ **数据分析ipynb文档链接** ](https://gitee.com/wu_xiao_jing/python-final/blob/master/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%96%87%E4%BB%B6/%E5%B9%BF%E5%B7%9E%E7%BE%8E%E9%A3%9F%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90.ipynb)

***

# 项目名称：广州美食店铺数据分析
## 一、数据分析项目MVP加/价值主张宣言
* 随着经济的快速发展以及新媒体的兴起，美食攻略、美食探店等一系列东西进入大众的眼球，而人们也会在各大平台中查找美食推荐，因此本项目做的美食店铺数据分析也是带有可行性的。
* 首先通过对广东省的各市美食店铺数量的地图分析，发现广州美食店铺数量最多，然后继续通过广州不同地区的美食店铺数据，分析美食店铺所在的地区、人均价格、菜系类别等字段，从而通过可视化图表呈现出来，帮助目标人群可以快速知道广州美食店铺的地理位置、人均价格、综合评分等信息。
## 二、问题情境的数据来源及类型
### 数据来源
* 通过在[和鲸社区](https://www.heywhale.com/home)查找得到的数据，该项目的目标在于给用户直观的数据，用数据说话增加可信度。

### 数据分析项目的问题情境说明清楚合理，展示了为啥要做
##### 用户画像
![用户画像](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/2%E7%94%A8%E6%88%B7%E7%94%BB%E5%83%8F_%E7%94%BB%E6%9D%BF%201.png)
##### 需求
使用情境|痛点|目标|
--|:--:|--:
随着经济的不断发展，人们的消费水平逐年升高，广州作为经济发达城市，不仅有越来越多博主在开始在平台分享自己吃到的美食图片，而且不少人们会经常出门吃饭/探店，但有时候就会存在不知道去哪里吃去吃什么的问题存在，而该项目就可以为目标人群提供一个美食店铺的数据分析供人们选择。|由于没有较强的数据分析，不能清楚地知道每家店铺的地址、评分、菜品质量等问题|为目标人群提供简单明了的数据分析图，供目标人群选择。|

### 数据分析项目的问题情境说明清楚合理，展示了是谁有需要解决的问题
* 选择哪个区域的美食店铺、选择店铺里的哪种菜系等问题是该数据分析可以解决的最大痛点。通过可视化的数据分析，帮助目标人群了解广州市各行政区的美食分布，为消费者推荐服务最好、人气最高的餐厅。

### 数据分析项目的问题情境说明清楚合理，展示了具有分析加价潜力的关键数据，是可以收集并分析.
* 通过在和鲸社区查找到的数据，目标给用户直观的数据，用数据说话，增加可信度。从店铺所在商圈、店铺星级、店铺人均价格、店铺美食类别等多维度多方面因素的数据进行分析广州各个行政区的美食店铺，是比较直观和全面的。

###  数据分析项目的问题情境说明清楚合理，展示了关键数据来源对问题情境的相关性
* 人均价格、口味评分以及服务评分会直接影响到顾客是否去该店铺用餐，而店铺所在商圈、店铺美食类别从多维度分析顾客选择餐厅的客观影响，因此目标人群可以通过人均价格、口味评分、店铺所在商圈、店铺美食类别做出的可视化图表从而进行选择。

### 数据分析项目的问题情境说明清楚合理，展示了关键数据类型特性对解决方案的可能影响论证
* 数据类型最终可以是地图、饼图、柱形图等，目标人群在选择美食店铺的时候可能会需要花点时间寻找、对比、统计，所以适当的时空交互将数据进行对比分析是必要的。

## 三、数据分析思路及方法
### 思路
![思路](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E6%80%9D%E8%B7%AF.png)
### 方法
* 1.首先调用广东不同城市地图信息，将美食店铺数量导入城市中，通过地图中颜色的变化观察数据更容易对比数据的变化，给用户提供想得到的信息。
* 2.调用广州地区店铺地图信息，将数据根据经纬度聚合，得到广州不同地区的数据信息。
* 3.计算广州每个行政区的美食数量，并且输入广州各个区域的名称，输入模块绘制饼图、柱状图、热力图、词云图等可视化图表，吸引用户的眼球，给用户提供想得到的信息。

## 四、数据分析流程及成果
### 数据分析流程
* 1.导入CSS样式
![CSS样式](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%AF%BC%E5%85%A5%E6%A0%B7%E5%BC%8F.png)
* 2.读取数据
![读取数据](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E8%AF%BB%E5%8F%96%E6%95%B0%E6%8D%AE.png)
* 3.合并数据集[修改 A 的（名称）为（店铺名称）,（类别）为（菜系）]
![合并数据集](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%90%88%E5%B9%B6%E6%95%B0%E6%8D%AE%E9%9B%86.png)
* 4.去除数据中的重复值
![去除重复值](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%8E%BB%E9%99%A4%E9%87%8D%E5%A4%8D%E6%95%B0%E6%8D%AE.png)
* 5.选择需要的列，查看缺失值
![缺失值](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E6%9F%A5%E7%9C%8B%E7%BC%BA%E5%A4%B1%E5%80%BC.png)
### 数据分析结果
* 做出广东美食店铺的空间地图，通过放大/缩小地图已经点击各个城市查看数据后，可以清楚看出广州的美食店铺数量是广东省最多的，由于店铺数量足够多因此可以对广州的美食店铺进行下一步的数据分析。
![广东美食](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%B9%BF%E4%B8%9C%E7%BE%8E%E9%A3%9F%E5%BA%97%E9%93%BA%E6%95%B0%E9%87%8F%E5%88%86%E5%B8%83.png)

* 做出广州美食地图分布，可以看出在广州各个区的美食店铺分布，从图中不难看出广州美食店铺基本分布在天河、越秀以及海珠三大区域，可以得出由于该三区属于较为繁荣的区域，所以美食店铺都趋向分布在该三区。
![图](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%B9%BF%E5%B7%9E%E5%90%84%E5%9C%B0%E5%8C%BA%E7%BE%8E%E9%A3%9F%E5%88%86%E5%B8%83.png)

* 做出行政区美食占比饼图，不同的颜色代表不同的区，可见饼图中紫色分布最多，他所代表的区域是天河区。对此可以得出天河区的美食店铺最多，目标人群想要探索美食店铺的时候，可以优先选择天河区，其次选择越秀区和海珠区。
![美食占比](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%B9%BF%E5%B7%9E%E5%90%84%E8%A1%8C%E6%94%BF%E5%8C%BA%E7%BE%8E%E9%A3%9F%E5%8D%A0%E6%AF%94.png)

* 做出广州美食商家分布商圈的柱状图，可以得到美食数量最多的十个商圈，根据图表可见该十大商圈分别是珠江新城、北京路、天河北、江南大道等。可供选择多，消费水平适中，是觅食的好去处，建议当用户想要去寻找美食店铺时可以优先选择这十个商圈，节省用户寻找时间为用户提供便利。
![商圈图](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%B9%BF%E5%B7%9E%E7%BE%8E%E9%A3%9F%E5%95%86%E5%AE%B6%E5%88%86%E5%B8%83%E7%9A%84%E5%95%86%E5%9C%88.png)

* 先将商家星级等级做出统计，再做出商家等级星级分布环形图，可见珠江新城、天河城/体育中心两个商圈仍然是五/四星级商家分布最多的商圈，进一步验证了该两个商圈的美食店铺可行度高，建议用户可到该两个商圈进行就餐。
![统计](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E6%98%9F%E7%BA%A7%E5%88%86%E5%B8%83.png)
![图](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%B9%BF%E5%B7%9E%E5%90%84%E5%8C%BA%E6%98%9F%E7%BA%A7%E5%95%86%E6%88%B7%E5%8D%A0%E6%AF%94.png)

* 经过对美食店铺的地理位置、等级、美食占比图做出了数据分析，接下来对美食种类做出统一分析。
* 通过对美食种类进行分类，做出广州美食种类柱形图，可见西餐、粤菜、日料、火锅是广州地区最受欢迎的菜系；湘菜、川菜的餐厅数量未上榜，说明当地人口味清淡。而广州美食店铺基本上以主食为主，但仍然有多菜系可供用户选择，这样可以满足用户不同的喜好。
* 继续对美食店铺的菜单进行分析，做出词云图，从该词云图可以得出：招牌和刺身出现的次数最多、两个词是最大的；同时还有很多不同的词汇，用户点击不同的词汇可以查看到该词出现的次数，从而猜测在多少个店铺菜单上出现过该词汇。
![图](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%B9%BF%E5%B7%9E%E7%BE%8E%E9%A3%9F%E7%A7%8D%E7%B1%BB%E5%88%86%E5%B8%83.png)
![图](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E5%B9%BF%E5%B7%9E%E7%BE%8E%E9%A3%9F%E8%AF%8D%E4%BA%91%E5%88%86%E5%B8%83%E5%9B%BE.png)

* 最后，通过对综合评分与人均价格关系进行分析，得出相关性热力图和线性图。可以得出综合评分与人均价格关系不大，不管是人均价格多高都不会直接影响到综合评分，反而综合评分是与口味评分，环境评分，服务评分有关系的。
![图](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E7%9B%B8%E5%85%B3%E6%80%A7%E7%83%AD%E5%8A%9B%E5%9B%BE.png)
![图](https://gitee.com/wu_xiao_jing/python-final/raw/master/images/%E7%BA%BF%E6%80%A7%E5%9B%BE.png)

### 总结描述
##### 通过分析广州美食店铺的数据后，经过不同方面的分析，可以得出： 
* 第一 广州餐饮的整体消费水平适中，美食的种类+分丰富，其中西餐、日料和粤.菜在人气评分及口碑方面都表现突出。
* 第二 从地理位置上看，广州的美食聚集程度较高，主要集中在天河区海珠区和越秀区，其中天河区作为广州的CBD，其商圈密集程度、菜系丰富度以及消费水平都比较高。
* 第三 在美食推荐方面，广泛探店可以考虑北京路、天河城/体育中心、珠江新城等热门商圈。

### 可行性分析
* 商业可行性：通过数据说话，经过不同层面对广州美食店铺的分析，为消费者提供更加准确的广州美食觅食建议
* 技术可行性：利用第三方在线网站数据（数据具有真实性），通过pandas数据分析进行数据清洗出报表及数据可视化 
* 用户可预性：该数据分析可帮助用户更加直观的得到需要的广州美食店铺数据，为用户提供更加精确的觅食建议 

## 五、心得总结及感谢
* 虽然一开始不知道从何下手，甚至不知道要去哪里寻找数据源及做什么可视化图，但是通过一系列查找学习后，最终还是确定了方向，做完了该项目。虽然可视化图比较多，分析的方面比较大，但是基本都是用着同一套代码理念，看似工程量巨大，但是其实不算太难，掌握原理和思维就可以很好的做出了，当然也参考了网络上一些代码和理念，对于这次的期末项目，感觉数据分析挺有意思的，可以分析出好多自己想知道的内容，虽然未能做出更加完美的数据可视化图，但是基本上可以通过该次学习到很多东西。

## 六、感谢以下内容创作者所分享的内容：  
* [matplotlib绘图教程](https://blog.csdn.net/weixin_44766179/article/details/90137496)  
* [seaborn教程](https://zhuanlan.zhihu.com/p/40303932)  
* [pandas数据重命名](https://blog.csdn.net/yangshaojun1992/article/details/106773844/)  
* [jupyter notebook主题的更改](https://blog.csdn.net/az9996/article/details/88621028)  
* [合并文件夹下的数据文件](https://www.cnblogs.com/shadrach/p/7687502.html)  
* [菜鸟sqlite教程](https://www.runoob.com/sqlite/sqlite-tutorial.html) 
* [Pandas清洗数据](https://blog.csdn.net/weixin_35702861/article/details/83094537)
* [Pandas的Series的统计函数](http://liao.cpython.org/pandas07/)
* [Pandas的数据分组-transform函数](http://liao.cpython.org/pandas31/)
* [Pandas的数据清洗-apply函数](http://liao.cpython.org/pandas24/)
* [Pandas的时间序列数据-datetime](http://liao.cpython.org/pandas32/) 
* [导出数据生成Excel文件](https://zhuanlan.zhihu.com/p/80888926)  
* [颜色搭配推荐网站字客网](https://www.fontke.com/)    
* [invalid syntax报错解决](https://www.cnblogs.com/lenfoo/p/11251517.html)  
* [和鲸社区所提供数据](https://www.heywhale.com/home/)  
* [NumPy绘图教程](https://www.runoob.com/numpy/numpy-tutorial.html)  
* [Python绘图总结(Matplotlib篇)之画布、颜色、及样式](https://blog.csdn.net/wuzlun/article/details/80059222)  
* [matplotlib可视化图表美化教程](http://www.bubuko.com/infodetail-3333299.html)  
***
