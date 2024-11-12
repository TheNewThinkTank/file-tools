"""
Extract tables from PDF files and convert them to CSV format.

Documentation: https://tabula-py.readthedocs.io/en/latest/tabula.html#tabula.io.build_options

Installation:
    pip install tabula-py
    pip install tabulate
"""

import glob
from tabula import convert_into, convert_into_by_batch, read_pdf
from tabulate import tabulate


def get_area(file: str) -> list[float]:
    """
    Calculate and return the area (top, left, bottom, right) from which to extract data
    within a PDF page by reading the file as JSON.

    :param file: Path to the PDF file to analyze.
    :type file: str
    :raises ValueError: _description_
    :return: List of coordinates [top, left, bottom, right] adjusted for extraction.
    :rtype: list[float]
    """

    try:
        tables = read_pdf(file, output_format="json", pages=1, silent=True)
        if not tables:
            raise ValueError("No tables found in the PDF.")
        
        top = tables[0]["top"]
        left = tables[0]["left"]
        bottom = tables[0]["height"] + top
        right = tables[0]["width"] + left
        print(f"{top=}\n{left=}\n{bottom=}\n{right=}")
        
        return [top - 20, left - 20, bottom + 10, right + 10]
    except Exception as e:
        print(f"Error calculating area for {file}: {e}")
        return [0, 0, 0, 0]


def inspect_first_table(file: str) -> None:
    """
    Inspect the first table from a PDF file to verify its structure.

    :param file: Path to the PDF file to inspect.
    :type file: str
    """

    try:
        df = read_pdf(
            file,
            multiple_tables=True,
            pages=1,
            area=get_area(file),
            silent=True
            )[0]
        print(tabulate(df.head(7), headers="keys"))
    except Exception as e:
        print(f"Error inspecting table in {file}: {e}")


def show_tables(file: str) -> None:
    """
    Print all tables from a PDF file.

    :param file: Path to the PDF file to read and display.
    :type file: str
    """

    try:
        tables = read_pdf(
            file,
            pages="all",
            multiple_tables=True,
            area=get_area(file),
            silent=True
            )
        for i, df in enumerate(tables, start=1):
            print(f"\nTable {i}:\n", tabulate(df, headers="keys"))
    except Exception as e:
        print(f"Error showing tables in {file}: {e}")


def convert_pdf_to_csv(file: str) -> None:
    """
    Convert all tables in a PDF to a single CSV file.

    :param file: Path to the PDF file to convert.
    :type file: str
    """

    try:
        output_csv = file.replace('.pdf', '.csv')
        convert_into(
            file,
            output_csv,
            output_format="csv",
            pages="all",
            area=get_area(file),
            silent=True
            )
        print(f"Converted {file} to {output_csv}")
    except Exception as e:
        print(f"Error converting {file} to CSV: {e}")


def convert_batch(directory: str) -> None:
    """
    Convert all PDF files in a directory to CSV format.

    :param directory: Path to the directory containing PDF files to convert.
    :type directory: str
    """

    try:
        convert_into_by_batch(directory, output_format="csv", pages="all", silent=True)
        print(f"Converted all PDF files in {directory} to CSV.")
    except Exception as e:
        print(f"Error converting batch in directory {directory}: {e}")


def main() -> None:
    """
    Main function to handle user interaction,
    for either displaying tables or converting PDFs to CSV.
    """
    files = glob.glob("*.pdf")
    if not files:
        print("No PDF files found in the current directory.")
        return

    file = files[0]
    print(f"Using file: {file}")

    choice = input("Show tables (s) or convert PDF to CSV (c): ").strip().lower()
    if choice == "s":
        show_tables(file)
    elif choice == "c":
        convert_pdf_to_csv(file)
    else:
        print("Invalid choice. Use 's' to show tables or 'c' to convert.")


if __name__ == "__main__":
    main()
