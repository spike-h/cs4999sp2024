import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

count = 0

# Define the paths
input_folder = 'C:/Users/spike/Documents/code/gifs/camera'
output_folder = 'C:/Users/spike/Documents/code/gifs/depth'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Iterate over the files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.npy'):
        count +=1
        print(count)
        # Load the depth data from the .npy file
        depth_data = np.load(os.path.join(input_folder, filename))
        plt.axis('off')
        # Plot the depth data
        plt.imshow(depth_data, cmap='gray')

        # Save the plot as a .png file in the output folder
        output_filename = os.path.splitext(filename)[0] + '.png'
        plt.savefig(os.path.join(output_folder, output_filename), bbox_inches='tight')

        # Clear the plot
        plt.clf()

        # # Save the depth image as a .png file in the output folder
        # output_filename = os.path.splitext(filename)[0] + '.png'
        # depth_image.save(os.path.join(output_folder, output_filename))
