from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os
from  invitatin_cards import invites

# Specify font and text
font_size = 24
font_path = Path(Path.home().joinpath("Desktop", "IMAGE", "PILW", "Briem_Hand",
                                      "static", "BriemHand-ExtraBold.ttf"))  # Example font file path

print("Font path:", font_path)  # Debugging statement

try:
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, font_size)
        print("Font loaded successfully!")  # Debugging statement
    else:
        print("Font file does not exist!")  # Debugging statement
except OSError as err:
    print("An error occurred:", str(err))  # Debugging statement

# Create a new image with a white background
width = 650
height = 550
background_color = (255, 255, 255) # RGB
image = Image.new("RGB", (width, height), background_color)

# Get a drawing context
draw = ImageDraw.Draw(image)

# print(invites)
text = invites[1]

# text_width, text_height = draw.textsize(text, font)
# position = ((650 - text_width) // 2, (550 - text_height) // 2)

# Calculate text size
try:
    x = 30
    y = 35

    # Draw text on the image
    text_color = (0, 0, 0)  # Black color
    draw.text((x, y), text, fill=text_color, font=font)

    # Save the image
    image.save("output.png")

    # Display the image (optional)
    # image.show()
except Exception as e:
    print("Error:", str(e))
