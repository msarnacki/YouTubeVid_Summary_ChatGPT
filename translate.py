from googletrans import Translator

def translate_polish_transcription(path_to_transcription):
    translator = Translator()

    with open(path_to_transcription, 'r') as key_file:
        text_to_translate = key_file.readline()

    #print(len(text_to_translate))

    #split text around each X*len_to_translate
    len_to_translate = 2000
    len_text_to_translate = len(text_to_translate)
    if len_text_to_translate > len_to_translate:
        num_of_splits = len_text_to_translate//len_to_translate
        position_of_dot = []
        for x in range(0,num_of_splits):
            position_of_dot.append(text_to_translate[len_to_translate*(x+1):].find('. ') + len_to_translate*(x+1) + 1)
            
            #if last split is smaller than len_to_translate/3 then remove last split
            if (x+1) == num_of_splits and len_text_to_translate <= (len_to_translate*(x+1)+len_to_translate//3):
                position_of_dot.pop()

    #print(position_of_dot)

    splitted_text_to_translate = []
    splitted_text_translated = []

    for i, split in enumerate(position_of_dot):
        if i == 0:
            splitted_text_to_translate.append(text_to_translate[:split])
        else:
            splitted_text_to_translate.append(text_to_translate[position_of_dot[i-1]:split])
        
        translation = translator.translate(splitted_text_to_translate[-1], src="pl", dest="en")
        splitted_text_translated.append(translation.text)

    #print(splitted_text_to_translate)
    #print(splitted_text_translated)

    text_translated = ''.join(splitted_text_translated)

    text_file = open(f'{path_to_transcription[:-4]}_EN.txt', 'w', encoding="utf-8")
    text_file.write(text_translated)
