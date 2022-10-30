from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def split(pdf_path):
  fname = os.path.splitext(os.path.basename(pdf_path))[0]
  pdf = PdfFileReader(pdf_path)
  for page in range(pdf.getNumPages()):
    pdfwrite = PdfFileWriter()
    pdfwrite.addPage(pdf.getPage(page))
    outputfilename = '{}_page_{}.pdf'.format(fname, page+1)
    with open(outputfilename, 'wb') as out:
        pdfwrite.write(out)
    print('Created: {}'.format(outputfilename))


if __name__ == "__main__":
  parser = ArgumentParser()
  # Add more options if you like
  parser.add_argument("-p", "--path",
                      dest="path",
                      default=".",
                      help="path of source PDF files")
  args = parser.parse_args()
  split(args.path) 
