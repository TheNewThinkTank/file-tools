
from moviepy.editor import AudioFileClip
import sys
import os


def extract_audio(
        input_file: str = "test.mp4",
        output_file: str = "test.mp3",
        fps: int = 44100
        ) -> None:
    """
    Extracts audio from a video file and saves it as an audio file.

    :param input_file: Path to the input video file, defaults to "test.mp4"
    :type input_file: str, optional
    :param output_file: Path for the output audio file, defaults to "test.mp3"
    :type output_file: str, optional
    :param fps: Frames per second for the audio output, defaults to 44100
    :type fps: int, optional
    """

    if not os.path.isfile(input_file):
        print(f"Error: The input file '{input_file}' does not exist.")
        return

    audio = None
    try:
        audio = AudioFileClip(input_file)
        audio.write_audiofile(output_file, fps)
        print(f"Audio extracted successfully to '{output_file}'")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if audio is not None:
            audio.close()


if __name__ == '__main__':
    # Optional: Accept file paths from command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else "test.mp4"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "test.mp3"
    extract_audio(input_file, output_file)
