from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path

from tts import speech_from_story, SpeechGenOpenAI


def separate_speech(speech):
    separated_audio_paths = []

    # Load the audio clip using Pydub
    audio = AudioSegment.from_file(speech.path)

    # Split the audio by silence (adjust parameters as needed)
    audio_segments = split_on_silence(audio, silence_thresh=-40, min_silence_len=500)

    # Set the target word count for each segment
    target_word_count = 3

    # Initialize variables
    current_word_count = 0
    current_segment = AudioSegment.silent()

    # Create a folder to save separated audio files
    parent_dir = Path(__file__).parent / "ignore.sep_audio_files"
    parent_dir.mkdir(parents=True, exist_ok=True)

    # Iterate through the audio segments and create new segments based on word count
    for i, segment in enumerate(audio_segments):
        current_word_count += len(segment.raw_data.split())
        current_segment += segment

        # Check if the current word count has reached the target
        if current_word_count >= target_word_count:
            final_path = parent_dir / f"segment_{i}.mp3"
            current_segment.export(final_path, format="mp3")
            separated_audio_paths.append(final_path)

            # Reset variables for the next segment
            current_word_count = 0
            current_segment = AudioSegment.silent()

    # If there's any remaining audio, save it as well
    if current_segment:
        final_path = parent_dir / "segment__.mp3"
        current_segment.export(final_path, format="mp3")
        separated_audio_paths.append(final_path)

    return separated_audio_paths


if __name__ == "__main__":
    # Replace this with an actual Speech object
    speech = speech_from_story("""Hey, art lovers! Ever wondered why the Mona Lisa is so valuable? 🤔 Turns out, it's not just about the artist's skill. Legend has it that the Mona Lisa's smile holds a hidden code, a message only a select few can decipher. 🔍💬

Enter Jacques, a brilliant art detective. In a daring move, he cracked the code and unveiled a secret compartment in the painting. Inside? A lost love letter from da Vinci himself! 😱💌 The discovery not only added a romantic twist to art history but also skyrocketed the painting's value.

Moral of the story: Sometimes, the true value lies in the hidden stories waiting to be uncovered. Keep your eyes open, you never know what secrets the world is hiding! """,
                               speech_generator=SpeechGenOpenAI())
    separate_speech(speech)
