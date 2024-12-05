## AI-Sight

James H's project for CS170 - Applications of Generative AI

AI-Sight is a program designed to enable visually-impared users to interact with the increasingly image-based online environment. It is designed to run everything locally for the best transparency, privacy, and customizability. This leads to the software being limited by the performance of the hardware it is being run on.

The LLM portion, which is by far the most computationally expensive, is able to be offloaded to a server using an API key.
It is Open-AI compatible, so GPT4 can, in theory, be utilized, but other models are utilized for local hosting. I prefer a small local Llava model over the cost of a GPT key.
Audio generation, which is generally much faster, is currently always run locally. I may find a way to offload this to a server in the future as well, but this is not a priority due to the relative speed compared to the LLM portion.

## Setup

# General Setup

1 -- Clone this repository to a location that is easy to access in the future.
2 -- Run Setup.py. This file will install all the necessary python libraries.
3 -- Create a shortcut to the AISightGUI.py program.
4 -- This is now where things diverge. See the appropriate section below for further instructions.

# Running the LLM Locally

1 -- Install LM Studio
2 -- Search for a vision-capable model in LM Studio's model browser. This model should be marked for full GPU Offload for best performance. Llava Models are likely to be the easiest to use.
3 -- Navigate to the Live Server tab in LM Studio.
4 -- Load the model you just downloaded using the top bar. Change its settings to utilize full GPU offload.
5 -- Start the live server. The URL provided should be used when running AI-Sight. The default API Key is "lm-studio."

# Using a cloud LLM

Performance and usability when using AI-Sight with a cloud service has not been tested. You can probably still do it, as the API calls are Open-AI compatible, but I do now know for certain. As I have not done this setup myself, the steps below may not be exact, but it is how I expect the process to work if you choose to go through with it.

1 -- Set up an account with your preferred service and acquire an API key.
2 -- Use their provided server URL and API Key when running AI-Sight.