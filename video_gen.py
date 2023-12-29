from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import TextClip


# Function to add text to a video
def video_generator(input_video_path, output_video_path, text, start_time=0, end_time=None, fontsize=140, color='white',
                    ):
    # Load the video clip
    video_clip = VideoFileClip(input_video_path)

    # If end_time is not specified, set it to the duration of the video
    if end_time is None:
        end_time = video_clip.duration

    # Create a TextClip with the specified text
    text_clip = TextClip(text, fontsize=fontsize, color=color, method='caption', stroke_color='black',
                         stroke_width='10px')

    # Set the duration of the text clip to match the specified time range
    text_clip = text_clip.set_duration(end_time - start_time)

    # Position the text clip on the video
    text_clip = text_clip.set_position(('center', 'center'))

    # Overlay the text clip on the video
    video_with_text = video_clip.subclip(start_time, end_time).overlay(text_clip, position=('center', 'center'))

    # Write the result to a new file
    video_with_text.write_videofile(output_video_path, codec='libx264', audio_codec='aac')


# Example usage
if __name__ == '__main__':
    input_video_path = 'res/input_video.mp4'
    output_video_path = 'outputs/output_video.mp4'
    text = 'Sample Text Overlay'
    video_generator(input_video_path, output_video_path, text, start_time=5, end_time=10, fontsize=40, color='red',
                    position='bottom')
