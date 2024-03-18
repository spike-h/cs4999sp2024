# import matplotlib.pyplot as plt
# import numpy as np

# img_array = np.load("/home/pcglab/Orbit/source/standalone/tutorials/04_sensors/output/camera/distance_to_image_plane_tensor([800], device='cuda:0')_0.npy")
# plt.axis('off')
# plt.imshow(img_array,cmap='gray')
# plt.show()

import cv2

# Load images as grayscale
image1 = cv2.imread("/home/pcglab/Downloads/unnamed1.png", 0)
image2 = cv2.imread("/home/pcglab/Downloads/unnamed2.png", 0)

# Calculate the per-element absolute difference between 
# two arrays or between an array and a scalar
diff = 255 - cv2.absdiff(image1, image2)

cv2.imshow('diff', diff)