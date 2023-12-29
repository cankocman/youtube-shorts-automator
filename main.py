#!/usr/bin/env python3
import time
import config
from story_gen import StoryGenerator
from tts import speech_from_sentences
import prompts

def main():
    prompt = prompts.prompt_generator()
    story_gen = StoryGenerator(model="gpt-3.5-turbo", prompt=prompt)
    
    story = story_gen.generate()
    with open(f"story_{int(time.time())}.txt", "w", encoding="utf-8") as f:
        f.write(story)

    # speechs = speech_from_sentences(story.split("."), voice="nova")

    print("finished")


if __name__ == "__main__":
    main()
