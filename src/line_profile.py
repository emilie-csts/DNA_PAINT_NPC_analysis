#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:20:23 2023

@author: christine
"""

import numpy as np




def generate_line_profile(image, center, angle, length, bins):

#    Generate a line profile on an image.
    
#    Args:
#        image (numpy.ndarray): The input image.
#        center (tuple): The coordinates (x, y) of the center of the line.
#        angle (float): The angle of the line.
#       length (int): The length of the line.
#        bins (int): The number of bins for the line profile.
        
#    Returns:
#        numpy.ndarray: The line profile array.
    
   
        
    
    # Extract the center coordinates
    x0, y0 = center # ne sont pas des entiers

    if (x0>length/2+1 and x0<image.shape[1]-length/2-1 and y0>length/2+1 and y0<image.shape[0]-length/2-1): #supprime pores au bord de l'image
    
# Calculate the x and y coordinates of the line # Pour un angle donné calcule les coordonées de la ligne 
        x = np.linspace(x0 - (length/2) * np.cos(angle),
                        x0 + (length/2) * np.cos(angle),
                        bins)
        y = np.linspace(y0 - (length/2) * np.sin(angle),
                        y0 + (length/2) * np.sin(angle),
                        bins)
        X=[]
        for i in range(0,bins):
            X.append([x[i],y[i]])


    # Calculate the x and y coordinates of the pixels along the line
    # Pour trouver les coordonées en pixel --> on repasse sur un système avec des entiers 
        xp = np.linspace(x0 - (length/2) * np.cos(angle),
                        x0 + (length/2) * np.cos(angle),
                        length).astype(int) 
        yp = np.linspace(y0 - (length/2) * np.sin(angle),
                        y0 + (length/2) * np.sin(angle),
                        length).astype(int)

    # Calculate the image intensity at the given pixels
    # Relève l'intensité du pixel à chaque pixel
    # En fonction de l'angle line profile n'a pas la même longueur
        fp = []
        for i in range(0,length):
            fp.append(image[yp[i],xp[i]])

    # Interpolate the pixel values along the line
    # Le fait d'interpoler permet d'avoir des line profile avec la même longueur car on choisit un bin égal pour tous 
        line_profile = np.interp(x, xp, fp)
    
    else:
        line_profile = np.empty(bins)
        line_profile[:] = np.nan
        
    
    return line_profile

#####################

def generate_rotational_line_profile(image, center, angle_bin, length, bins):

#    Generate a line profile on an image.
    
    line_profile_a=[]
    
    for angle in range(0,int(180-180/angle_bin),int(180/angle_bin)):
        
        # Interpolate the pixel values along the line
        line_profile_a.append(generate_line_profile(image, center, angle, length, bins))
    
    return line_profile_a

def average_rotational_line_profile(image, center, angle_bin, length, bins):

#    Generate a line profile on an image.
    
    line_profile_a=[]
    
    for angle in range(0,int(180-180/angle_bin),int(180/angle_bin)):
        
        # Interpolate the pixel values along the line
        line_profile_a.append(generate_line_profile(image, center, angle, length, bins))
    
    line_profile = np.mean(line_profile_a, axis=0)
    
    return line_profile