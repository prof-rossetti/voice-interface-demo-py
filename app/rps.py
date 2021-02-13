

from speech_recognition import Recognizer, Microphone

class VoiceService:
    def __init__(self):
        self.client = Recognizer()

    def capture_audio(self):
        with Microphone() as mic:
            audio = self.client.listen(mic)
        return audio

    def get_transcript(self, audio, show_all=False):
        return self.client.recognize_google(audio, show_all=show_all)

if __name__ == '__main__':

    service = VoiceService()

    print("----------------")
    print("HELLO! I AM LISTENING...")
    print("WHEN YOU ARE READY, PLEASE SAY SOMETHING... ")
    audio = service.capture_audio()
    #print(type(audio)) #> <class 'speech_recognition.AudioData'>

    print("----------------")
    print("OK! I THINK YOU SAID... ")
    transcript = service.get_transcript(audio)
    print(transcript.upper())
