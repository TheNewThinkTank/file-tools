
import pytest
from unittest.mock import patch, MagicMock
from file_convertion_tools.audio import extract_audio


@pytest.fixture
def create_test_video(tmp_path):
    """Fixture to create a small test video file for testing."""
    test_video_path = tmp_path / "test.mp4"
    # Use 'open' to create an empty placeholder file (not a real video, but enough for mock testing)
    test_video_path.touch()
    return test_video_path


@pytest.fixture
def create_test_output(tmp_path):
    """Fixture for the expected output audio file path."""
    return tmp_path / "test.mp3"


def test_extract_audio_success(create_test_video, create_test_output):
    """Test if audio extraction runs successfully and calls write_audiofile."""
    with patch("file_convertion_tools.audio.AudioFileClip") as MockAudioFileClip:
        mock_audio = MagicMock()
        MockAudioFileClip.return_value = mock_audio

        extract_audio(str(create_test_video), str(create_test_output))

        # Check if write_audiofile was called with the correct arguments
        mock_audio.write_audiofile.assert_called_once_with(str(create_test_output), 44100)
        mock_audio.close.assert_called_once()


def test_extract_audio_file_not_found(create_test_output):
    """Test if the function handles a non-existent input file correctly."""
    non_existent_file = "non_existent.mp4"

    with patch("builtins.print") as mock_print:
        extract_audio(non_existent_file, str(create_test_output))
        mock_print.assert_called_once_with(f"Error: The input file '{non_existent_file}' does not exist.")


def test_extract_audio_handles_exceptions(create_test_video, create_test_output):
    """Test if the function handles exceptions during audio extraction gracefully."""
    with patch("file_convertion_tools.audio.AudioFileClip", side_effect=Exception("Mocked error")) as MockAudioFileClip, \
         patch("builtins.print") as mock_print:

        extract_audio(str(create_test_video), str(create_test_output))
        mock_print.assert_called_with("An error occurred: Mocked error")
