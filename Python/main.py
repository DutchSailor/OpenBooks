import glob, sys, fitz

# To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

filename = 'C:/Users/mikev/Documents/GitHub/OpenBooks/Bernoullis Vademecum/20230526164358626.pdf'

path = 'C:/Users/mikev/Documents/GitHub/OpenBooks/Bernoullis Vademecum/Bernoullis Vademecum'

doc = fitz.open(filename)  # open document
i = 252
for page in doc:  # iterate through the pages
    pix = page.get_pixmap(matrix=mat)  # render page to an image
    pix.save(path + '-' + str(i) + '.png')  # store image as a PNG
    i = i + 1