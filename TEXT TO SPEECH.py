import pyttsx3
inp = input("Enter a text to turn into speech : ")
tts = pyttsx3.init()
tts.say(inp)
tts.runAndWait()