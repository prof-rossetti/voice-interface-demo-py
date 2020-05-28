
import speech_recognition as sr

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
    print("THIS IS ALEXA, COMPLETING YOUR REQUEST...")

if "lumos" in transcript.lower():
    print("TURNING LIGHTS ON...")
    # todo: interface with smarkt IoT home devices to actually turn the lights on
