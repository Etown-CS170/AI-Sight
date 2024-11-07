# V4
import os
import torch

if torch.cuda.is_available():
    device = torch.device("cuda")  # Use GPU
else:
    device = torch.device("cpu")  # Use CPU
    torch.set_num_threads(4)
local_file = 'model_src//v3_en.pt'


model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

# example_text = "The image shows a large, inflatable rubber duck floating on a body of water. In the background, there is a city skyline with buildings and a bridge, suggesting that this could be a photo taken from a riverbank or a dock in an urban area. The sky is dusky with shades of blue, indicating either dawn or dusk. There's also a hint of colorful clouds, adding to the serene ambiance of the scene. The rubber duck seems to be placed there as part of an event or simply for fun."
# sample_rate = 48000
# speaker='en_13'

# audio_paths = model.save_wav(text=example_text,
#                              speaker=speaker,
#                              sample_rate=sample_rate)

def text_to_audio(inputText, speaker = 13):
    if speaker < 0 or speaker > 117:
        speaker = 13
    
    if torch.cuda.is_available():
        device = torch.device("cuda")  # Use GPU
    else:
        device = torch.device("cpu")  # Use CPU
        torch.set_num_threads(4)

    local_file = 'model_src//v3_en.pt'
    sample_rate = 48000
    speaker=f'en_{speaker}'

    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    custom_audio_path = r"app_src/audioOutputs/audio.wav"
    audio_paths = model.save_wav(
        text=inputText,
        speaker=speaker,
        sample_rate=sample_rate,
        audio_path=custom_audio_path
        )
    
    return custom_audio_path
