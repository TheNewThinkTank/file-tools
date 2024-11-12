
import moviepy.editor as mpy

# Video export settings
VCODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"

# Titles and cut times
TITLE = "<MOVIE-TITLE>"
INPUT_FILE = f"{TITLE}.mp4"
OUTPUT_FILE = f"{TITLE}_edited.mp4"
CUTS = [
    ('00:00:24.000', '00:04:22.000')
    ]


def edit_video(input_file, output_file, cuts):
    # Validate cuts
    if not cuts or any(len(cut) != 2 for cut in cuts):
        raise ValueError("Each cut must be a tuple with start and end times.")

    # Process video
    with mpy.VideoFileClip(input_file) as video:
        clips = [video.subclip(start, end) for start, end in cuts]
        final_clip = mpy.concatenate_videoclips(clips)

        # Save the final video
        final_clip.write_videofile(
            output_file,
            threads=4,
            fps=24,
            codec=VCODEC,
            preset=COMPRESSION,
            ffmpeg_params=["-crf", VIDEO_QUALITY]
        )


if __name__ == '__main__':
    edit_video(INPUT_FILE, OUTPUT_FILE, CUTS)
