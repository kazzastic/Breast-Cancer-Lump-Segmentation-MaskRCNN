#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:16:21 2020

@author: kazzastic
"""

import glob
import shutil


def dataset_folder_roi(dataset_folder, new_dataset_folder):
    '''
    dataset_folder : string
    example : /media/kazzastic/external hdd/dataset/
    
    new_dataset_folder : string
    example : /media/kazzastic/external hdd/new dataset/
    '''
    arr = []
    dataset_folder = dataset_folder+'*png'
    
    for filename in glob.glob(dataset_folder):
        arr.append(filename)
        
    for i in range(len(arr)):
        if(arr[i].find('Calc-Test') != -1):
            print("[INFO]-Copying TEST case in new folder")
            shutil.copy(arr[i], new_dataset_folder)
        else:
            continue
        
def dataset_folder_mammogram(dataset_folder, new_dataset_folder):
    
    '''
    dataset_folder : string array
    example : ['/media/kazzastic/external hdd/dataset/', ...]
    
    new_dataset_folder : string
    example : /media/kazzastic/external hdd/new dataset/
    '''
    arr = []
    count = 1
    for j in range(len(dataset_folder)):
        dataset_folder[j]+='*png'
        
    for j in range(len(dataset_folder)):
        for filename in glob.glob(dataset_folder[j]):
            arr.append(filename)
        
    for i in range(len(arr)):
        shutil.copy(arr[i], new_dataset_folder)
        count+=1
        print("File Count {}".format(count))
        
one = '/media/kazzastic/C08EBCFB8EBCEAD4/data_png/patches/calcification/'
folders = [one+'benign/',one+'benign_no_callback/', one+'malignant/', one+'no_tumor/']
new_folder = '/media/kazzastic/C08EBCFB8EBCEAD4/Calc_training_full_mammogram_images/'
dataset_folder_mammogram(folders, new_folder)