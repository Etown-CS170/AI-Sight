import os
import torch
import torch_directml as dml

# Initialize DirectML device
device = dml.device(0)

# Load the TTS model
local_file = os.path.join('model_src', 'v3_en.pt')
model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")

# Move tensors within the model to the DirectML device manually
for attr_name in dir(model):
    attr = getattr(model, attr_name)
    if isinstance(attr, torch.Tensor):
        try:
            setattr(model, attr_name, attr.to(device))
            print(f"Moved tensor attribute '{attr_name}' to {device}")
        except Exception as e:
            print(f"Could not move attribute '{attr_name}' to {device}: {e}")


def text_to_audio(input_text, speaker=13):
    """
    Convert text to audio using the TTS model.

    Args:
        input_text (str): The text to synthesize.
        speaker (int): Speaker ID, defaults to 13. Must be between 0 and 117.
    
    Returns:
        str: Path to the generated audio file.
    """
    if not (0 <= speaker <= 117):
        speaker = 13  # Default speaker if out of range

    sample_rate = 48000
    speaker_name = f'en_{speaker}'
    custom_audio_path = os.path.join("app_src", "audioOutputs", "audio.wav")
    
    # Generate audio
    audio_paths = model.save_wav(
        text=input_text,
        speaker=speaker_name,
        sample_rate=sample_rate,
        audio_path=custom_audio_path
    )
    return custom_audio_path


# Example usage
if __name__ == "__main__":
    # Generate audio for a sample text
    text = "Hello, this is a test of the text-to-speech model."
    generated_audio_path = text_to_audio(text)
    print(f"Generated audio saved at: {generated_audio_path}")
