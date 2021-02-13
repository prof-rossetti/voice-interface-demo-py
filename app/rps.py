
from random import choice

from speech_recognition import Recognizer, Microphone

OPTIONS = ["ROCK", "PAPER", "SCISSORS"]


class VoiceService:
    def __init__(self):
        self.client = Recognizer()

    def capture_audio(self):
        with Microphone() as mic:
            audio = self.client.listen(mic)
        return audio

    def get_transcript(self, audio, show_all=False):
        return self.client.recognize_google(audio, show_all=show_all)

    def capture_and_transcribe_audio(self):
        audio = self.capture_audio()
        #print(type(audio)) #> <class 'speech_recognition.AudioData'>
        transcript = self.get_transcript(audio, show_all=False)
        return transcript.upper()

if __name__ == '__main__':

    service = VoiceService()

    # USER SELECTION

    print("----------------")
    print("HELLO! I AM LISTENING...")
    print("WHEN YOU ARE READY, PLEASE SAY 'ROCK', 'PAPER', OR 'SCISSORS'... ")

    transcript = service.capture_and_transcribe_audio()
    print(transcript)

    user_choice = None
    choices = 0
    for option in OPTIONS:
        if option in transcript:
            user_choice = option
            choices+=1
    if user_choice == None or choices > 1:
        print("OOPS PLEASE TRY AGAIN")
        exit()

    print("----------------")
    print("YOU CHOSE:")
    print(user_choice)

    computer_choice = choice(OPTIONS)
    print("----------------")
    print("THE COMPUTER CHOSE:")
    print(computer_choice)

    print("----------------")
    print("THE WINNER IS...")
    print("[TODO]")
