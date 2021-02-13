
from speech_recognition import Recognizer, Microphone

if __name__ == '__main__':

    print("----------------")
    print("INITIALIZING THE CLIENT...")
    client = Recognizer()
    print(type(client))

    print("----------------")
    print("HELLO! I AM LISTENING. WHEN YOU ARE READY, PLEASE SAY SOMETHING... ")
    with Microphone() as mic:
        audio = client.listen(mic)

    print("AUDIO CAPTURED. ANALYZING...")
    #transcript = client.recognize_google(audio)
    response = client.recognize_google(audio, show_all=True) # passing show_all gets us the confidence and alternatives
    best_alternative = response["alternative"][0]
    transcript = best_alternative["transcript"]
    #confidence = best_alternative["confidence"]

    print("----------------")
    print("RESULTS:")
    print(f"\n    '{transcript.upper()}'")
    print("\n    ", response, "\n")
