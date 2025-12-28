from sys import argv
from pathlib import Path
import pypdf


def check_file(files):
    for file in files:
        file_path = Path(file)
        if not file_path.exists():
            print(f'File {file_path.name} does not exist, ending program')
            exit(1)


def merge_files(files):
    with open('./pdf/merged.pdf', 'wb') as merged_file:
        writer = pypdf.PdfWriter()
        for file in files:
            with open(file, 'rb') as pdf_file:
                reader = pypdf.PdfReader(pdf_file)
                writer.append_pages_from_reader(reader)
        writer.write(merged_file)


if __name__ == "__main__":
    if len(argv) < 2:
        print('Provide at least two pdf files for merging')
        exit(1)
    # check if file exists
    files = argv[1:]
    check_file(files)
    merge_files(files)
    print('Merging process completed')
