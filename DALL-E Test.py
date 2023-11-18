import openai

response = openai.Image.create(
  prompt="a girl with blonde hair and a red roses bouquet in hand",
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']

print(image_url)