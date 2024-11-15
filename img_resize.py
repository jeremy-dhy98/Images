from PIL import  Image
from pathlib import Path

input_file  = Path(r"C:\Users\mulwa\Desktop\IMAGE\PILW\IMG_20230816_124606.jpg")
with Image.open(input_file) as img:
    img.load() # Read the img into pyrthon
    img.show() # see the img

def img_desc():
    print(f"Image size: {img.size}")
    print(f"Image mode: {img.mode}")
    print(f"Image format: {img.format}")

img_desc()

def imag_resize():
    # cropped_img = img.crop((300, 150, 450, 500))
    # cropped_img.show()
    resized_img = img.resize((img.width//10, img.height//10))
    print(f"Size after resizing: {resized_img.size}")
    # resized_img.show()
    resized_img.save("fit.png")

imag_resize()