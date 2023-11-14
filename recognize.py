import speech_recognition as sr

# transcribe audio file                                            
AUDIO_FILE = "audio-chunks/chunk1.wav"

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

print("Transcription: " + r.recognize_google(audio, language="pl-PL"))
