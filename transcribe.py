from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import download_mp3
import mp3_to_text
import os
import translate

'''
# Params: 
    video_code - part of yt link after "https://www.youtube.com/watch?v="

#Returns:
    whole_text - transription in english of a video
    mp3_filename.split("\\")[1] - 
'''
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
        whole_text_eng = formatter.format_transcript(dict_transcript).replace("\n", " ")

        #print(whole_text_eng) # >>> string in english
        video_title = download_mp3.yt_video_title(youtube_url + video_code)
        text_file = open(f'results/{video_title}_EN.txt', 'w', encoding="utf-8")
        text_file.write(whole_text_eng)
        print(f'Saved file: results/{video_title}_EN.txt')
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
        
        print(f'Transcribing audio file {mp3_filename}.wav')
        txt_filename = mp3_to_text.transcribe_large_audio(f'{mp3_filename}.wav')
        whole_text_eng = translate.translate_polish_transcription(f'results/' + txt_filename + '.txt')

    return whole_text_eng