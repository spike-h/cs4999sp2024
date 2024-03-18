# import matplotlib.pyplot as plt
# import numpy as np

# img_array = np.load("/home/pcglab/Orbit/source/standalone/tutorials/04_sensors/output/camera/distance_to_image_plane_tensor([800], device='cuda:0')_0.npy")
# plt.axis('off')
# plt.imshow(img_array,cmap='gray')
# plt.show()

# import cv2

# # Load images as grayscale
# image1 = cv2.imread("/home/pcglab/Downloads/unnamed1.png", 0)
# image2 = cv2.imread("/home/pcglab/Downloads/unnamed2.png", 0)

# # Calculate the per-element absolute difference between 
# # two arrays or between an array and a scalar
# diff = 255 - cv2.absdiff(image1, image2)

# cv2.imshow('diff', diff)

import cv2
import os

def images_to_video(image_folder, video_name, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    if not images:
        print("No images found in the folder.")
        return

    # Sort images based on numerical order in filenames
    images.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        if os.path.exists(img_path):
            video.write(cv2.imread(img_path))
        else:
            print(f"Image file not found: {img_path}")

    cv2.destroyAllWindows()
    video.release()

# Example usage:
image_folder = '/home/pcglab/Orbit/source/standalone/tutorials/04_sensors/output/camera/'
video_name = 'output_video.mp4'
fps = 24  # Frames per second

images_to_video(image_folder, video_name, fps)


