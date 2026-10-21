import numpy as np

def find_edge(img, k=1):
    f = img.astype(np.float32)
    out = np.zeros_like(f, dtype=np.float32)

    mask_gx = np.array([[-1, 0, 1],
                        [-k, 0, k],
                        [-1, 0, 1]], dtype=np.float32)

    mask_gy = np.array([[-1, -k, -1],
                        [ 0,  0,  0],
                        [ 1,  k,  1]], dtype=np.float32)

    bd = mask_gx.shape[0] // 2
    padded = np.pad(f, pad_width=bd, mode="constant", constant_values=0)
    m, n = f.shape

    for i in range(m):
        for j in range(n):
            sub_f = padded[i : i + 2 * bd + 1, j : j + 2 * bd + 1]
            gx = np.multiply(sub_f, mask_gx).sum()
            gy = np.multiply(sub_f, mask_gy).sum()
            out[i, j] = np.sqrt(gx**2 + gy**2)

    out = np.clip(out, 0, 255)
    return out.astype(np.uint8)