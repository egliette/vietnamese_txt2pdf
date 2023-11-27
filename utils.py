import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics, ttfonts


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def txt2pdf(txt_fpath, pdf_fpath):
    c = canvas.Canvas(pdf_fpath, pagesize=letter)

    page_width, page_height = letter
    offset = 50
    x = offset
    y = page_height - offset
    font_size = 12

    font_path = 'AndikaNewBasic-R.ttf'
    font_name = "CustomFont"
    pdfmetrics.registerFont(ttfonts.TTFont(font_name, font_path))
    c.setFont(font_name, font_size)

    with open(txt_fpath, "r", encoding="utf-8") as f:
        for line in f:
            new_line = ""
            words = line.strip().split(" ")
            for word in words:
                if c.stringWidth(new_line+word+" ", font_name, font_size) <= page_width - 2*offset:
                    new_line += word + " "
                else:
                    if y - (font_size) < offset:
                        c.showPage()
                        c.setFont(font_name, font_size)
                        y = page_height - offset

                    c.drawString(x, y, new_line)
                    y -= (font_size + 8)
                    new_line = ""

            if new_line != "":
                if y - (font_size) < offset:
                    c.showPage()
                    c.setFont(font_name, font_size)
                    y = page_height - offset

                c.drawString(x, y, new_line)
                y -= (font_size + 8)

    c.showPage()
    c.save()
