#!/usr/bin/env python3

import speech_recognition as sr

from features.respond.tts import tts

# Suppress ALSA lib error messages
# ----------------------------------------------------
# from ctypes import *

# # Define our error handler type
# ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


# def py_error_handler(filename, line, function, err, fmt):
#     pass


# c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
# asound = cdll.LoadLibrary('libasound.so')
# # Set error handler
# asound.snd_lib_error_set_handler(c_error_handler)
# ----------------------------------------------------


tts('Welcome! systems are now ready to run. How can I help you?')

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())

speech_text = ''

# recognize speech using Sphinx
try:
    speech_text = r.recognize_sphinx(audio)
    print("Sphinx thinks you said " + speech_text)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    speech_text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + speech_text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

tts(speech_text)
tts('Bye My friend')

'''
# recognize speech using Wit.ai
WIT_AI_KEY = "NCC2OIS54Y2ROFYCJ2XZDZREMXTNTIR5"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    speech_text = r.recognize_wit(audio, key=WIT_AI_KEY)
    print("Wit.ai thinks you said " + speech_text)
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

client = Wit(access_token=WIT_AI_KEY)
resp = client.message(speech_text)
print('Yay, got Wit.ai response: ' + str(resp))
'''

'''
# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
Endpoint: https://api.cognitive.microsoft.com/sts/v1.0
Key 1: 0d6a77ea6cb648a5a123639dd5b4932b
Key 2: 92cf7a2c73424f31b6424e4148e37e4f
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
'''
