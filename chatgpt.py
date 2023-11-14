import openai

with open('chatgpt_api_key.txt', 'r') as key_file:
    openai.api_key = key_file.readline()


messages = [{"role": "system", "content": "You are a film critic."}]
messages.append({"role": "user", "content": "Tell me something about movie Avatar in 100 words."})

answers = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-4k",
        messages=messages
    )

print(answers['choices'][0]['message']['content'])