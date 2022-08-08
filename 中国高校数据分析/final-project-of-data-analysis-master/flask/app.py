from flask import Flask, render_template, request
import pandas as pd 
import cufflinks as cf
from collections import Counter
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
from pyecharts.charts import Pie
from pyecharts.charts import Bar, Timeline


app = Flask(__name__)

# 读取数据
df_学校 = pd.read_csv('data/school.csv',encoding='gbk')
df_专业 = pd.read_csv('data/professional.csv',encoding='gbk')
cf.set_config_file(offline=True, theme="ggplot")
df_学校.drop(['归属','开设专业链接'],axis=1,inplace=True)

@app.route('/')
def shouye():
	return render_template('shouye.html')


@app.route('/province_school_counts')
def province_school_counts():
	province = list(df_学校["省份"])
	province_学校数量 = dict(Counter(province))
	省份_list = list(province_学校数量.keys())
	学校数量_list = list(province_学校数量.values())
	# 各省学校数量汇总表格
	df_各省学校数量 = pd.DataFrame({'省份':省份_list,'学校数量':学校数量_list}).to_html()
	# 各省学校表格
	province_学校 = df_学校.groupby(['省份','学校']).sum().to_html()
	# 交互式可视化图表
	p = 省份_list
	v = 学校数量_list
	c = (
	    Map(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	    .add("", [list(z) for z in zip(p,v)], "china")
	    .set_global_opts(
	        title_opts=opts.TitleOpts(title="高校分布地区"),
	        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
	    )
	)
	tu = c.render_embed()
	return render_template('province_school_counts.html',tu = tu,data1 = df_各省学校数量,data2 = province_学校)



@app.route('/ben_zhuang')
def ben_zhuang():
	df_本专科数量 = df_学校['水平层次'].value_counts().reset_index()
	df_本专科数量.rename(columns = {'index':'水平层次','水平层次':'数量'},inplace = True)
	l = list(df_本专科数量['水平层次'])
	v = list(df_本专科数量['数量'])
	c = (
	    Pie(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	    .add(
	        "",
	        [list(z) for z in zip(l,v)],
	        radius=["40%", "75%"],
	    )
	    .set_global_opts(
	        title_opts=opts.TitleOpts(title="本/专科占比"),
	        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
	    )
	    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
	)
	tu = c.render_embed()
	# 本专科数量汇总表
	df_本专科数量 = df_本专科数量.to_html()
	# 本专科学校总览表
	df_本专科学校 = df_学校.groupby(['水平层次','学校']).sum().to_html()
	return render_template('ben_zhuang.html',tu = tu,data1 = df_本专科数量,data2 = df_本专科学校)



@app.route('/banxueleibie')
def banxueleibie():
	df_办学类别数量 = df_学校['办学类别'].value_counts().reset_index()
	df_办学类别数量.rename(columns = {'index':'办学类别','办学类别':'数量'},inplace = True)
	l = list(df_办学类别数量['办学类别'])
	v = list(df_办学类别数量['数量'])
	c = (
	    Pie(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	    .add(
	        "",
	        [list(z) for z in zip(l,v)],
	    )
	    .set_global_opts(
	        title_opts=opts.TitleOpts(title="办学类别占比"),
	        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
	    )
	    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
	)
	tu = c.render_embed()
	# 办学类别数量汇总表
	df_办学类别数量 = df_办学类别数量.to_html()
	# 办学类别学校总览表
	df_办学类别学校 = df_学校.groupby(['办学类别','学校']).sum().to_html()

	return render_template('banxueleibie.html',tu = tu,data1 = df_办学类别数量,data2 = df_办学类别学校)


@app.route('/zhongdianyuanxiaosl')
def zhongdianyuanxiaosl():
	su_985 = df_学校[df_学校['985'] == '是'].shape[0]
	su_211 = df_学校[df_学校['211'] == '是'].shape[0]
	su_yiliu = int(df_学校['双一流'].value_counts().values[0])
	重点院校类别_list = ['985','211','双一流']
	重点院校数量_list = [su_985,su_211,su_yiliu]
	df_重点院校数量 = pd.DataFrame({'重点院校类别':重点院校类别_list,'重点院校数量':重点院校数量_list})
	c = (
	    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	    .add_xaxis(['985','211','双一流'])
	    .add_yaxis("",[su_985,su_211,su_yiliu])
	    .set_global_opts(title_opts=opts.TitleOpts(title="重点大学数量对比"))

	)
	tu = c.render_embed()
	df_重点院校数量 = df_重点院校数量.to_html()
	return render_template('zhongdianyuanxiaosl.html',tu = tu,data = df_重点院校数量)


@app.route('/zhongdianyuanxiaofb')
def zhongdianyuanxiaofb():
	tl = Timeline(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	for i in ['985','211','双一流']:
	    p_v = df_学校[df_学校[i] == '是']
	    p_v = p_v['省份'].value_counts().reset_index()[:10]
	    p = list(p_v['index'])[::-1]
	    v = list(p_v['省份'])[::-1]
	    bar = (
	        Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	        .add_xaxis(p)
	        .add_yaxis("数量",v, label_opts=opts.LabelOpts(position="right"))
	        .reversal_axis()
	        .set_global_opts(
	            title_opts=opts.TitleOpts("重点大学分布轮播图".format(i))
	        )
	    )
	    tl.add(bar, "{}".format(i))
	tu = tl.render_embed()
	# 985学校统计表
	df_985 = df_学校[df_学校['985'] == '是']
	df_985学校及分布 = df_985.groupby(['省份','学校']).sum().to_html()
	# 211学校统计表
	df_211 = df_学校[df_学校['211'] == '是']
	df_211学校及分布 = df_211.groupby(['省份','学校']).sum().to_html()
	# 双一流学校统计表
	df_双一流 = df_学校[df_学校['双一流'] == '是']
	df_双一流学校及分布 = df_双一流.groupby(['省份','学校']).sum().to_html()

	return render_template('zhongdianyuanxiaofb.html',tu = tu,data1 = df_985学校及分布,data2 = df_211学校及分布,data3 = df_双一流学校及分布)


@app.route('/zhuanye_top20')
def zhuanye_top20():
	top20 = df_专业['专业名称'].value_counts().reset_index()
	专业名称 = list(top20['index'])[:20]
	数量 = list(top20['专业名称'])[:20]
	df_top20专业 = pd.DataFrame({'专业名称':专业名称,'开设总数':数量}).to_html()
	c = (
	    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	    .add_xaxis(
	        专业名称
	    )
	    .add_yaxis("", 数量)
	    .set_global_opts(
	        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
	        title_opts=opts.TitleOpts(title="开设专业top20"),
	    )
	)
	tu = c.render_embed()

	return render_template('zhuanye_top20.html',tu = tu,data = df_top20专业)


@app.route('/tesezhuanye')
def tesezhuanye():
	tese = df_专业[df_专业['国家特色专业'] == '是']
	tese = tese.groupby('学校').count()['国家特色专业'].reset_index()
	tese = tese.sort_values(by='国家特色专业',ascending=False)
	school = list(tese['学校'])[:20]
	values = list(tese['国家特色专业'])[:20]
	c = (
	    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
	    .add_xaxis(
	        school
	    )
	    .add_yaxis("", values)
	    .set_global_opts(
	        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
	        title_opts=opts.TitleOpts(title="特色专业top20"),
	    )
	)
	tu = c.render_embed()
	tese = tese.to_html()
	return render_template('tesezhuanye.html',tu = tu,data = tese)









if __name__ == '__main__':
    app.run(debug=True)