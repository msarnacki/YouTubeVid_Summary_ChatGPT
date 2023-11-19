from pydub import AudioSegment
import speech_recognition as sr
import os
from pydub.silence import split_on_silence

def mp3_to_wav(src_path,dst_path):
        try:
                sound = AudioSegment.from_file(src_path, "mp3")
        except:
                sound = AudioSegment.from_file(src_path, format="mp4")
        sound.export(dst_path, format="wav")


def transcribe_large_audio(path):
    
    org_filename = path[path.index('\\')+1:-4] #>>> title with underscores instead of spaces
    org_filename = org_filename[:30]
    #print(org_filename)

    r = sr.Recognizer()

    sound = AudioSegment.from_wav(path)
    # Split audio where silence is 700ms or greater and get chunks
    chunks = split_on_silence(sound, min_silence_len=400, silence_thresh=sound.dBFS-14, keep_silence=500)
    print("Splitting audio... Creating " + str(len(chunks)) + " chunks")

    # Create folder to store audio chunks
    folder_name = f"audio-chunks/audio-chunks-{org_filename}"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    
    whole_text = ""
    # Process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # Export chunk and save in folder
        chunk_filename = os.path.join(folder_name, f"chunk-{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        # Recognize chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # Convert to text
            try:
                print(f"Saved file: {chunk_filename} | Length: {round(audio_chunk.duration_seconds,2)}s. Transcribing...")
                text = r.recognize_google(audio_listened, language="pl-PL")
            except sr.UnknownValueError as e:
                print(f"Saved file: {chunk_filename} | Length: {round(audio_chunk.duration_seconds,2)}s. Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                #print(chunk_filename, ":", text)
                whole_text += text
                #print("Whole text: " + whole_text)

    print(f"Saved file: {org_filename}.txt")        
    
    text_file = open(f'results/{org_filename}.txt', 'w')
    text_file.write(whole_text)
    return org_filename

