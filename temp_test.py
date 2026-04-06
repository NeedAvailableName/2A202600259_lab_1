
import os
import time
from day_01_llm_api_foundation.template import call_openai

prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."
temps = [0.0, 0.5, 1.0, 1.5]

for temp in temps:
    print(f"--- Temperature: {temp} ---")
    response, latency = call_openai(prompt, temperature=temp)
    print(response)
    print(f"Latency: {latency:.2f}s\n")
