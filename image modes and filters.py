from PIL import Image
from PIL import ImageFilter #import imagefilter from pillow to apply filters on image 
img=Image.open("C:\\Users\\atul_\\Downloads\\1.jpg")
image_c=img.convert("L") #convert function is used to convert image mode "L" is used for black and white
#"RGB" is used for RGB mode
#"CMYK" is used for CMYK
image_blur=img.filter(ImageFilter.BLUR) #BLUR is used for to apply blur filter
image_detail=img.filter(ImageFilter.DETAIL)#DETAIL is used to apply details filter  
image_edge=img.filter(ImageFilter.FIND_EDGES)#FIND_EDGES is used to apply edge filter
image_edge.show()
image_detail.show()
image_blur.show()
image_c.show()

