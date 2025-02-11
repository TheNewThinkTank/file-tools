
import os
import logging
from moviepy import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip

# Video export settings
VCODEC = "libx264"
VIDEO_QUALITY = "24"
COMPRESSION = "slow"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_cuts(cuts: list[tuple[str, str]]) -> None:
    """Validate the list of cuts."""
    if not cuts or any(len(cut) != 2 for cut in cuts):
        raise ValueError("Each cut must be a tuple with start and end times "
                         "in the format 'HH:MM:SS.mmm'.")
    logging.info("Cuts validated successfully.")

def check_file_exists(filepath: str) -> None:
    """Check if the input file exists."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    logging.info(f"Input file '{filepath}' found.")

def edit_video(input_file: str, output_file: str, cuts: list[tuple[str, str]], title_text: str | None = None) -> None:
    """Edit the video by applying cuts and optionally adding a text overlay."""
    validate_cuts(cuts)
    check_file_exists(input_file)

    try:
        logging.info("Processing video...")
        with VideoFileClip(input_file) as video:
            # Convert cuts from string format to seconds
            clips = [
                video.subclip(
                    _convert_time_to_seconds(start),
                    _convert_time_to_seconds(end)
                ) for start, end in cuts
            ]
            final_clip = concatenate_videoclips(clips)

            # Add a text overlay if title_text is provided
            if title_text:
                logging.info("Adding text overlay to the video...")
                text_clip = (
                    TextClip(
                        title_text,
                        fontsize=50,
                        color="green",
                        font="Arial-Bold"  # Ensure this font is installed
                    )
                    .set_duration(3)
                    .set_position(("center", "top"))
                )
                final_clip = CompositeVideoClip([final_clip, text_clip])

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

def _convert_time_to_seconds(time_str: str) -> float:
    """Convert time in 'HH:MM:SS.mmm' format to seconds."""
    hours, minutes, seconds = map(float, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds

def main():
    """Main function to execute the video editing process."""
    # Titles and cut times
    title = "demo"  # Replace with the actual movie title
    input_file = f"{title}.mp4"
    output_file = f"{title}_edited.mp4"
    cuts = [
        ('00:00:01.000', '00:01:36.000'),
        # ('00:00:24.000', '00:04:22.000'),
    ]
    title_text = "My Custom Title"  # Set to None if no text overlay is needed

    edit_video(input_file, output_file, cuts, title_text)

if __name__ == "__main__":
    main()
