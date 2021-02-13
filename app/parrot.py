
#import platform
#import subprocess
#
#from speech_recognition import Recognizer, Microphone
#
#def say(message):
#    message = "You said... " + message
#    print(message)
#    if platform.system() == "Darwin":
#        # on mac we can also use the say command, for bidirectional voice communication:
#        subprocess.run(["say", f"'{message}'"])
