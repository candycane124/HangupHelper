import streamlit as st

st.title("Log of speech recognition entries")


import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone():
    # Directly use the subscription key and region
    speech_config = speechsdk.SpeechConfig(subscription='CmlST8J5ZyK8Myk2Bz3svg3j2v0sibOovLt6gmPJ22uFNKFErO8HJQQJ99BBACYeBjFXJ3w3AAAYACOGeE4i', region='eastus')
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        return "" #"No speech could be recognized: {}".format(speech_recognition_result.no_match_details)
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            return "" # "Error details: {}".format(cancellation_details.error_details)
        return "" #"Speech Recognition canceled: {}".format(cancellation_details.reason)



from google import genai

def analyze_speech(recognized_text):
    client = genai.Client(api_key="AIzaSyCZJ9qqc7f2Vyzmht7Ja7Bp0m4LPs-_87c")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=("determine if this is a scam caller or if its a genuine person. if you believe it is a scammer, for example, if the text includes a lot of mentions of credit card info return a response in the form: CAREFUL of potential scam callers. Real banking services will never ask for your credit card information. note: only return a message if you believe the user is being scammed, if there is not enough information or you do not believe they are being scammed, return an empty string. Here is the text"+recognized_text)
    )
    print(response.text)
    return response.text



st.title("Speech Recognition App")
if st.button("Start Recognition"):
    calling = True
    endclicked = st.button("end call")
    while calling:
        if endclicked:
            calling = False
        recognized_text = recognize_from_microphone()
        analysis=analyze_speech(recognized_text)
        st.write("{}".format(recognized_text))
        if (not analysis is "") and analysis.startswith("CAREFUL"):
            st.write("{}".format(analysis))

