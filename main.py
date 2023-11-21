import transcribe

#TODO: strip text from unnecessary chars before ChatGPT analysis (cost optimization)

youtube_url = "https://www.youtube.com/watch?v="
destination = './videos'

vid_id_PL_CC   = "0Dd_2ni4SZc"
vid_id_PL_noCC = "9oxrtuhRgGY"
vid_id_EN_CC   = "lFlu60qs7_4"
vid_id_EN_autoCC = "8H2ixCTphNM"

'''
vid_id = vid_id_EN_autoCC
whole_text = transcribe.transcribe(vid_id)
print(whole_text)

exit()
'''

file_video_ids = open('video_ids.txt', 'r')
video_ids = file_video_ids.readlines()
 
for vid_id in video_ids:
    whole_text = transcribe.transcribe(vid_id)
    print(whole_text)
