from gtts import gTTS
import os
mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"
audio = gTTS(text=mytext, lang="fr", slow=False)
audio.save("example.wav")
os.system("start example.wav")