from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go

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




app = Flask(__name__)



@app.route('/',methods=['GET'])
def entry_page() -> 'html':
	population = pd.read_csv('data/各地区人口构成数据.csv')
	# 删掉全国的数据
	population.drop(index=[0],inplace=True)
	x_data = population['地区'].tolist()
	y_data = population['人口数(人)'].tolist()

	m = Map()
	m.add('',[list(z) for z in zip(x_data,y_data)],maptype = 'china',is_map_symbol_show=False)
	m.set_series_opts(label_opts = opts.LabelOpts(is_show=True))
	m.set_global_opts(title_opts = opts.TitleOpts(title = '全国人口分布地图',
		subtitle = '此为2020年全国第七次人口普查有关数据，以下所有皆为常住人口的数据。\n\n全国人口共141178万人。\n\n由图表看出：2020年广东省的常住人口数量最多，人口密度仍然是由黑河—腾冲线划分开，黑河—腾冲线以东占了全国96%的人口',),
	visualmap_opts = opts.VisualMapOpts(min_=population['人口数(人)'].min(),max_=population['人口数(人)'].max(),
	range_color=['#C2E7C0','#61BDCD','#0D6DAE']))
	m.render('templates/全国人口分布地图.html')

	population.drop(columns='Unnamed: 0',inplace=True)       #删除列
	population_all = population.to_html()

	with open("templates/全国人口分布地图.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = population_all,
    	the_title='全国人口分布地图')


@app.route('/grow',methods=['GET'])
def entry_page2() -> 'html':
	population1 = pd.read_csv('data/2010与2020各地区人口构成数据.csv')

	line=(
	    Line()
	    .add_xaxis(xaxis_data=population1['地区'].tolist())
	    .add_yaxis(series_name="十年增长人数",y_axis=population1['10年增长人数'].tolist(), is_smooth=True)
	#     .add_yaxis(series_name="y2线",y_axis=population1.head()['人口数(人)'], is_smooth=True)
	    .set_global_opts(title_opts=opts.TitleOpts(title="中国十年增长人数折线图",
	                                               subtitle="数据表明，2010至2020年广东人口增长了2千多万，黑龙江人口负增长500多万。\n进一步说明了人口向经济发达区域、城市群进一步集聚。",
	                                               title_textstyle_opts=opts.TextStyleOpts(font_size=25,), 
	                                               pos_left="center", pos_top="0",),
	                     
	                     legend_opts=opts.LegendOpts(orient="vertical", pos_top="35%", pos_left="80%"))
	    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
	    .render('templates/中国十年增长人数折线图.html')
	)
	population1.drop(columns='Unnamed: 0',inplace=True)       #删除列
	population1_all = population1.to_html()

	with open("templates/中国十年增长人数折线图.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = population1_all,
    	the_title='中国十年增长人数折线图')





@app.route('/gender',methods=['GET'])
def entry_page4() -> 'html':
	gender = pd.read_csv('data/各地区人口性别构成数据.csv')
	x_data = gender['地区'].tolist()
	y_data = gender['性别比(%)'].tolist()

	m = Map()
	m.add('',[list(z) for z in zip(x_data,y_data)],maptype = 'china',is_map_symbol_show=False)
	m.set_series_opts(label_opts = opts.LabelOpts(is_show=True))
	m.set_global_opts(title_opts = opts.TitleOpts(title = '全国人口性别比地图', 
	                                              subtitle = "注:性别比是在种群层面上研究的问题，是指族群中雄性（男性）对雌性（女性）的比率。\n\n数据表明，广东省的男女比例失衡最严重。东北三省的男女比例最为均衡。\n其实，这也可以看出，劳动力流失问题。\n中国，已经成为世界上出生性别比失衡较为严重、持续时间较长的国家。"),
	                  
	visualmap_opts = opts.VisualMapOpts(min_=gender['性别比(%)'].min(),max_=gender['性别比(%)'].max(),
	range_color=['#FF99CC','#CC99CC','#CC3399']))
	m.render('templates/全国人口性别比地图.html')

	gender.drop(columns='Unnamed: 0',inplace=True)       #删除列
	gender_all = gender.to_html()

	with open("templates/全国人口性别比地图.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = gender_all,
    	the_title='全国人口性别比地图')




