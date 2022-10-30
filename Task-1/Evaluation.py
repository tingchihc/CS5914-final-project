import os
import os.path

import skimage
from skimage import io
from skimage import metrics


def calcMse(dirname):
    imageCount = len([entry for entry in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, entry))]) / 2
    i = 1
    mse = 0
    SSIM = 0
    psnr = 0
    while i < imageCount + 1:
        origin = io.imread(dirname + str(i) + '-O.jpg')
        perturb = io.imread(dirname + str(i) + "-P.jpg")
        mse += skimage.metrics.mean_squared_error(origin, perturb)
        SSIM += skimage.metrics.structural_similarity(origin, perturb, multichannel=True, data_range=255)
        psnr += skimage.metrics.peak_signal_noise_ratio(origin, perturb)
        i += 1
    mse /= imageCount
    SSIM /= imageCount
    psnr /= imageCount
    print(mse)
    print(SSIM)
    print(psnr)


dirname = "C:/Users/123/Desktop/Results_ariana/"
calcMse(dirname)
