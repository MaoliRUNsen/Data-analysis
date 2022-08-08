from flask import Flask, render_template
from funciton import get_data, get_data_category, get_data_goods, get_sales

app = Flask(__name__)


@app.route('/')
def entry_page() -> 'html':
    title = '数据分析网站'
    data = get_data()
    return render_template('entry.html',
                           the_title=title,
                           the_data=data(classes="male", index=False))


@app.route('/get_data_category')
def category_page() -> 'html':
    title = '数据分析网站——畅销分类'
    data_category = get_data_category()
    return render_template('category.html',
                           the_title=title,
                           the_data=data_category(classes="male", index=False))


@app.route('/get_data_goods')
def goods_page() -> 'html':
    title = '数据分析网站——畅销商品'
    data_goods = get_data_goods()
    return render_template('goods.html',
                           the_title=title,
                           the_data=data_goods(classes="male", index=False))


@app.route('/get_sales')
def sales_page() -> 'html':
    title = '数据分析网站——销售额占比'
    data_goods = get_sales()
    return render_template('sales.html',
                           the_title=title,
                           the_data=data_goods(classes="male", index=False))


if __name__ == '__main__':
    app.run()
