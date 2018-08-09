"""
Args:
    [1] Easygui - select directory
    [2] Easygui - enter sample size to compute

"""
from easygui import *
import Augmentor
import sys


# Use easygui to select folder of images
path = diropenbox("Pick a folder containing the images to augment", "Image_Augmentor")

p = Augmentor.Pipeline(path)  # pull in the file path of folder to be augmented

p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=0.8)
p.flip_top_bottom(probability=0.3)
p.shear(probability=0.5, max_shear_left=10, max_shear_right=10)
p.skew(probability=0.5, magnitude=0.2)
p.random_contrast(probability=0.4, min_factor=1, max_factor=2)
p.random_distortion(0.8, grid_width=5, grid_height=5, magnitude=4)
p.rotate(probability=0.4, max_right_rotation=10, max_left_rotation=10)

s_size = integerbox("Enter how many images you want to create", "Image_Augmentor")

size = int(s_size)  # change the argv to an integer
p.sample(size)



