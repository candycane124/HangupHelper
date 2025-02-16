import streamlit as st
import azure.cognitiveservices.speech as speechsdk
from google import genai
from app import check_scam_number

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


def analyze_speech(recognized_text):
    client = genai.Client(api_key="AIzaSyCZJ9qqc7f2Vyzmht7Ja7Bp0m4LPs-_87c")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=("determine if this is a scam caller or if its a genuine person. if you believe it is a scammer, for example, if the text includes a lot of mentions of credit card info return a response in the form: CAREFUL of potential scam callers...[fact about why its most likely a scam] note: only return a message if you believe the user is being scammed, if there is not enough information or you do not believe they are being scammed, return an empty string. Here is the text"+recognized_text)
    )
    print(response.text)
    return response.text

@st.dialog( "WAIT A MINUTE", width = "large")
def careful(warning_message):
    colo1, colo2 = st.columns(2, vertical_alignment = "center")
    with colo1: 
        st.image('./assets/owl_stop.png')
    with colo2:
        st.subheader("{}".format(warning_message))


st.logo("./assets/favicon.png")

col1, col2=st.columns([1,2], vertical_alignment = "center")
with col1:
    st.image("./assets/owl_logo_wbg.png", width=800)
with col2:
    st.title("Hangup Helper speaking!")
    phone_number = st.text_input("Is this number safe?")
    if phone_number:
        scam_result = check_scam_number(phone_number)
        st.write(scam_result)
    

img1, cool1, img2, cool2 = st.columns([1,2,1,2], vertical_alignment="center")
with img1: 
    st.image('./assets/pickup.png', width = 100)
with cool1:
    lol = st.button("Start Call Analysis")
with img2:
    st.image('./assets/hangup.png', width = 100)
with cool2: 
    endclicked = st.button("End Call")

if lol:
    calling = True
    st.write("Call transcript:")
    while calling:
        if endclicked:
            calling = False
            st.balloons()
        recognized_text = recognize_from_microphone()
        analysis=analyze_speech(recognized_text)
        st.write("{}".format(recognized_text))
        if (not analysis is "") and analysis.startswith("CAREFUL"):
            careful(analysis)

st.subheader("Whoo whoo am I calling?")
st.text("Many seniors are especially vulnerable to online scams. According to the FBI Internet Crime Complaint Center, roughly $3.4 billion in total fraud losses were reported by Americans over the age of 60 in 2023, while Nasdaq reported $77.7 billion of global fraud was linked to elderly victims in 2024.")
st.info("Be careful! Remember, someone may seem like your friend, but you never know their intentions.") 