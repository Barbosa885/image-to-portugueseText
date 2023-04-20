#opencv
import cv2
import pytesseract
import os

from pdf2image import convert_from_path
from deep_translator import GoogleTranslator

dir = "./Pdfs/"
img = "./Images/"

dirs = os.listdir(dir)

for file in dirs:
    print(dir+file)
    images = convert_from_path(dir+file)

    for image in images:
        image.save(img+"%s-pagina-%d.jpg" % (file, images.index(image)+1), "JPEG")


minha_imagem = cv2.imread("./Images/lista1-iia.pdf-pagina-1.jpg")

res = pytesseract.image_to_string(minha_imagem)

file = open("./Texts/%s.txt" % (file), "w")
file.write(res)
file.close()

translated = GoogleTranslator(source="auto", target="portuguese").translate_file("./Texts/%s.txt" % (file))

file = open("./Texts/%s-translated.txt" % (file), "w")
file.write(translated)
file.close()