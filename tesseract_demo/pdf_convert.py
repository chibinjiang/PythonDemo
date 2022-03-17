from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Path of the pdf
PDF_file = "/Users/chibinjiang/Downloads/0106002.pdf"


def main():
    pages = convert_from_path(PDF_file, 500)
    image_counter = 1
    # Iterate through all the pages stored above
    for page in pages[:1]:
        # Declaring filename for each page of PDF as JPG
        # For each page, filename will be:
        # PDF page 1 -> page_1.jpg
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG')
        image_counter = image_counter + 1
    # Variable to get count of total number of pages
    filelimit = image_counter-1
    outfile = "pdf_demo_output.txt"

    # Open the file in append mode so that
    # All contents of all images are added to the same file
    with open(outfile, "a") as f:
        # Iterate from 1 to total number of pages
        for i in range(1, filelimit + 1):

            # Set filename to recognize text from
            # Again, these files will be:
            # page_1.jpg
            filename = "page_"+str(i)+".jpg"
            # Recognize the text as string in image using pytesserct
            text = str(((
                pytesseract.image_to_string(
                    Image.open(filename), lang='chi_sim'
                )
            )))
            print(text)
            # The recognized text is stored in variable text
            # Any string processing may be applied on text
            # Here, basic formatting has been done:
            # In many PDFs, at line ending, if a word can't
            # be written fully, a 'hyphen' is added.
            # The rest of the word is written in the next line
            # Eg: This is a sample text this word here GeeksF-
            # orGeeks is half on first line, remaining on next.
            # To remove this, we replace every '-\n' to ''.
            text = text.replace('-\n', '')
            f.write(text)


if __name__ == '__main__':
    main()
