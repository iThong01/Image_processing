import numpy as np

def gamma_transform(img, gamma):
    img_float = img.astype(np.float32) / 255.0 
    corrected = 255.0 * (img_float ** gamma)
    return np.clip(corrected, 0, 255).astype(np.uint8)

def contrast_stretch(img):
    img_float = img.astype(np.float32)
    min_val = img_float.min()
    max_val = img_float.max()
    if max_val == min_val:
        return np.zeros_like(img, dtype=np.uint8)
    stretched =  255.0* (img_float - min_val) / (max_val - min_val)
    return np.clip(stretched,0,256).astype(np.uint8)

def equalize_hist_manual(img):
    hist = np.bincount(img.ravel(),minlength=256)
    cdf = hist.cumsum()
    nonzero_cdf = cdf[cdf > 0]

    if len(nonzero_cdf) == 0:
        return np.zeros_like(img), np.arange(256, dtype=np.uint8)

    cdf_min = nonzero_cdf[0]
    total = img.size

    if total == cdf_min:
        return img.copy(), np.arange(256, dtype=np.uint8)

    lut = np.round((cdf - cdf_min) * 255 / (total - cdf_min))
    lut = np.clip(lut, 0, 255).astype(np.uint8)
    return lut[img]