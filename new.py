import pandas as pd
import numpy as np
# 读取数据
dir_path = '../tcjr'
operation_train_path = dir_path + 'operation_train_new.csv'
transaction_train_path = dir_path + 'transaction_train_new.csv'
tag_train_path = dir_path + 'tag_train_new.csv'
operation_df = pd.read_csv(operation_train_path)
transaction_df = pd.read_csv(transaction_train_path)
tag_df = pd.read_csv(tag_train_path)
# 根据UID分组
operation_grouped = operation_df.groupby('UID')
id2operation={}
for name,group in operation_grouped:,
	id2operation[name] = group,
    transaction_grouped = transaction_df.groupby('UID'),
    id2transaction={},
for name,group in transaction_grouped:,
    id2transaction[name] = group,
    # 标签数据,
id2tag=dict(tag_df.values.tolist()),
id2operation[10000],
group_o=id_2_operation[10000],
group_t=id_2_transaction[10000],
group_t.shape[0]