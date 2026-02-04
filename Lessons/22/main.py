import glob
import os
from fpdf import FPDF, XPos, YPos

# Ustawienie katalogu roboczego
os.chdir(os.path.dirname(os.path.abspath(__file__)))

A4W = 210
A4H = 297

pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font("DejaVu", size=12)
pdf.cell(text="Oferta biura podróży")

pdf.image("logo.png", x=A4W*0.25, y=A4W*0.25, w=A4W*0.5, h=A4W*0.5)

for image_path in glob.glob("atrakcje_grafiki/*"):
    atraction = image_path[:-4].replace("atrakcje_grafiki\\", "")
    text_path = f"atrakcje_opisy/{atraction}.txt"

    pdf.add_page()
    pdf.set_font("DejaVu", size=24)
    pdf.cell(
        200,
        20,
        text=f"Nazwa atrakcji: {atraction.replace("-", " ").capitalize()}",
        new_x=XPos.LEFT, new_y=YPos.NEXT, align="C")
    
    # Dodanie grafiki
    pdf.cell(200, 10, link=pdf.image(image_path, w=195, h=120), new_x=XPos.LEFT, new_y=YPos.NEXT, align="C")

    # Dodanie opisów
    pdf.set_font("DejaVu", size=12)
    with open(text_path, 'r', encoding="utf-8") as file:
        desc = file.read()
    pdf.multi_cell(200, 10, text = f"Opis: {desc}", new_x=XPos.LEFT, new_y=YPos.NEXT, align="L")

pdf.output("Oferta_biura_podrozy.pdf")