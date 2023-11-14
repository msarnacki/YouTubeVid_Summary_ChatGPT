import transcribe
import mp3_to_text
import translate

youtube_url = "https://www.youtube.com/watch?v="
destination = './videos'

vid_id_PL_CC   = "0Dd_2ni4SZc"
vid_id_PL_noCC = "ZDAduvcDC48"
vid_id_EN_CC   = "lFlu60qs7_4"
vid_id_EN_autoCC = "Zlq4p0ToiJk"

vid_id = vid_id_PL_noCC

#whole_text, filename = transcribe.transcribe(vid_id)

#result = mp3_to_text.transcribe_large_audio(f'videos/{filename}.wav')


path_to_polish_transcription = './results/Zmiana_kursu_Bitcoin_nadchodzi.txt'

translate.translate_polish_transcription(path_to_polish_transcription)