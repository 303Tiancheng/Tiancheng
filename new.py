import pandas as pd
import numpy as np
# 读取数据
dir_path = '../tcjr/'
operation_train_path = dir_path + 'operation_train_new.csv'
transaction_train_path = dir_path + 'transaction_train_new.csv'
tag_train_path = dir_path + 'tag_train_new.csv'
operation_df = pd.read_csv(operation_train_path)
transaction_df = pd.read_csv(transaction_train_path)
tag_df = pd.read_csv(tag_train_path)
# 根据UID分组
operation_grouped = operation_df.groupby('UID')
transaction_grouped = transaction_df.groupby('UID')
id2transaction={}
id2operation={}
for name,group in operation_grouped:
    id2operation[name] = group
    


for name,group in transaction_grouped:
    id2transaction[name] = group
# 标签数据,
id2tag=dict(tag_df.values.tolist())


# 特征模板，输入某个UID对应的grouop，返回list
# 下面这个特征抽取函数将每个UID对应的记录条数作为一个一维特征
def records_amount(group)
    features = []
    features.append(group.shape[0])
    return features