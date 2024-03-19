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
    # frames = frames[::2]

    frame_one = frames[0]
    base_width= 350
    wpercent = (base_width / float(frame_one.size[0]))
    hsize = int((float(frame_one.size[1]) * float(wpercent)))
    frames = [img.resize((base_width, hsize)) for img in frames]
    frames = frames[::2]
    
    # Save the GIF
    frame_one = frames[0]
    frame_one.save("/home/pcglab/Orbit/source/standalone/tutorials/04_sensors/output/camera1.gif", format="GIF", append_images=frames,
                    save_all=True, duration=125/3, loop=0)

if __name__ == "__main__":
    make_gif("/home/pcglab/Orbit/source/standalone/tutorials/04_sensors/output/camera1")
