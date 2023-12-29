import os
import time
from pathlib import Path
from dotenv import load_dotenv

import elevenlabs
import openai
from moviepy.editor import AudioFileClip

if __name__ == "__main__":
    pass

load_dotenv()

client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))


class Speech:
    path: Path
    sentence: str
    audio: AudioFileClip

    def __init__(self, sentence: str, path: Path):
        self.sentence = sentence
        self.audio = AudioFileClip(path.__str__())
        self.path = path

    def __str__(self):
        return self.sentence

    @property
    def duration(self):
        return self.audio.duration


class SpeechGenOpenAI:
    model = "tts-1"
    voice = "nova"

    def generate(self, text: str, path: Path):
        resp = client.audio.speech.create(input=text, model=self.model, voice=self.voice)
        resp.stream_to_file(path)


class SpeechGen11:
    voice = "Daniel"
    model = "eleven_multilingual_v2"

    def generate(self, text: str, path: Path):
        resp = elevenlabs.generate(
            text=text,
            voice=self.voice,
            model=self.model,
        )
        elevenlabs.save(resp, path)


def speech_from_story(sentence: str, speech_generator=SpeechGen11()) -> [Speech]:
    parent_dir = Path(__file__).parent / f"ignore.{str(int(time.time()))}"
    os.mkdir(parent_dir)

    speech_file_path = parent_dir / f"speech.mp3"
    speech_generator.generate(text=sentence, path=speech_file_path)
    return Speech(sentence, speech_file_path)


if __name__ == "__main__":
    speech_from_story("hello, how are you doing today my name is Daniel!")
