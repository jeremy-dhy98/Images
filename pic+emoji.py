from PIL import Image, ImageDraw, ImageFont

# Image specifications
width = 300
height = 300
bgc = (255, 255, 255)  # Background color (white)

# Create an image
img = Image.new("RGB", (width, height), color=bgc)
draw = ImageDraw.Draw(img)

# Add text to the image
font_path = r"C:\Windows\Fonts\seguiemj.ttf" 

# Load a font (ensure the font supports emojis)
font = ImageFont.truetype(font_path, size=20)

text = ("Python is really fun.\nIndeed it is 😊")

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
draw.multiline_text(text=text, font=font, fill=txt_color, xy=txt_loc)

# Save the image
img.save("firstpic_emoji.png")
print("Image saved as 'firstpic.png'.")
