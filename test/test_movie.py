
import pytest
from unittest.mock import patch, MagicMock
import os
from file_convertion_tools.movie import edit_video


# def test_valid_cuts():
#     cuts = [('00:00:24.000', '00:04:22.000')]

#     with patch('moviepy.editor.VideoFileClip') as mock_video:
#         # Create mock video and clip
#         mock_video_instance = MagicMock()
#         mock_video.return_value = mock_video_instance

#         mock_clip = MagicMock()
#         mock_video_instance.subclip.return_value = mock_clip
#         mock_clip.set_duration.return_value = mock_clip
#         mock_clip.set_start.return_value = mock_clip
#         mock_clip.crossfadein.return_value = mock_clip
#         mock_clip.crossfadeout.return_value = mock_clip

#         # Call the edit_video function
#         edit_video('test_input.mp4', 'test_output.mp4', cuts)

#         # Check if the subclip was called with correct parameters
#         mock_video_instance.subclip.assert_called_with('00:00:24.000', '00:04:22.000')


# Test invalid cuts (raises ValueError)
def test_invalid_cuts():
    invalid_cuts = [('00:00:24.000',)]

    with pytest.raises(ValueError, match="Each cut must be a tuple with start and end times."):
        edit_video('test_input.mp4', 'test_output.mp4', invalid_cuts)


# Test video file generation (mock the video processing part)
# def test_video_output():
#     cuts = [('00:00:24.000', '00:04:22.000')]

#     with patch('moviepy.editor.VideoFileClip') as mock_video, \
#          patch('moviepy.editor.VideoClip.write_videofile') as mock_write:
#         # Create mock video and clip
#         mock_video_instance = MagicMock()
#         mock_video.return_value = mock_video_instance

#         mock_clip = MagicMock()
#         mock_video_instance.subclip.return_value = mock_clip
#         mock_clip.set_duration.return_value = mock_clip
#         mock_clip.set_start.return_value = mock_clip
#         mock_clip.crossfadein.return_value = mock_clip
#         mock_clip.crossfadeout.return_value = mock_clip

#         # Call the edit_video function
#         edit_video('test_input.mp4', 'test_output.mp4', cuts)

#         # Check if the write_videofile method was called (indicating file save)
#         mock_write.assert_called_with('test_output.mp4', threads=4, fps=24,
#                                       codec="libx264", preset="slow", ffmpeg_params=["-crf", "24"])


# Test file creation (mock the filesystem interaction)
# def test_output_file_creation():
#     cuts = [('00:00:24.000', '00:04:22.000')]

#     with patch('moviepy.editor.VideoFileClip') as mock_video, \
#          patch('moviepy.editor.VideoClip.write_videofile') as mock_write:
#         # Create mock video and clip
#         mock_video_instance = MagicMock()
#         mock_video.return_value = mock_video_instance

#         mock_clip = MagicMock()
#         mock_video_instance.subclip.return_value = mock_clip
#         mock_clip.set_duration.return_value = mock_clip
#         mock_clip.set_start.return_value = mock_clip
#         mock_clip.crossfadein.return_value = mock_clip
#         mock_clip.crossfadeout.return_value = mock_clip

#         # Simulate calling edit_video
#         edit_video('test_input.mp4', 'test_output.mp4', cuts)

#         # Check if the output file exists (mocked)
#         assert os.path.exists('test_output.mp4')
