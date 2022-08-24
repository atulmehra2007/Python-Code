from PIL import Image
img=Image.open("C:\\Users\\atul_\\Downloads\\Untitled.jpg")
area=(100,150,455,588)
cropped_img=img.crop(area)
print(img.mode)
cropped_img.show()
