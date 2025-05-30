import ocrmypdf
def convert_scanned_pdf_to_text_pdf(input_pdf_path, output_pdf_path, language='tel'):
    """
    Converts a scanned image PDF to a text-searchable PDF using OCRmyPDF.

    Args:
        input_pdf_path (str): Path to the input scanned PDF file.
        output_pdf_path (str): Path to save the output text-searchable PDF file.
        language (str, optional): Language code for OCR (e.g., 'eng' for English, 'fra' for French). Defaults to 'eng'.
    """
    try:
        ocrmypdf.ocr(input_pdf_path, output_pdf_path, language=language, skip_text=True)
        print(f"Successfully converted '{input_pdf_path}' to '{output_pdf_path}'")
    except Exception as e:
        print(f"Error converting '{input_pdf_path}': {e}")


if __name__ == '__main__':
    basepath="E:\\ConvertedPDFs\\Input\\"
    outputpath="E:\\ConvertedPDFs\\Output\\"
    input_pdf = '12-geeta paramArtha chandrika-chadalavADa.pdf'  # Replace with the path to your input PDF file
    output_pdf = "Text_"+input_pdf  # Replace with the desired path for the output PDF file
    language_code = 'tel'  # Change to your desired language code, if different from english

    convert_scanned_pdf_to_text_pdf(basepath+input_pdf, outputpath+output_pdf, language_code)