from PIL import Image
img=Image.open("C:\\Users\\atul_\\Downloads\\Untitled.jpg")
img2=Image.open("C:\\Users\\atul_\\Downloads\\1.jpg")
area=(10,12,50,65)
img2.paste(img,area)
img2.show()
