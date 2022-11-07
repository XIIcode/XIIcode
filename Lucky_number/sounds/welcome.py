from gtts import gTTS
import os
mytext = "Hi, Welcome to Lucky Number created by Daniel Gitonga @innercircle.com"
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("example_1.mp3")
