import requests
import json

import os

def speak_text(text):
    powershell_command = f"powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"
    os.system(powershell_command)

city = input("Enter the name of the city:\n")

url = f"http://api.weatherapi.com/v1/current.json?key=31757bbc97df4761bb0155258241505&q={city}"

r = requests.get(url)
# print(r.text)
a = json.loads(r.text)
# print(a, "hi")
w = a["current"]["temp_c"]

s = f"The current weather in {city} is {w} degrees"
speak_text(s)



