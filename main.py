

import speech_recognition as sr



# It will create our recognizer
rec = sr.Recognizer()


with sr.Microphone() as mic:
    
    #It Will adjust the noise around microphone
    rec.adjust_for_ambient_noise(mic)
    
    # It will catch the audio and convert to text the caught
    print('Speek...')
    audio = rec.listen(mic)
    text = rec.recognize_google(audio, language="ENG")

    print(text.title())



