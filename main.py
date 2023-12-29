#!/usr/bin/env python3
import time
import config
from separate_speech import separate_speech
from story_gen import StoryGenerator
from tts import speech_from_story, SpeechGenOpenAI
import prompts


def main():
    prompt = prompts.prompt_generator()
    story_gen = StoryGenerator(model="gpt-3.5-turbo", prompt=prompt)

    story = story_gen.generate()
    with open(f"story_{int(time.time())}.txt", "w", encoding="utf-8") as f:
        f.write(story)

    speech = speech_from_story(story.split("."), speech_generator=SpeechGenOpenAI())

    separated_speech = separate_speech(speech)
    print("finished")


if __name__ == "__main__":
    main()
