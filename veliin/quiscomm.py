import numpy as np
from pyvsnr import vsnr2d

img = np.random.random((100, 100))  # Input image
filters = [{'name':'Dirac', 'noise_level':0.35}]  # List of filters
img_corr_py = vsnr2d(img, filters)  # Compute VSNR
