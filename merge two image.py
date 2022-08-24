from PIL import Image
img=Image.open("C:\\Users\\atul_\\Downloads\\Untitled.jpg")
img1=Image.open("C:\\Users\\atul_\\Downloads\\1.jpg")
area=(0,0,1000,1000)
c_img=img.crop(area) #here crop function is used to make file of same size. 
c_img1=img1.crop(area)



r1,g1,b1=c_img.split() #split function is used to split image in their native color Red,Green,Blue(RGB) or in CMYK 
r2,g2,b2=c_img1.split()
print(img.size)
print(img1.size)

new_image=Image.merge("RGB",(r2+1,g1,b2)) #Image.merge function is used merge splited image and "RGB" and "cmyk" used to specific mode of image created
new_image.show()
new_image=Image.merge("RGB",(r1,g2,b1)) #Image.merge function is used merge splited image and "RGB" and "cmyk" used to specific mode of image created
new_image.show()
new_image=Image.merge("RGB",(r2,g1,b2)) #Image.merge function is used merge splited image and "RGB" and "cmyk" used to specific mode of image created
new_image.show()