@app.route('/age',methods=['GET'])
def entry_page3() -> 'html':
	age_country = pd.read_csv('data/全国人口年龄构成数据.csv')
	# 删掉总计的数据
	age_country.drop(index=[0],inplace=True)

	x_data = age_country['年龄'].tolist()
	y_data = age_country['比重(%)'].tolist()
	c = (
	    Pie()
	    .add("", [list(z) for z in zip(x_data,y_data)],
	         # 调整饼图位置
	         center=["50%", "60%"])
	    .set_series_opts(label_opts = opts.LabelOpts(is_show=True))
	    .set_global_opts(title_opts=opts.TitleOpts(title="全国人口年龄占比饼状图",
	                                              subtitle ="国际上通常把60岁以上的人口占总人口比例达到10%，或65岁以上人口占总人口的比重达到7%作为国家或地区进入老龄化社会的标准。 \n65岁及以上人口的比例超过10％表明老龄化已经非常严重了。\n\n然而，中国人口总数中的65岁及以上人口已经占了13.50%，老龄化非常严重。因此，国家发布三胎政策以缓解老龄化问题。",
	                                              pos_top="0",),
	    legend_opts=opts.LegendOpts(orient="vertical", pos_top="35%", pos_left="2%"),)
	    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
	    .render("templates/全国人口年龄占比饼状图.html")
	)

	age_country.drop(columns='Unnamed: 0',inplace=True)       #删除列
	age_country_all = age_country.to_html()

	with open("templates/全国人口年龄占比饼状图.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = age_country_all,
    	the_title='全国人口年龄占比饼状图')


@app.route('/age_region1',methods=['GET'])
def entry_page8() -> 'html':
	age_region = pd.read_csv('data/各地区人口年龄构成数据.csv')
	# 删掉全国的数据
	age_region.drop(index=[0],inplace=True)
	# 排序
	age_region.sort_values(by='其中65岁及以上比重(%)',inplace=True,ascending=False)
	# 更新索引
	age_region.dropna().reset_index(drop=True)
	# 提取前五个和后五个数据
	age_region1 = age_region.iloc[[0,1,2,3,4,26,27,28,29,30]]

	color_function = """
	        function (params) {
	            if (params.value < 16) 
	                return '#66CC99';
	            else return '#009999';
	        }
	        """

	bar = (
	    Bar()
	    .add_xaxis(age_region1['地区'].tolist())      # x轴
	    .add_yaxis(series_name="65岁及以上人口占比", y_axis=age_region1['其中65岁及以上比重(%)'].tolist(),itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))

	#     .reversal_axis()   # xy轴交换
	    .set_global_opts(
	        title_opts=opts.TitleOpts(title='老龄化程度对比图',
	                                  subtitle='此表格选取各五个老龄化程度最重与最轻的数据，老龄化形成的原因是多方面的。\n\n①有年轻劳动力流失流入问题。\n\n②医疗水平提高，人类寿命普遍提高。\n\n③新中国建立后，生育潮爆发。\n\n④人们生育意愿不高等。', 
	                                  title_textstyle_opts=opts.TextStyleOpts(), pos_left="50%", pos_top="0",
	                                  ),
	        legend_opts=opts.LegendOpts(orient="vertical", pos_top="35%", pos_right="0%"),
	    )

	)


	line = (
	    Line()
	    .add_xaxis(age_region1['地区'].tolist())      # x轴
	    .add_yaxis(series_name="老龄化程度", y_axis=age_region1['其中65岁及以上比重(%)'].tolist(),color=["#336699"])
	    .set_series_opts(label_opts = opts.LabelOpts(is_show=False))
	    
	)

	bar.overlap(line).render("templates/老龄化程度对比图.html")

	age_region1.drop(columns='Unnamed: 0',inplace=True)       #删除列
	age_region1_all = age_region1.to_html()



	with open("templates/老龄化程度对比图.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = age_region1_all,
    	the_title='老龄化程度对比图')


