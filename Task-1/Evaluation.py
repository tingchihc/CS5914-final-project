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
    count = 0
    for k in range(0, 101):
        oriName = str(k) + "-O.jpg"
        perName = str(k) + "-P.jpg"

        if (oriName in list and perName in list):
            oriFile = dirname + oriName
            perFile = dirname + perName
            print(oriFile, perFile)
            origin = io.imread(oriFile)
            perturb = io.imread(perFile)
            mse += skimage.metrics.mean_squared_error(origin, perturb)
            SSIM += skimage.metrics.structural_similarity(origin, perturb, multichannel=True, data_range=255)
            psnr += skimage.metrics.peak_signal_noise_ratio(origin, perturb)
            count += 1
        k += 1

        print(mse)
    print(count)
    mse /= count
    SSIM /= count
    psnr /= count
    print(mse)
    print(SSIM)
    print(psnr)


dirname = "C:/Users/123/Desktop/resultsKK/"
calcMse(dirname)
