from argparse import ArgumentParser
from glob import glob
from PyPDF2 import PdfFileMerger
import os
from natsort import natsorted

def merge(path, output_filename):
    merger = PdfFileMerger(strict=False)
    pdffile = f = open(path, 'rb')
    print(pdffile)
    
    # list_of_pages =[(210, 211), (262, 263), (296, 296), (340, 340), (374, 374), (431, 431), (474, 475), (503, 503), (538, 538), (584, 586), (663, 665), (740, 742)]
    # list_of_pages =[(242, 242), (294, 295), (328), (372), (406), (463), (506, 507), (535), (570), (616, 618), (695, 697), (772, 774)] 
    list_of_pages =[(242, 242), (294, 295), (328, 328), (372, 372), (406, 406), (463, 463), (506, 506), (535, 535), (570, 570), (616, 616), (695, 695), (772, 772)] 
    # bookmark = os.path.basename(pdffile[:-4])
    # print(f" Bookmark: '{bookmark}'")
    for chapter_pages in list_of_pages:
        print(f"Appending: '{chapter_pages}'")
        merger.append(pdffile, pages= chapter_pages)
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