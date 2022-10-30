import os
import os.path

import skimage
from skimage import io
from skimage import metrics


def calcMse(dirname):
    # imageCount = len([entry for entry in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, entry))]) / 2
    i = 1
    mse = 0
    SSIM = 0
    psnr = 0
    list = os.listdir(dirname)
    root = []
    for k in range(0, len(list)):
        root.append(dirname + list[k])
    for k in range(0, len(list)):
        origin = io.imread(root[k])
        perturb = io.imread(root[k + 1])
        print(root[k], root[k + 1])
        mse += skimage.metrics.mean_squared_error(origin, perturb)
        SSIM += skimage.metrics.structural_similarity(origin, perturb, multichannel=True, data_range=255)
        psnr += skimage.metrics.peak_signal_noise_ratio(origin, perturb)
        k += 2

        print(mse)
    mse /= len(list)
    SSIM /= len(list)
    psnr /= len(list)
    print(mse)
    print(SSIM)
    print(psnr)


dirname = "C:/Users/123/Desktop/Results_ariana/"
calcMse(dirname)
