
from tempfile import NamedTemporaryFile
from file_convertion_tools.concatenate_files import concatenate_files


def test_concatenate_files():
    # Create temporary files for testing
    with NamedTemporaryFile('w+', delete=False) as temp_file1, \
         NamedTemporaryFile('w+', delete=False) as temp_file2, \
         NamedTemporaryFile('w+', delete=False) as temp_output:

        # Write test data to the input files
        temp_file1.write("line1_file1\nline2_file1\nline3_file1\n")
        temp_file2.write("line1_file2\nline2_file2\n")
        
        # Flush to make sure data is written to disk
        temp_file1.flush()
        temp_file2.flush()
        
        # Call the function with the temporary files
        concatenate_files(temp_file1.name, temp_file2.name, temp_output.name)
        
        # Read the output file and check its contents
        temp_output.seek(0)
        result = temp_output.read()
        expected_result = "line1_file1line1_file2\nline2_file1line2_file2\nline3_file1\n"
        
        assert result == expected_result, f"Expected '{expected_result}', but got '{result}'"
