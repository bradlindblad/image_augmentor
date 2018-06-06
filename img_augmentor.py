"""
Args:
    Enter file path of image directory you would like to augment
    ex: python img_augmentor.py C:\\bobcat_imgs

"""

import Augmentor
import getopt
import sys

#p = Augmentor.Pipeline(sys.argv[1])
p = Augmentor.Pipeline('C:\\Users\\XPS\\Desktop\\yo')
p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=0.8)
p.flip_top_bottom(probability=0.3)
p.shear(probability=0.5, max_shear_left=10, max_shear_right=10)
p.skew(probability=0.5, magnitude=0.2)
p.random_contrast(probability=0.7 ,min_factor=1, max_factor=2)
p.random_distortion(0.4, grid_width=6, grid_height=6, magnitude=5)
p.rotate(probability=0.4, max_right_rotation=10, max_left_rotation=10)
p.sample(50)

