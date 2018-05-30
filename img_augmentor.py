"""
Args:
    Enter file path of image directory you would like to augment
    ex: python img_augmentor.py C:\\bobcat_imgs

"""

import Augmentor
import getopt
import sys

p = Augmentor.Pipeline(sys.argv[1])

p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=0.8)
p.flip_top_bottom(probability=0.3)

p.sample(50)

