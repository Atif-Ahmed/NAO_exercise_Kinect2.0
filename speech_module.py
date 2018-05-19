import os
from gtts import gTTS
from pygame import mixer
import nao_interface

_is_simulate = None
tts = None


def init(is_simulate):
    global _is_simulate
    _is_simulate = is_simulate
    global tts
    tts = nao_interface.get_tts()


def speak(text, wait=True):
    if _is_simulate:
        mixer.quit()
        mixer.init(25000)
        file_path = "Sound/" + text[1] + ".mp3"
        my_file = os.path.isfile(file_path)

        if not my_file:
            speech = gTTS(text=text[0], lang='en')
            speech.save(file_path)
        mixer.music.load(file_path)
        mixer.music.play()
        if wait:
            while mixer.music.get_busy():
                pass

    else:
        tts.say(text[1])