@app.route('/age_region2',methods=['GET'])
def entry_page9() -> 'html':
	age_region = pd.read_csv('data/各地区人口年龄构成数据.csv')
	# 删掉全国的数据
	age_region.drop(index=[0],inplace=True)
	# 排序
	age_region.sort_values(by='0-14岁比重(%)',inplace=True,ascending=False)
	# 更新索引
	age_region.dropna().reset_index(drop=True)
	# 提取前五个和后五个数据
	age_region2 = age_region.iloc[[0,1,2,3,4,26,27,28,29,30]]

	color_function = """
	        function (params) {
	            if (params.value < 20) 
	                return '#99CC99';
	            else return '#FFCC99';
	        }
	        """

	bar = (
	    Bar()
	    .add_xaxis(age_region2['地区'].tolist())      # x轴
	    .add_yaxis(series_name="0-14岁人口占比", y_axis=age_region2['0-14岁比重(%)'].tolist(),itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))

	#     .reversal_axis()   # xy轴交换
	    .set_global_opts(
	        title_opts=opts.TitleOpts(title='地区新生比重对比图',
	                                  subtitle='此表格选取各地区0-14岁人口占比最大与最小的数据。\n\n由图表看出，我国经济发达区域，近十四年新生人口占比较低。\n\n一方面有计划生育政策的原因，同时人们生育意愿不高等原因存在。', 
	                                  title_textstyle_opts=opts.TextStyleOpts(), pos_left="50%", pos_top="0",
	                                  ),
	        legend_opts=opts.LegendOpts(orient="vertical", pos_top="35%", pos_right="0%"),
	    )

	)


	line = (
	    Line()
	    .add_xaxis(age_region2['地区'].tolist())      # x轴
	    .add_yaxis(series_name="0-14岁人口占比", y_axis=age_region2['0-14岁比重(%)'].tolist(),color=["#99CC99"])
	    .set_series_opts(label_opts = opts.LabelOpts(is_show=False))
	    
	)

	bar.overlap(line).render("templates/地区新生比重对比图.html")

	age_region2.drop(columns='Unnamed: 0',inplace=True)       #删除列
	age_region2_all = age_region2.to_html()



	with open("templates/地区新生比重对比图.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = age_region2_all,
    	the_title='地区新生比重对比图')




@app.route('/education',methods=['GET'])
def entry_page5() -> 'html':
	education = pd.read_csv('data/各地区每10万人口中拥有的各类受教育程度人数数据.csv')
	# 删掉全国的数据
	education.drop(index=[0],inplace=True)

	# 绘制全国各地每10人中大学以上的人数，以地图展示
	x_data = education['地区'].tolist()
	y_data = education['大学（大专及以上）'].tolist()

	m = Map()
	m.add('',[list(z) for z in zip(x_data,y_data)],maptype = 'china',is_map_symbol_show=False)
	m.set_series_opts(label_opts = opts.LabelOpts(is_show=True))
	m.set_global_opts(title_opts = opts.TitleOpts(title = '全国各地每10万人中大学以上学历的人口分布',
		subtitle='北京是全国的文化中心，人才的聚集地。\n\n上海是全国的经济中心，发展历史悠久，对于人才也非常有吸引力。名牌大学、重点大学，也有集中扎堆的现象，主要分布在北京、上海。', ),
	visualmap_opts = opts.VisualMapOpts(min_=education['大学（大专及以上）'].min(),max_=education['大学（大专及以上）'].max(),range_color=['#FFFF99','#99CC99','#666600']))
	m.render('templates/各地每10万人中大学以上学历的人口分布.html')

	education.drop(columns='Unnamed: 0',inplace=True)       #删除列
	education_all = education.to_html()



	with open("templates/各地每10万人中大学以上学历的人口分布.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = education_all,
    	the_title='全国人口年龄占比饼状图')



