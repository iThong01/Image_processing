import sys
import os
hw1_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hw1_dir)
import function.enhancement as en
import function.show as sh
import cv2

img = sh.read_img('images/pic1.png')
img.shape

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

sh.plot_hist([img],['Original'])
sh.show_images([img],['ori'])

gamma_same = en.gamma_transform(img,0.3)

r,g,b = cv2.split(img)
gamma_r = en.gamma_transform(r,0.3)
gamma_g = en.gamma_transform(g,0.27)
gamma_b = en.gamma_transform(b,0.28)
rgb_gamma = cv2.merge((gamma_r,gamma_g,gamma_b))

gamm_equal = en.equalize_hist_manual(rgb_gamma)

sh.plot_hist([img,gamma_same,rgb_gamma,gamm_equal],["ori","Gamma Same","Gamma Manual","Gamma+Eqaul"])
sh.show_images([img,gamma_same,rgb_gamma,gamm_equal],['Ori','Gamma Same','after gamma manual',"Gamma+Eqaul"])