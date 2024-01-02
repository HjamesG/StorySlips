import os
import random
from gpiozero import Button
import openai


model_engine = "text-davinci-003"
openai.api_key = "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"

def GPT(query):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=query,
        max_tokens=1024,
        temperature=0.5,
        
    )
    return str.strip(response['choices'][0]['text'])

def orphans(text):
    output = ""
    words = text.split(" ")
    line = ""
    for word in words:
        if (len(word) + len(line)) >= 32:
            output = output + line + "\n"
            line = word + " "
        elif (len(word) + len(line)) < 32:
            line = line + word + " "
    output = output + line
            
    return output

# sets up random query for ChatGPT
genere = ["Horror", "Fantasy", "Sci-Fi", "realistic Fiction"]
stories = [genere[random.randint(0,3)] + " story about a brand new character with a new name", "two sentence horror story", "poem", "song"]

# Removes punctuation that makes the string difficult
response = GPT("clear our history and write me a " + stories[random.randint(0, 3)])
response = response.replace("\'", "")
response = response.replace("\"", "")

response = response.replace(":", "")
title = GPT("write a short title about this: \n\n" + response)
title = title.replace(":", "")

# Outputs to console
print(title)
print("\nBy: ChatGPTn\n")
print(orphans(response)) 

os.system("stty -F /dev/serial0 19200")
os.system("echo '"+ orphans(title) + "\n\nBy: ChatGPT \n\n" + orphans(response) + "\n\n\n\n' > /dev/serial0")

