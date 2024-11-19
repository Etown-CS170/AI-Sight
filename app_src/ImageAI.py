from dotenv import load_dotenv
from openai import OpenAI
import PIL
import pyautogui as gui
import io
import os
import base64  

# global variables
load_dotenv()
ImgWidth = 480
ImgHeight = 480
url = os.getenv('url')
API_KEY = os.getenv('API_KEY')
client = OpenAI(base_url= url, api_key= API_KEY)

# functions
def Capture(width = 360, height = 360):
    x , y = gui.position()
    image = gui.screenshot()

    image = image.crop(((x-width//2),(y-height//2),(x+width//2),(y+width//2)))
    return image

def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))

#base64_image = image_to_base64_str(Capture())


# AI inference with user input for test

def get_response(base64_image, streaming = False):
  completion = client.chat.completions.create(
    stream = streaming,
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
  return completion.choices[0].message.content


# message = get_response()
# print(message)