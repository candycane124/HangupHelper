import azure.cognitiveservices.speech as speechsdk

def recognize_from_microphone():
    # Directly use the subscription key and region
    speech_config = speechsdk.SpeechConfig(subscription='CmlST8J5ZyK8Myk2Bz3svg3j2v0sibOovLt6gmPJ22uFNKFErO8HJQQJ99BBACYeBjFXJ3w3AAAYACOGeE4i', region='eastus')
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    for i in range (5):
        print("Listening for speech...")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

recognize_from_microphone()
