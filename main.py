# my first steps into Python Text to speech
import pyttsx3
engine = pyttsx3.init()

file = open('file.txt', 'r')
engine.say(file.read())
engine.runAndWait()
print("The Final line has been read")