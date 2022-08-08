# 数据分析期末项目

#### 数据源：

- [和鲸社区](https://www.heywhale.com/home)。搜索超市销售数据。

#### 数据分析目标：

> 原数据 -> 整合合并数据 -> 提取关键数据
- 分析超市的销售数据。
- 获取畅销分类ID。
- 获取畅销商品ID。
- 各超市销售额占比。
- 通过matplotlib制作python可视化的各超市销售额占比的饼图。
- 将项目放到Flask框架中。

#### 数据分析结果价值宣言：

- 近些年来，国内大型连锁超市如雨后春笋般迸发，对于各个超市来说，竞争压力不可谓不大，为了拓展、保留客户，各种促销手段应运而生。"以下为国内某连锁超市的成交统计数据，针对于该数据，挖掘其中价值，为该超市的促销手段提供技术支持。

#### 数据分析结果可视化：

- 通过matplotlib制作python可视化的各超市销售额占比的饼图，分析市场占比。
- 饼图

![饼图](https://gitee.com/coldmeaning/final-project-of-data-analysis/raw/master/images/%E9%A5%BC%E5%9B%BE.png)

- 通过matplotlib制作python可视化的订单随着时间的成交变化的折线图。
- 折线图

![折线图](https://gitee.com/coldmeaning/final-project-of-data-analysis/raw/master/images/%E6%8A%98%E7%BA%BF%E5%9B%BE.png)

#### 项目介绍：

- 项目人：李懿轩
- 时间：2周
- 数据源：[和鲸社区](https://www.heywhale.com/home)。搜索超市销售数据。
- 目标：本项目分析的是超市的销售数据，并且用Flask框架通过web呈现出来。


#### 遇到的问题和解决的方法：

- **数据筛选和分析** *解决方法：查询大量文章和资料一步步解决。* 所查询的文章如下：
  - Python可视化 [链接](https://blog.csdn.net/Frank_LJiang/article/details/89363901)
  - matplotlib饼图 [链接](https://blog.csdn.net/sinat_38340111/article/details/81023230)
  - csv文件读取参数 [链接](https://www.jianshu.com/p/f80586446151)
  - group用法 [链接](https://blog.csdn.net/qq_32618817/article/details/80587228)
  - pandas表格问题 [链接](https://www.cnblogs.com/hankleo/p/11478949.html)
  - pandas去除重复项 [链接](https://blog.csdn.net/u010665216/article/details/78559091)
  
- **Flask问题** *解决方法：找到以前Python做Flask的期末项目进行参考并修改本项目。*

#### 尚未解决的问题：

- Flask显示的web页面不够好看，css使用得不好，需要多多学习。[css教程链接](https://www.w3school.com.cn/css/index.asp)

#### Flask的web页面：

- 一个有4个页面，可以通过点击按钮进行相互交互。

- 首页
![首页](https://gitee.com/coldmeaning/final-project-of-data-analysis/raw/master/images/%E9%A6%96%E9%A1%B5.png)

- 畅销分类页
![畅销分类页](https://gitee.com/coldmeaning/final-project-of-data-analysis/raw/master/images/%E7%95%85%E9%94%80%E5%88%86%E7%B1%BB%E9%A1%B5.png)

- 畅销商品页
![畅销商品页](https://gitee.com/coldmeaning/final-project-of-data-analysis/raw/master/images/%E9%94%80%E5%94%AE%E5%95%86%E5%93%81%E9%A1%B5.png)

- 销售额占比页
![销售额占比页](https://gitee.com/coldmeaning/final-project-of-data-analysis/raw/master/images/%E9%94%80%E5%94%AE%E9%A2%9D%E5%8D%A0%E6%AF%94%E9%A1%B5.png)