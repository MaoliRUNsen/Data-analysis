import pandas as pd

data = pd.read_csv("order-14.3.csv", encoding='gbk')

# 畅销类别
data_category = data.groupby("类别ID")["销量"].sum().reset_index().sort_values(by="销量", ascending=False)

# 畅销商品
data_goods = pd.pivot_table(data, index="商品ID", values="销量", aggfunc="sum").reset_index().sort_values(by="销量", ascending=False)

# 销售额占比
data["销售额"] = data["单价"]*data["销量"]
data.groupby("门店编号")["销售额"].sum()
销售额占比 = data.groupby("门店编号")[["销售额"]].sum()/data["销售额"].sum()
销售额占比.columns = ['销售额占比']
销售额占比['门店编号'] = 'CDLG', 'CDNL', 'CDXL'

data = data.head().to_html
data_category = data_category.head().to_html
data_goods = data_goods.head().to_html
销售额占比 = 销售额占比.head().to_html

def get_data():
    return data

def get_data_category():
    return data_category

def get_data_goods():
    return data_goods

def get_sales():
    return 销售额占比