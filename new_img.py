from PIL import  Image, ImageDraw, ImageFont
from  practice import font

width = 300
height = 300
bgc = (255,255,255)

img = Image.new("RGB", (width, height), color=bgc)
draw = ImageDraw.Draw(img)

# Add text to pic
text = "Python is really fun.\nIndeeed it is😊"
x = 10
y = 15
txt_loc = (x, y)
txt_color = (0, 0 , 0)
draw.multiline_text(text=text, font=font, fill=txt_color, xy=txt_loc)

img.save("firstpic.png")
# img.show()
