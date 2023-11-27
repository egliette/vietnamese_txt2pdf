import os

import argparse
from tqdm import tqdm

from utils import txt2pdf, create_folder


def main(txt_path, pdf_path, file_convert=True):
    if file_convert:
        if pdf_path is None:
            pdf_path = txt_path.split(".")[-1] + ".pdf"
        txt2pdf(txt_path, pdf_path)
    else:
        if pdf_path is None:
            pdf_path = txt_path.split(".")[-1] + "_pdf"
        create_folder(pdf_path)
        file_list = list()
        for f in tqdm(os.listdir(txt_path)):
            if os.path.isfile(os.path.join(txt_path, f)):
                file_path = txt_path + "/" + f
                target_path = pdf_path + "/" + f.split(".")[0] + ".pdf"
                txt2pdf(file_path, target_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='File Converter')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', help='Path to the input file to be converted')
    group.add_argument('--dir', help='Path to the input directory to convert all files')

    parser.add_argument('--target', help='Name for the output file or directory', default=None)

    args = parser.parse_args()

    if args.file:
        main(args.file, args.target, file_convert=True)
    
    if args.dir:
        main(args.dir, args.target, file_convert=False)
        