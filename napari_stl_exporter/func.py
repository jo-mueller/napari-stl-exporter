# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:35:04 2021

@author: johan
"""

import os
from skimage import measure
from stl import mesh
import numpy as np
import tifffile as tf

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def convert_binary2frame(image):
    """

    Generates a wireframe consisting of vertices, edges and faces from
    a binarized image with the marching cubes algorithm

    Parameters
    ----------
    binary : 3D array
        binarized image with values 0 or X (can be any)

    Returns
    -------
    obj: mesh object that can be save by the stl package.

    """
    
    # Convert to numpy
    image = np.asarray(image)
    image[image != 0] = 1
    
    # Add a layer of zeros around 3D array so that borders can be detected propperly
    _image = np.zeros(np.asarray(image.shape) + 2)
    _image[1:-1, 1:-1, 1:-1] = image
    
    # Account for multiple, separate objects
    image = connect_objects(_image)
    
    # marching cubes
    verts, faces, normals, values = measure.marching_cubes(image, 0)
    
    # Create the mesh
    obj = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    for i, f in enumerate(faces):
        for j in range(3):
            obj.vectors[i][j] = verts[f[j],:]
            
    return obj

def connect_objects(image):
    """
    Examines whether multiple objects are present and connects separate objects
    with a scaffold

    Parameters
    ----------
    labels : nd array (NxDxM)
        Numpy Array containing binarized objects with the voxel value
        corresponding to its index

    Returns
    -------
    output:  nd array
        Numpy array containing binarized objects with scaffold structures between objects

    """
    
    # Label connected voxels
    labels = measure.label(image)
    labels_list = np.unique(labels)
    
    # Check how many voxels are present
    if len(labels_list) == 2:
        return labels
    elif len(labels_list) < 2:
        raise Exception('Only single value found in image! Image must contain of binary (0,1) values!')
    elif len(labels_list) > 3:
        
        # Find centroid for every object
        props = measure.regionprops(labels)
        
    
    

if __name__ == "__main__":
    
    image = tf.imread(r'D:\Documents\Promotion\Projects\2021_napari_stl_exporter\napari-stl-exporter\data\Pyramid.tif')
    
    obj = convert_binary2frame(image)
    obj.save(r'C:\Users\johan\Desktop\test.stl')
    
    