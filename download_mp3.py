# importing packages 
from pytube import YouTube 
import os 

#youtube_url = "https://www.youtube.com/watch?v="
#destination = './videos'

def download(yt_url, destination):
    # url input from user 
    yt = YouTube(yt_url) 
    
    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 
    
    # download the file 
    out_file = video.download(output_path=destination) 
    
    # save the file 
    base, ext = os.path.splitext(out_file.replace(" ", "_")) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    
    new_file_name = base.split("/")[-1]
    print(new_file_name)
    return(new_file_name)