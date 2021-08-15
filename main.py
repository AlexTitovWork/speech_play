import gtts
from playsound import playsound
import pyttsx3

# make request to google to get synthesis
tts = gtts.gTTS("Hello world")
# save the audio file
tts.save("hello.mp3")
# play the audio file
playsound("hello.mp3")

# in spanish
tts = gtts.gTTS("Привет я не робот, я живое существо. А может ты робот, или мне нужно проверить это?", lang="ru")
tts.save("hola.mp3")
playsound("hola.mp3")


# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = "Python is a great programming language"
engine.say(text)
# play the speech
engine.runAndWait()