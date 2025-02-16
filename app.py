import streamlit as st
import azure.cognitiveservices.speech as speechsdk
import time
import requests
import os
#from dotenv import load_dotenv

#load_dotenv()

API_TOKEN = "my8zolap7qx9w2geib04cf6tdrs1n3"
SPEECH_API_KEY = "AIzaSyCZJ9qqc7f2Vyzmht7Ja7Bp0m4LPs-_87c"
SCAMSEARCH_URL = "https://scamsearch.io/api/search?search"

def check_scam_number(phone_number):
    try:
        response = requests.get(
            SCAMSEARCH_URL,
            params={
                "search": phone_number,
                "type": "phone",
                "api_token": API_TOKEN
            },
            timeout=10
        )
        data = response.json()

        print(data)
        if data.get("status"):
            return "Scam call record found! Do NOT pick up."
        else:
            return "This number looks safe..."

    except requests.exceptions.RequestException as e:
        return f"Error occured while checking number: {e}"

# def recognize_audio(internal, audio_file_path="", audio_placeholder=""):
#     speech_config = speechsdk.SpeechConfig(subscription=SPEECH_API_KEY, region='eastus')
#     speech_config.speech_recognition_language="en-US"

#     if internal:
#         amazon_call_file = open(audio_file_path, "rb").read()
#         audio_placeholder.audio(amazon_call_file,autoplay=True)
#         time.sleep(8)

#         audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)
#         speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
#         print("Transcribing audio...")
#         speech_recognition_result = speech_recognizer.recognize_once_async().get()
#     else:
#         audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
#         speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
#         print("Listening for speech...")
#         speech_recognition_result = speech_recognizer.recognize_once_async().get()

#     if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         print("Recognized: {}".format(speech_recognition_result.text))
#         return speech_recognition_result.text
#     elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
#         return ""
#     else:
#         cancellation_details = speech_recognition_result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))

# def simulate_call():
#     status_placeholder.text("Calling...")
#     i = 1
#     ended = end_call_place.button("Hang Up")
#     while not ended and i <= 3:
#         recognized_text = recognize_audio(True,f"./audio/amazon_{i}.wav",audio_placeholder)
#         if recognized_text:
#             transcript_placeholder.write("Caller: " + recognized_text)
#         i += 1
#         time.sleep(1)
#         recognized_text = recognize_audio(False)
#         if recognized_text:
#             transcript_placeholder.write("You: " + recognized_text)

# st.title("Hangup Helpers")
# st.header("Proof of Concept")

# phone_number = st.text_input("Incoming Call From: ")
# if phone_number:
#     scam_result = check_scam_number(phone_number)
#     st.write(scam_result)

# # clicked = st.button("Simulate Call",on_click=simulate_call)

# status_placeholder = st.empty()
# audio_placeholder = st.empty()
# transcript_placeholder = st.container()
# end_call_place = st.empty()
