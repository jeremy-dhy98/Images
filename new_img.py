from PIL import  Image, ImageDraw, ImageFont
from  practice import font
import emoji

width = 300
height = 300
bgc = (255,255,255)

img = Image.new("RGB", (width, height), color=bgc)
draw = ImageDraw.Draw(img)

# Add text to pic
text = ("Python is really fun.\nIndeeed it is ✔")
# Calculate text size using textbbox
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Calculate the center position
x = (width - text_width) / 2
y = (height - text_height) / 2
txt_loc = (x, y)
txt_color = (0, 0 , 0)
# Draw the text
draw.multiline_text(text=text, font=font, fill=txt_color, xy=txt_loc, align="center")

img.save("firstpic.png")
# img.show()
