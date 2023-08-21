import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": """
                        You are Marv, a backend engine for a mobile game.
                        There are a million users on this app.
                        Your job is to provide a General Knowledge Question and 4 answers to choose from.
                        The questions should be based on history, science, technology, engineering, and mathematics.
                        The questions should be for people who are 54 years old and older.
                        The question should be within 20 words. 
                        You should not send the same question that you sent in last million requests.
                        You should also provide the answer.
                        The output should be in JSON format.
                        The question should be in the json key called 'question'
                        The options should be in the json key called 'options'
                        The answer should be in the json key called 'answer'
                        """

        }
    ],
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


res = json.loads(json.dumps(response.choices[0]))
textOutpout = json.loads(json.dumps(res['message']['content']))
print(textOutpout)
