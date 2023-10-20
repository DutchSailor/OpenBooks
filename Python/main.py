import glob, sys, fitz
from glob import glob

from os import path

def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

folder = "C:/Users/mikev/Documents/GitHub/OpenBooks/Ir A.P. Potma en Ir J.E. de Vries Staalconstructies, theorie, berekening en uitvoering/"
#"C:/Users/mikev/3BM Dropbox/Maarten Vroegindeweij/Domera/10_PR_bureau_standaardisatie/50_brochure/Brochure 7 Bouwnummers/"
Prefix = "Ir A.P. Potma en Ir J.E. de Vries Staalconstructies, theorie, berekening en uitvoering"
path2 = folder + Prefix

pdffiles = find_ext(folder,'pdf')

print(pdffiles)
#sys.exit()
# To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

i = 0
for j in pdffiles:
    doc = fitz.open(j)  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(matrix=mat)  # render page to an image
        if i<10:
            istr = "00" + str(i)
        elif i<100:
            istr = "0" + str(i)
        else:
            istr = str(i)
        pix.save(path2 + istr + '.png')  # store image as a PNG
        i = i + 1