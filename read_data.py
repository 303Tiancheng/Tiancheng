#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import csv
root_path = 'B:\\Tiancheng\\dataset'
operation_train_file = os.path.join(root_path, 'operation_train_new.csv')
operation_train = pd.read_csv(operation_train_file, iterator=False)
# chunk_size = 1000
# chunks = []
# while True:
#     try:
#         chunk = operation_train.get_chunk(chunk_size)
#         chunks.append(chunk)
#     except StopIteration:
#         print('data read complite')
#         break
# dp = pd.concat(chunks)
operation_train



