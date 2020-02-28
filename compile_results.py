## Author : Nicolas Farrugia, February 2020
from matplotlib import pyplot as plt 
import torch
import torch.nn as nn
from tqdm import tqdm
import os 
import sys
import numpy as np 

from nilearn.plotting import plot_stat_map

from nilearn.regions import signals_to_img_labels

import sys

import pandas as pd

""" 
state = {
                                    'net': net.state_dict(),
                                    'epoch': epoch,
                                    'train_loss' : train_loss,
                                    'val_loss' : val_loss,
                                    'test_loss' : test_loss,
                                    'nfeat' : nfeat,
                                    'ninputfilters' : ninputfilters,
                                    'model' : net
                                } """

path = sys.argv[1]
all_test_loss = []
all_files = []
for root, dirs, files in os.walk(path, topdown=False):
   for name in files:
       if name[-2:] == 'pt':
           currentdict = os.path.join(root, name)
           
           #print(currentdict)
           try:
               old_dict = torch.load(currentdict)#['test_loss']
               #print(test_loss)
               doct = currentdict.split("/")[-2]
               values = doct.split("_")

               my_dict = dict(test_loss=old_dict["test_loss"],filename=currentdict)
               my_dict["alpha"] = values[2]
               my_dict["beta"] = values[3]
               my_dict["gamma"] = values[4]
               my_dict["delta"] = values[5]

               all_files.append(my_dict)
               all_test_loss.append(test_loss)
           except:
               print('Error for {}'.format(currentdict))
df = pd.DataFrame(all_files)
print(df.sort_values("test_loss"))
df.sort_values("test_loss").to_csv("test.csv")
"""
all_test_loss = np.stack(all_test_loss)


indsort = np.argsort(all_test_loss)
files_sort = [all_files[curind] for curind in indsort]
print(files_sort)

indmin = np.argmin(all_test_loss)
print("Minimum loss {} found for {}".format(all_test_loss[indmin],all_files[indmin]))

"""