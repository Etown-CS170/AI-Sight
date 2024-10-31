import secret_keys
from openai import OpenAI
import PIL
import pyautogui as gui
import io
import base64  

# global variables
ImgWidth = 480
ImgHeight = 480
url = secret_keys.url
API_KEY = secret_keys.API_KEY
client = OpenAI(base_url= url, api_key= API_KEY)

# functions
def Capture(width = 480, height = 480):
    x , y = gui.position()
    image = gui.screenshot()

    image = image.crop(((x-width//2),(y-height//2),(x+width//2),(y+width//2)))
    return image

def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))

base64_image = image_to_base64_str(Capture())


# AI inference with user input for test
completion = client.chat.completions.create(
  stream = True,
  model="model-identifier",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Describe the image in the form of alt-text for a screen reader. Be accurate and precise.",
        },
        {
          "type": "image_url",
          "image_url": {
            "url":  f"data:image/jpeg;base64,{base64_image}"
          },
        },
      ],
    }
  ],
)
message = ""
for chunk in completion:
  if (chunk.choices[0].delta.content != None):
    message_chunk = chunk.choices[0].delta.content
    print(message_chunk, end = "", flush = True)
    message += message_chunk