from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os
from  invitatin_cards import invites

# Specify font and text
font_size = 24
font_path = Path(Path.home().joinpath("Desktop", "IMAGE", "PILW", "Briem_Hand",
                                      "static", "BriemHand-ExtraBold.ttf"))  

print("Font path:", font_path)  

try:
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, font_size)
        print("Font loaded successfully!") 
    else:
        print("Font file does not exist!")  
except OSError as err:
    print("An error occurred:", str(err))  

# Create a new image with a white background
width = 650
height = 550
background_color = (255, 255, 255) # RGB
image = Image.new("RGB", (width, height), background_color)

# Get a drawing context
draw = ImageDraw.Draw(image)

# print(invites)
text = invites[1]

# Calculate text size using textbbox
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Calculate the center position
x = (width - text_width) / 2
y = (height - text_height) / 2
txt_loc = (x, y)
txt_color = (0, 0 , 0)

try:
    # Draw text on the image
    text_color = (0, 0, 0)  # Black color
    draw.text((x, y), text, fill=text_color, font=font, align="center")

    # Add a border
    border_color = (255, 0, 0)  # Red border
    border_width = 10
    draw.rectangle([(0, 0), (width, height)], outline=border_color, width=border_width)
    
    # Save the image
    image.save("output.png")

    # Display the image
    # image.show()
except Exception as e:
    print("Error:", str(e))
