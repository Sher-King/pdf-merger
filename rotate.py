import PyPDF2
from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate(file_path):
  pdf_in = open(file_path, 'rb')
  pdf_reader = PdfFileReader(pdf_in)
  pdf_writer = PdfFileWriter()
  for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(180)
    pdf_writer.addPage(page)
  pdf_out = open('rotated.pdf', 'wb')
  pdf_writer.write(pdf_out)
  pdf_out.close()
  pdf_in.close()


if __name__ == "__main__":
  parser = ArgumentParser()
  # Add more options if you like
  parser.add_argument("-p", "--path",
                      dest="path",
                      default=".",
                      help="path of source PDF files")
  args = parser.parse_args()
  rotate(args.path)