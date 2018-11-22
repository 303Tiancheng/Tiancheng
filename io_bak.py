{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "# 读取数据\n",
    "dir_path = './'\n",
    "operation_train_path = dir_path + 'operation_train_new.csv'\n",
    "transaction_train_path = dir_path + 'transaction_train_new.csv'\n",
    "tag_train_path = dir_path + 'tag_train_new.csv'\n",
    "operation_df = pd.read_csv(operation_train_path)\n",
    "transaction_df = pd.read_csv(transaction_train_path)\n",
    "tag_df = pd.read_csv(tag_train_path)\n",
    "# 根据UID分组\n",
    "operation_grouped = operation_df.groupby('UID')\n",
    "id2operation={}\n",
    "for name,group in operation_grouped:\n",
    "    id2operation[name] = group\n",
    "\n",
    "transaction_grouped = transaction_df.groupby('UID')\n",
    "id2transaction={}\n",
    "for name,group in transaction_grouped:\n",
    "    id2transaction[name] = group\n",
    "\n",
    "# 标签数据\n",
    "id2tag=dict(tag_df.values.tolist())\n",
    "id2operation[10000]\n",
    "group_o=id_2_operation[10000]\n",
    "group_t=id_2_transaction[10000]\n",
    "group_t.shape[0]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
