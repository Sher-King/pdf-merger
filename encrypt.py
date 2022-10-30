from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt(file_path, outputpdf):
    password = "AufhskfdbBD674238^4@24"
    pdf_in = open(file_path, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    for page in range(pdf_reader.getNumPages()):
      pdf_writer.addPage(pdf_reader.getPage(page))
      pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
      use_128bit=True)
    with open(outputpdf, 'wb') as fh:
      pdf_writer.write(fh)

if __name__ == "__main__":
  parser = ArgumentParser()
  # Add more options if you like
  parser.add_argument("-o", "--output",
                      dest="output_filename",
                      default="Merged .pdf",
                      help="write merged PDF to FILE",
                      metavar="FILE")
  parser.add_argument("-p", "--path",
                      dest="path",
                      default=".",
                      help="path of source PDF files")
  args = parser.parse_args()
  encrypt(args.path, args.output_filename)