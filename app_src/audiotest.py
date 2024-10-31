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

example_text = 'This is a test file.'
sample_rate = 48000
speaker='en_0'

audio_paths = model.save_wav(text=example_text,
                             speaker=speaker,
                             sample_rate=sample_rate)