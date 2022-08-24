from PIL import Image
img=Image.open("C:\\Users\\atul_\\Downloads\\Untitled.jpg")
r1,g1,b1=img.split() #split function is used to split image in their native color Red,Green,Blue(RGB) or in CMYK 
r1.show()# it show Red colour image 
g1.show()# it show Green colour image 
b1.show()# it show Blue colour image 
print(img.mode) #mode show the mode of colour format in which image save i.e RGB or CMYK
new_image=Image.merge("RGB",(r1,g1,b1)) #Image.merge function is used merge splited image and "RGB" and "cmyk" used to specific mode of image created
new_image.show()
