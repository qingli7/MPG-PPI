import torch
import torch.nn as nn
import numpy as np



list1 = []
# addr  = '/home/peisen/ql_code/HIGH-PPI-main/result_save/gnn_multi_layer/valid_results_.05.txt'
addr  = '/home/peisen/ql_code/HIGH-PPI-main/result_save/gnn_training_seed_1/valid_results.txt'

try:
    file = open(addr, 'r')
except FileNotFoundError:
    print('File is not found')
else:
    lines = file.readlines()
    i = 1
    for line in lines:
        if (i%10==0): 
            a = line.split(',')
            # x = a[5]  # loss
            # x = x[23:]+ ','
            # x = a[7]  # precesion
            # x = x[12:]+ ','
            # x = a[6]  # recall
            # x = x[9:]+ ','
            x = a[8]  # F1
            x = x[5:]+ ','
            list1.append(x)
        i +=1
    # last_line = lines[-1]
    # a = line.split(',')
    # x = a[7]
    # x = x[12:]+ ','
    # list1.append(x)
file.close()
 
for x in list1:
    print(x)