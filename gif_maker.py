import glob
from PIL import Image
import glob
from PIL import Image
import re

def make_gif(frame_folder):
    # Load the image files
    file_paths = glob.glob(f"{frame_folder}/*.png")
    
    # Sort the image files by the number in their file name
    sorted_files = sorted(file_paths, key=lambda x: int(re.search(r'\[(\d+)\]', x).group(1)))
    
    # Convert the sorted image files to Image objects
    frames = [Image.open(image) for image in sorted_files]
    
    # Save the GIF
    frame_one = frames[0]
    frame_one.save("my_awesome.gif", format="GIF", append_images=frames,
                    save_all=True, duration=125/3, loop=0)

if __name__ == "__main__":
    make_gif("depth/")
