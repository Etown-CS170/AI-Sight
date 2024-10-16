from openai import OpenAI
import PIL
import pyautogui as gui
import io
import base64   

# global variables
ImgWidth = 360
ImgHeight = 360
url = "http://127.0.0.1:1234/v1"
API_KEY = "lm-studio"
client = OpenAI(base_url= url, api_key= API_KEY)
systemPrompt = "You are an AI assistant for the visually impared. Describe any images you are given in a concise manner."

# functions
def Capture(width, height):
    x , y = gui.position()
    image = gui.screenshot()

    image = image.crop((x-width//2),(y+height//2),(x+width//2),(y-width//2))
    return image

def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return str(base64.b64encode(byte_arr).decode('utf-8'))


# AI inference with user input for test
clientPrompt = input("User: ")
completion = client.chat.completions.create(
  model="model-identifier",
  messages=[
    {"role": "system", "content": systemPrompt},
    {"role": "user", "content": clientPrompt}
  ],
  temperature=0.7,
)
