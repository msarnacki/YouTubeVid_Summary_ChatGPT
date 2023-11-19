import transcribe
import mp3_to_text

#TODO: read list of yt links and perform process for all of them
#TODO: strip text from unnecessary chars before ChatGPT analysis (cost optimization)


youtube_url = "https://www.youtube.com/watch?v="
destination = './videos'

vid_id_PL_CC   = "0Dd_2ni4SZc"
vid_id_PL_noCC = "9oxrtuhRgGY"
vid_id_EN_CC   = "lFlu60qs7_4"
vid_id_EN_autoCC = "Zlq4p0ToiJk"

vid_id = vid_id_PL_CC

whole_text = transcribe.transcribe(vid_id)
print(whole_text)
