import os
from moviepy.editor import *
from PIL import Image

source_path = os.path.join("video.mp4")

os.makedirs("thumbnail",exist_ok=True)
save_path = os.path.join("thumbnail")
def make_thumbnail():
    try:
        clip = VideoFileClip(source_path)
        duration = clip.duration
        thumbnail_duration = int(duration)//3
        frame = clip.get_frame(thumbnail_duration)
        thumbnail_path = os.path.join(save_path,"thumb.jpg")
        thumbnail = Image.fromarray(frame)
        print("Processing Thumbnail")
        thumbnail.save(thumbnail_path)
        return thumbnail_path
    except :
        print("No video found")
    
    
