
import os
import py7zr  # type: ignore


def extract_7zip_file(zipped_file: str, target_path: str = '.') -> None:
    """Extracts a .7z file to the specified directory."""
    if not os.path.isfile(zipped_file):
        raise FileNotFoundError(f"The file '{zipped_file}' does not exist.")
    
    with py7zr.SevenZipFile(zipped_file, mode='r') as z:
        z.extractall(path=target_path)
    print(f"Extracted '{zipped_file}' to '{target_path}'")


def compress_folder_to_7zip(folder_to_zip: str, output_file: str) -> None:
    """Compresses a folder into a .7z archive."""
    if not os.path.isdir(folder_to_zip):
        raise NotADirectoryError(f"The folder '{folder_to_zip}' does not exist.")
    
    with py7zr.SevenZipFile(output_file, 'w') as z:
        z.writeall(folder_to_zip, arcname=os.path.basename(folder_to_zip))
    print(f"Compressed '{folder_to_zip}' into '{output_file}'")


def main():
    choice = input('Compress or extract folder (c/e): ').strip().lower()

    if choice == 'e':
        zipped_file = input("Enter the path of the .7z file to extract: ").strip()
        target_path = input(
            "Enter the target directory (default is current directory): "
            ).strip() or '.'
        extract_7zip_file(zipped_file, target_path)

    elif choice == 'c':
        folder_to_zip = input("Enter the path of the folder to compress: ").strip()
        output_file = input("Enter the output .7z file path: ").strip()
        compress_folder_to_7zip(folder_to_zip, output_file)

    else:
        print("Invalid choice. Please enter 'c' to compress or 'e' to extract.")


if __name__ == '__main__':
    main()
