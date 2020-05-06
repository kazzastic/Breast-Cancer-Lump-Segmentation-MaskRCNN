#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:17:45 2020

@author: kazzastic
"""

import numpy as np
from matplotlib import pyplot as plt


directory = '/home/kazzastic/Documents/Breast-Cancer-Lump-Segmentation-MaskRCNN/data/patches/calcification/no_tumor'
img_array = np.load(directory+'/Calc-Test_P_00038_LEFT_CC_19.npy')


plt.imshow(img_array, cmap='gray')
plt.show()