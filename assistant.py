import speech_recognition as sr

def recognize_from_file(filepath):
    r = sr.Recognizer()
    audio_file = sr.AudioFile(filepath)
    with audio_file as source:
        audio = r.record(source,duration=3)
    return r.recognize_google(audio,show_all=False) #key=

def recognize_from_mic():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=4)
    return r.recognize_google(audio,show_all=False)

def list_microphones():
    mic = sr.Microphone()
    return mic.list_microphone_names()
