import sys
import os
hw1_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(hw1_dir)
import function.enhancement as en
import function.show as sh
import function.edge as ed

img = sh.read_img('images/pic3.png',0)
print(img.shape)
print(img.min(),img.max(),img.mean(),img.std())

sh.show_images([img],["xx"])
sh.plot_hist([img],['ori1'])

edge_img = ed.find_edge(img)

gamma = en.gamma_transform(img,3)
gamma_edge = ed.find_edge(gamma)

equal = en.equalize_hist_manual(img)
equal_edge = ed.find_edge(equal)

gam_equal = en.equalize_hist_manual(gamma)
gam_equal_edge = ed.find_edge(gam_equal)

sh.show_images([img,edge_img,gamma_edge,equal_edge,gam_equal_edge],['Ori','edge','gamma','equal','gamma+equal'])
sh.plot_hist([img,edge_img,gamma_edge,equal_edge,gam_equal_edge],['Ori','edge','gamma','equal','gamma+equal'])
sh.plot_hist([img,edge_img,gamma,equal,gam_equal],['Ori','edge','gamma','equal','gamma+equal'])