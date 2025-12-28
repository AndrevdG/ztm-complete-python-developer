import pypdf

# rb = read binary
with open('./pdf/dummy.pdf', 'rb') as file:
    reader = pypdf.PdfReader(file)
    # print(reader.get_num_pages())
    # print(reader.get_page(0))
    page = reader.get_page(0)
    page.rotate(180)
    writer = pypdf.PdfWriter()
    writer.add_page(page)
    with open('./pdf/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
