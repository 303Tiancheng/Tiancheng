import pandas as pd
import numpy as np

dir_path = 'C:/Users/Yuetong/DataSet/tcjr/'
operation_train_path = dir_path + 'operation_train_new.csv/'
transaction_train_path = dir_path + 'transaction_train_new.csv/'
tag_train_path = dir_path + 'tag_train_new.csv/'
operation_df = pd.read_csv(operation_train_path)
transaction_df = pd.read_csv(transaction_train_path)
print(operation_df.head())
