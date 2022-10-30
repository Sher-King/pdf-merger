from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileReader

def extract_text(file_path):
  with open(file_path, 'rb') as f:
    pdf = PdfFileReader(f)
  # get the first page
  page = pdf.getPage(1)
  print(page)
  print('Page type: {}'.format(str(type(page))))
  text = page.extractText()
  print(text)

if __name__ == "__main__":
  parser = ArgumentParser()
  # Add more options if you like
  parser.add_argument("-p", "--path",
                      dest="path",
                      default=".",
                      help="path of source PDF files")
  args = parser.parse_args()
  extract_text(args.path) 