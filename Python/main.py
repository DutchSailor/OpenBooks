import glob, sys, fitz
from glob import glob

from os import path

def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

folder = 'C:/Users/mikev/Documents/GitHub/OpenBooks/Paneeldeuren/'
Prefix = "Paneeldeuren-"
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
        pix.save(path2 + str(i) + '.png')  # store image as a PNG
        i = i + 1