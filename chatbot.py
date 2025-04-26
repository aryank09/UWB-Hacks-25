from openai import OpenAI
import os
import json


'''
First, it ensures that the program is in the same directory as the python file itself.
It then reads the OpenAI API key from a file stored in the same directory.
It then reads the system message from another file stored in the same directory.
'''
########################################################################
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

f = open('keys.txt', 'r')
key = f.read().strip()
f = open('system.txt', 'r')
system_message = f.read().strip()

os.environ["OPENAI_API_KEY"] = key
########################################################################
















def query_gpt(content : str, key : str, system_message : str):

    client = OpenAI()
    completion = client.beta.chat.completions.parse(
        model='gpt-4o-mini',
        store=False,
        response_format=SentimentRating,
        messages=[
            {   
                "role": "developer",
                "content": [
                    {
                    "type": "text", # have it generate only the number
                    "text": system_message
                    }
                ]
                },
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": content
                    }
                ]
                }
        ]        
    )
    
    return completion.choices[0].message.content