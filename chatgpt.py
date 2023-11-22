import openai

def ask_chatgpt(question):
    with open('chatgpt_api_key.txt', 'r') as key_file:
        openai.api_key = key_file.readline()


    messages = [{"role": "system", "content": "You are a person who writes summaries of youtube videos"}]
    messages.append({"role": "user", "content": question})

    answers = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

    return answers['choices'][0]['message']['content']