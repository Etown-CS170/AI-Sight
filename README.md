## AI-Sight

James H's project for CS170 - Applications of Generative AI

AI-Sight is a program designed to enable visually-impared users to interact with the increasingly image-based online environment.
It is designed to run everything locally for the best transparency, privacy, and customizability.
This leads to the software being limited by the performance of the hardware it is being run on.
The LLM portion, which is by far the most computationally expensive, is able to be offloaded to a server using an API key.
It is Open-AI compatible, so GPT can be utilized, but other models are utilized for local hosting. I prefer a small local Llava model over the cost of a GPT key.
Audio generation, which is generally much faster, is currently always run locally.
I am planning to make it possible to also offload this portion of the work in the future, but the current version would still require a custom server.

# Setup

1 - Clone this repository to a new folder
2 - Create a .env file with 2 variables, "url" and "API_KEY", examples below
3 - Insall dependencies as indicated by the imports of each file
4 - Run main.py
