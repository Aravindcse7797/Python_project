import speech_recognition as sr     
r = sr.Recognizer()                 
with sr.Microphone() as source:     
    print("Speak Anything :")
    audio = r.listen(source)        
    try:   
        print("You said : "+r.recognize_googke(audio));
    except:
        pass;    
