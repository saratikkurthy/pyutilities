import pymupdf
import fitz


def convert_to_black_and_white(input_pdf, output_pdf, dpi=150):
    # Open the input PDF
    pdf_document = fitz.open(input_pdf)
    # Create a new PDF for the output
    new_pdf = fitz.open()

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # Convert to grayscale pixmap
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), colorspace=fitz.csGRAY, alpha=False)

        # Create a new page in the new PDF
        new_page = new_pdf.new_page(width=pix.width, height=pix.height)

        # Insert the grayscale image into the new page
        new_page.insert_image(new_page.rect, pixmap=pix)

    # Save the new PDF
    new_pdf.save(output_pdf)
    new_pdf.close()
    pdf_document.close()

if __name__ == '__main__':
    input_path="E:\\FilterPDF\\Input\\"
    output_path="E:\\FilterPDF\\Output\\"
    input_pdf = "Setu_Mahattva_With_The_Andhra_CommentarybBy_Venkata_Subba_Shastri.pdf"
    output_pdf = "Filtered_"+input_pdf
    convert_to_black_and_white(input_path+input_pdf, output_path+output_pdf)