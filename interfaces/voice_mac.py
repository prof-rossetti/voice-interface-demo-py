import subprocess

import speech_recognition as sr

print("----------------")
client = sr.Recognizer()
print("CLIENT", type(client))

with sr.Microphone() as mic:
    print("SAY SOMETHING!")
    audio = client.listen(mic)

print("----------------")
transcript = client.recognize_google(audio)
print("I THINK YOU SAID:", transcript.upper())

response = client.recognize_google(audio, show_all=True)
print(response)

print("----------------")
if "alexa" in transcript.lower():
    message = "THIS IS ALEXA, COMPLETING YOUR REQUEST..."
    print(message)
    subprocess.run(["say", f"'{message}'"])

if "lumos" in transcript.lower():
    message = "TURNING LIGHTS ON..."
    print(message)
    subprocess.run(["say", f"'{message}'"])
