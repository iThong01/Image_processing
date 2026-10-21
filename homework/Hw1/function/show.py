import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def read_img(fp,color=1):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(current_dir)
        p = os.path.join(base_dir, fp)
        img = cv2.imread(p, color)
        if img is None:
            raise FileNotFoundError(f"ไม่เจอ {p}")
        return img
    except FileNotFoundError as e:
        print(e)
        return None
    
def plot_hist(imgs,titles):
    plt.figure(figsize=(6*len(imgs),5))
    for idx,(img,title) in enumerate(zip(imgs,titles)):
        plt.subplot(1,len(imgs),idx+1)
        if img.ndim == 2:
            hist = np.bincount(img.ravel(),minlength=256)
            plt.plot(hist,color='black',label='BLACK')
        else:
            for idx, color in enumerate(['red','green','blue']):
                hist = cv2.calcHist([img],[idx],None, [256], [0,256])
                plt.plot(hist,color=color,label=color.upper())
        plt.title(title)
        plt.xlabel(f'Pixel')
        plt.ylabel('Instensity')
        plt.legend()
    plt.show()

def show_images(imgs,titles):
    plt.figure(figsize=(4*len(imgs),5))
    for idx, (img,title) in enumerate(zip(imgs,titles),start =1):
        plt.subplot(1,len(imgs),idx)
        if img.ndim == 2:
            plt.imshow(img,cmap ='gray')
        else:
            plt.imshow(img)
        plt.title(title)
        plt.axis('off')
    plt.show()