@app.route('/education_3',methods=['GET'])
def entry_page6() -> 'html':
	education = pd.read_csv('data/各地区每10万人口中拥有的各类受教育程度人数数据.csv')
	# 抽取出北京、上海、广东个地区进行分析
	education_3 = education.iloc[[1,9,19]]
	education_3

	# 指定柱子颜色的js代码
	color_function = """
	        function (params) {
	            if (params.value < 20000) 
	                return '#66CC99';
	            else if (params.value > 30000 && params.value < 35000) 
	                return '#66CCCC';
	            else return '#009999';
	        }
	        """

	b = (
	    Bar()
	    .add_xaxis(education_3['地区'].tolist())      # x轴
	    .add_yaxis(series_name="三地比较", y_axis=education_3['大学（大专及以上）'].tolist(),itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))

	#     .reversal_axis()   # xy轴交换
	    .set_global_opts(
	        title_opts=opts.TitleOpts(title='北上广三地大学学历人数比较图',
	                                  subtitle='北京、上海、广州、深圳是中国的超一线城市，对于人才引进都应非常重视。\n\n然而，广东省主要是在改革开放后经济才迅速发展，与北京、上海相比，人才资源明显不足。\n\n广东省仍需加强人才政策实施。', 
	                                  title_textstyle_opts=opts.TextStyleOpts(), pos_left="center", pos_top="0",),
	        legend_opts=opts.LegendOpts(orient="vertical", pos_top="35%", pos_right="0%"),
	    )
	    .render("templates/北上广三地大学学历人数比较图.html")
	)

	education_3.drop(columns='Unnamed: 0',inplace=True)       #删除列
	education_3_all = education_3.to_html()



	with open("templates/北上广三地大学学历人数比较图.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = education_3_all,
    	the_title='北上广三地大学学历人数比较图')



@app.route('/education_year',methods=['GET'])
def entry_page7() -> 'html':
	education_year = pd.read_csv('data/各地区15岁及以上人口平均受教育年限.csv')

	b = (
	    Bar(
	#         init_opts=opts.InitOpts(           # 初始配置项
	#             theme=ThemeType.MACARONS,
	#             animation_opts=opts.AnimationOpts(
	#                 animation_delay=1000, animation_easing="cubicOut"   # 初始动画延迟和缓动效果
	#             ))
	        )
	    # 选取表格中前五个数据
	    .add_xaxis(xaxis_data=education_year.head()['地区'].tolist())      # x轴
	    .add_yaxis(series_name="2010年", y_axis=education_year.head()['2010年'].tolist(),color=["#336699"])       # y轴
	    .add_yaxis(series_name="2020年", y_axis=education_year.head()['2020年'].tolist(),color=["#99CC33"])       # y轴
	    .set_global_opts(
	        title_opts=opts.TitleOpts(title='15岁及以上人口平均受教育年限对比图',
	                                  subtitle='此表格选取前五个数据，各地区15岁及以上人口平均受教育年限都在增长。 \n\n表明了我国人们越来越重视教育，科教兴国战略实施有效，民族是非常有希望的。', 
	                                  title_textstyle_opts=opts.TextStyleOpts(), pos_left="center", pos_top="0",
	                                  ),
	        legend_opts=opts.LegendOpts(orient="vertical", pos_top="35%", pos_right="0%"),
	        xaxis_opts=opts.AxisOpts(name='地区', axislabel_opts=opts.LabelOpts(rotate=0)),  # 设置x名称和Label rotate解决标签名字过长使用
	        yaxis_opts=opts.AxisOpts(name='15岁及以上人口平均受教育年限'),

	    )
    .render("templates/教育年限对比.html")
)

	education_year.drop(columns='Unnamed: 0',inplace=True)       #删除列
	education_year_all = education_year.to_html()



	with open("templates/教育年限对比.html", encoding="utf8", mode="r") as f:
		plot_all = "".join(f.readlines())

	return render_template('美妙样式.html',
    	the_plot_all = plot_all,
    	data = education_year_all,
    	the_title='15岁及以上人口平均受教育年限对比图')





if __name__ == '__main__':
    app.run(debug=True)
