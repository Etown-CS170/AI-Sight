import ImageAI
import AudioAI
import playsound
import keyboard


#testing only
print('here')

cmd = ''

while True:

    cmd = keyboard.read_key()

    if cmd == 'x':
        break

    #testing only
    print('running')

    if cmd == 'c':
        screen = ImageAI.Capture()
        screen = ImageAI.image_to_base64_str(screen)

        responseText = ImageAI.get_response(screen)

        #testing only
        print(responseText)

        responseAudio = AudioAI.text_to_audio(responseText)
        playsound(responseAudio)