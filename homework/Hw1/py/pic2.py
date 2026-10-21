import sys
import os
hw1_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hw1_dir)
import function.enhancement as en
import function.show as sh

img = sh.read_img('images/pic2.png',0)
img.shape

sh.show_images([img],['original'])
sh.plot_hist([img],["Hist Original"])

img_stretched = en.contrast_stretch(img)
x = en.equalize_hist_manual(img)

sh.show_images([img,img_stretched,x],['ori',"streched","equalize"])
sh.plot_hist([img,img_stretched,x],['ori',"stretched","Hist equalize"])