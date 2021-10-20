from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger
import os
from natsort import natsorted

def merge(path, output_filename):
    merger = PdfFileMerger(strict=False)
    f_list =natsorted(glob(path + os.sep + '*.pdf'))
    for pdffile in f_list:
        if pdffile == output_filename:
            continue
        print(f"Appending: '{pdffile}'")
        bookmark = os.path.basename(pdffile[:-4])
        # print(f" Bookmark: '{bookmark}'")
        merger.append(pdffile, bookmark)
    merger.write(output_filename)
    merger.close()

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
    merge(args.path, args.output_filename)