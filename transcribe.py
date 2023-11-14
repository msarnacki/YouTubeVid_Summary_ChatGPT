from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import download_mp3
import mp3_to_text
import os

def transcribe(video_code):
    formatter = TextFormatter()
    whole_text = ""
    
    youtube_url = "https://www.youtube.com/watch?v="
    destination = './videos'

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_code)
        transcript = transcript_list.find_transcript(['en', 'pl'])
        #print(transcript) # >>> pl ("Polish")[TRANSLATABLE]

        if transcript.language_code == "pl":
            transcript = transcript.translate('en')

        dict_transcript = transcript.fetch()
        whole_text = formatter.format_transcript(dict_transcript).replace("\n", " ")

        print(whole_text) # >>> string z tekstem po polsku
    except:
        print("No captions availible for this video. Downloading MP3...")
        #download file and return filename without extension >>> videos/filename
        mp3_filename = download_mp3.download(yt_url=youtube_url + video_code, destination=destination )
        print(f"MP3 \'{mp3_filename}.mp3\' downloaded. \nConverting MP3 to WAV...")
        #convert videos/filename.mp3 to videos/filename.wav
        mp3_to_text.mp3_to_wav(f"{mp3_filename}.mp3", f"{mp3_filename}.wav")
        print(f"WAV \'{mp3_filename}.wav\' created. \nMP3 \'{mp3_filename}.mp3\' deleted.")
        #delete mp3 file
        os.remove(f"{mp3_filename}.mp3") 

    return whole_text, mp3_filename.split("\\")[1]