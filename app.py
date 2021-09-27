from gtts import gTTS
from playsound import playsound

language = 'en'
audio = 'voice.mp3'

text = gTTS(text='hello developer...how u doing...its better to work smart'
                 'er..',lang=language,slow = False)
text.save(audio)
playsound(audio)
print('=====here it now======')