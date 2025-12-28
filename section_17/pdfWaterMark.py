from sys import argv
import pypdf


if len(argv) != 2:
    print("Provide one pdf for watermarking")
    exit(1)
stamp = pypdf.PdfReader("./pdf/wtr.pdf").pages[0]
writer = pypdf.PdfWriter(clone_from=argv[1])
for page in writer.pages:
    page.merge_page(stamp, over=False)
writer.write("./pdf/watermarked.pdf")
