

from moviepy.editor import *
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
os.environ["IMAGEMAGICK_BINARY"] = "/opt/homebrew/bin/convert"

# Load the video file
video = VideoFileClip("video.mp4")

# Load the subtitle file as a text file
with open("subtitles.vtt") as f:
    subtitle_text = f.read()

# Create a TextClip with the subtitle text
subtitles = TextClip(subtitle_text, fontsize=24, color='white')


# Set the duration of the subtitles to match the duration of the video
subtitles = subtitles.set_duration(video.duration)

# Set the position of the subtitles on the video
subtitles = subtitles.set_position(('center', 'bottom'))

# Add the subtitles to the video
video_with_subtitles = CompositeVideoClip([video, subtitles])

# Save the merged video file
video_with_subtitles.write_videofile("merged_video.mp4")
