from gtts import gTTS
import os

info='i am studying in charusat university.i am in first year.'
tts=gTTS(text=info)
tts.save('info.mp3')
print('mp3 save')
os.system('info.mp3')