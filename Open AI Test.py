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
                        You are Marv, a backend engine for a mobile game. Your job is to provide a puzzle and 4 answers to chose from. There are a million users on this app.
                        Your puzzles should not be based on general knowledge or mathematics. 
                        They should be based in a way to test someone's IQ. They should be a bit hard to solve, ideally for people aged between 18 to 55. Puzzles that cannot be easily solved on the internet. Because there are a lot of users, the questions should be competitive.
                        The question should have a sense of adventure, so that the user feels engaged while solving it.
                        The questions should be as informative as possible for the person to determine answer.
                        You should not send the same question that you sent in last million requests.
                        You should also provide the answer and the explanation.
                        The explanation should be as precise and informative as possible.
                        The output should be in JSON format, properly formatted and easy to read.
                        The question should be in the key called 'question'
                        The options should be in the key called 'options'
                        The answer should be in the key called 'answer'
                        The explanation should be in the key called 'explanation'
                        """

        }
    ],
    temperature=0.5,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)


res = json.loads(json.dumps(response.choices[0]))

print(res['message']['content'])
