#导入必要的包
import pandas as pd
import numpy as np

inf_value = -1
def fill_inf(train_data,test_data):
    train_data[np.isinf(train_data)] = inf_value
    test_data[np.isinf(test_data)] = inf_value
    return train_data,test_data

def del_singular_feature(train_data,test_data):
    #删除特征
    train_data = train_data.drop(['year_of_birth','customer_id','mobileno_flag', 'idcard_flag', 'disbursed_date'],axis=1)
    test_data = test_data.drop(['year_of_birth','customer_id','mobileno_flag', 'idcard_flag', 'disbursed_date'],axis=1)
    return train_data,test_data