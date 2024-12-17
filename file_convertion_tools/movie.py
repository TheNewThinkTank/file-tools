
import os
import logging
import moviepy.editor as mpy

# Video export settings
VCODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_cuts(cuts: list[tuple[str, str]]) -> None:
    """Validate the list of cuts."""
    if not cuts or any(len(cut) != 2 for cut in cuts):
        raise ValueError("Each cut must be a tuple with start and end times,"
                         "in the format 'HH:MM:SS.mmm'."
                         )
    logging.info("Cuts validated successfully.")


def check_file_exists(filepath: str):
    """Check if the input file exists."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    logging.info(f"Input file '{filepath}' found.")


def edit_video(input_file, output_file, cuts, title_text: str | None = None) -> None:

    validate_cuts(cuts)
    check_file_exists(input_file)

    try:
        logging.info("Processing video...")
        with mpy.VideoFileClip(input_file) as video:
            clips = [video.subclip(start, end) for start, end in cuts]
            final_clip = mpy.concatenate_videoclips(clips)

            # Add a text box if title_text is provided
            if title_text:
                logging.info("Adding text overlay to the video...")
                text_clip = mpy.TextClip(
                    title_text,
                    fontsize=50,
                    color="green",
                    font="Arial-Bold"  # Ensure the font is installed on your system
                ).set_duration(3).set_position(("center", "top"))
                final_clip = mpy.CompositeVideoClip([final_clip, text_clip])

            # Save the final video
            logging.info(f"Exporting video to '{output_file}'...")
            final_clip.write_videofile(
                output_file,
                threads=4,
                fps=24,
                codec=VCODEC,
                preset=COMPRESSION,
                ffmpeg_params=["-crf", VIDEO_QUALITY],
                audio=True
            )
        logging.info("Video editing completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during video processing: {e}")
        raise


def main():
    # Titles and cut times
    title = "demo"  # "<MOVIE-TITLE>"
    input_file = f"{title}.mp4"
    output_file = f"{title}_edited.mp4"
    cuts = [
        ('00:00:01.000', '00:01:36.000'),
        # ('00:00:24.000', '00:04:22.000'),
        ]
    title_text = "My Custom Title"  # Text to overlay on the video (set to None if not needed)

    # edit_video(input_file, output_file, cuts)
    edit_video(input_file, output_file, cuts, title_text)


if __name__ == '__main__':
    main()
