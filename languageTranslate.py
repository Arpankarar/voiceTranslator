import speech_recognition as s
from googletrans import Translator
from gtts import gTTS 
from playsound import playsound

listener = s.Recognizer()

def lang_trans():
    with s.Microphone() as input:
        print("listening.....")
        our_input = listener.listen(input)
        texts = listener.recognize_google(our_input)
        translator= Translator()
        t=translator.translate(texts,dest='hi')
        print(t.text)
        voice = gTTS(text = t.text,long='hi')
        voice.save("lang.mp3")
        playsound("lang.mp3")
        print(texts)
        