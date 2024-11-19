import ImageAI
import AudioAI
from playsound import playsound
import keyboard


#testing only
print('here')

cmd = ''

while True:

    cmd = keyboard.read_key()

    if cmd == 'x':
        #testing only
        print('exit')
        break

    #testing only
    print('running')

    if cmd == 'u':
        screen = ImageAI.Capture()
        screen = ImageAI.image_to_base64_str(screen)
        #testing only
        print('screenshot')

        responseText = ImageAI.get_response(screen)

        #testing only
        print(responseText)

        responseAudio = AudioAI.text_to_audio(responseText)
        playsound("C:/Users/jhutc/OneDrive/Documents/CS Projects/AI-Sight/app_src/audioOutputs/audio.wav")