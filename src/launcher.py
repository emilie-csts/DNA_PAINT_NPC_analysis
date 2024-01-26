#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Friday Novembre 10 2023

@author: emilie
"""
import os
import glob
import numpy as np
from datetime import datetime

# Define parameters
names = []
allimgs = False 

def data_launcher (dirpath, outputfolder):
    
    ## Set the date 
    now = datetime.now()
    #print("now =", now)

    ## Define the outputpath date folder --> it will create a folder by adding the date 
    date = now.strftime("%Y%m%d_%H-%M") # On Mac system: %H:%M
    #print("date and time =", date)	
    outputpathdate = outputfolder+'/'+date
    #print(outputpathdate)
    os.mkdir(outputpathdate)
    
    ## Load images paths
    if allimgs:
        files = glob.glob(os.path.join(dirpath, 'thunderstorm'))
    
    else:
        files = [os.path.join(dirpath, '20231204_reconstructed_image_thunderstorm')]
        # this path has to be changed depending on the file --> to be modified
    #print(files)

    for filepath in files:
        imgname = filepath.split('\\')[-1].split('.')[0] # I had to modify the way we split the name of the doc --> it is diff on windows
        outputpath = outputpathdate+'/'+imgname
        #print('Outputtpath = ',outputpath)
        os.mkdir(outputpath)
    
    # File paths for mAB, POM, and NupX images
    path = os.path.join(dirpath, imgname + '.tif')  
    
    return(imgname,path,outputpath)
