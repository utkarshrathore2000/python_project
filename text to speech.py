from gtts import gTTS
import os
f=input('enter your text')
#x=f.read()
language='en'
audio=gTTS(text=f,lang=language,slow=False)
audio.save('1.wav')
os.system('1.wav')
