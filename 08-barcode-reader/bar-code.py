
    #this code creates svg file  with a plot of the given data.<s

#from barcode import EAN13
#number = '123456789010'

#generate_barcode = EAN13(number)
##generate_barcode.save("bar-to-the-code")

#this code creates  an image from the generated barcode and adds it to the SVG file 

from barcode import EAN13
from barcode.writer  import ImageWriter
number = '147852369010'

generated_barcode = EAN13(number, writer=ImageWriter())
generated_barcode.save("bar-to-the-code")