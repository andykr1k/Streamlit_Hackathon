import assemblyai as aai
import os
from dotenv import load_dotenv


def TranscribeSpeechToText(file):
    load_dotenv()

    AAI_API_KEY = os.getenv("AAI_API_KEY")

    aai.settings.api_key = AAI_API_KEY

    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(file)

    return transcript.text