import secret_keys
from openai import OpenAI
import PIL
import pyautogui as gui
import io
import base64 
import tkinter as tk  

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

root = tk.Tk()
root.withdraw()

popup = tk.Toplevel(root)
popup.title = "AI Response"

message_label = tk.Label(popup, text="Initial Message", width=40, height=10)
message_label.pack(padx=20, pady=20)

message_queue = []

def update_message(new_message):
  message_label.config(text=new_message)

def process_stream():
  global message_queue

  if message_queue:  # Check if there are messages to process
      message = message_queue.pop(0)
      update_message(message)

  # Schedule this function to be called again after 100ms
  popup.after(100, process_stream)

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
          "text": "Describe the image in the form of alt-text for a screen reader.",
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

def handle_stream():
  for chunk in completion:
    if chunk.choices[0].delta.content is not None:
      message = chunk.choices[0].delta.content
      print(message, end="", flush=True)
      message_queue.append(message)

  # Call process_stream to update the UI
  process_stream()

handle_stream()

popup.mainloop()