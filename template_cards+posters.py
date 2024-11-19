# from PIL import Image, ImageDraw, ImageFont

# # Canvas dimensions (1080x1920 for portrait mode)
# canvas_width, canvas_height = 1080, 1920
# bg_color = (255, 250, 200)  # Vibrant background

# # Create the canvas
# canvas = Image.new("RGB", (canvas_width, canvas_height), color=bg_color)
# draw = ImageDraw.Draw(canvas)

# # Font setup
# try:
#     font = ImageFont.truetype("arial.ttf", size=80)  # Update with your preferred font path
# except IOError:
#     font = ImageFont.load_default()

# # Text for the title
# title_text = "You're Invited!"
# title_color = (255, 0, 50)

# # Calculate title position (centered horizontally at the top)
# title_width, title_height = draw.textsize(title_text, font=font)
# title_x = (canvas_width - title_width) // 2
# title_y = 100  # Top margin
# draw.text((title_x, title_y), title_text, fill=title_color, font=font)

# # Load decorations (ensure you have these images available)
# balloon = Image.open("balloon.png").resize((150, 150))
# cake = Image.open("cake.png").resize((300, 300))
# party_emoji = Image.open("party_emoji.png").resize((100, 100))

# # Add balloons to the top corners
# canvas.paste(balloon, (50, 50), balloon)  # Top-left corner
# canvas.paste(balloon, (canvas_width - 200, 50), balloon)  # Top-right corner

# # Add a cake to the center
# center_x = (canvas_width - 300) // 2
# center_y = (canvas_height - 300) // 2
# canvas.paste(cake, (center_x, center_y), cake)

# # Add party emojis to the bottom corners
# canvas.paste(party_emoji, (50, canvas_height - 150), party_emoji)  # Bottom-left
# canvas.paste(party_emoji, (canvas_width - 150, canvas_height - 150), party_emoji)  # Bottom-right

# # Additional details (event info)
# event_text = "Saturday, Nov 4th\n6:00 PM\n123 Party St, FunTown"
# event_color = (0, 100, 200)
# event_font = ImageFont.truetype("arial.ttf", size=50)
# event_width, event_height = draw.textsize(event_text, font=event_font)
# event_x = (canvas_width - event_width) // 2
# event_y = canvas_height - 400  # Near the bottom
# draw.multiline_text((event_x, event_y), event_text, fill=event_color, font=event_font, align="center")

# # Save and show the poster
# canvas.save("party_invitation.png")
# canvas.show()

# # Making a photo transparent for layering
# from PIL import Image

# # Load the image
# image_path = "input_image.png"  # Replace with your image path
# img = Image.open(image_path).convert("RGBA")

# # Get pixel data
# pixels = img.getdata()

# # Define the color to make transparent (e.g., white)
# background_color = (255, 255, 255)  # RGB value of white

# # Create a new pixel data list
# new_pixels = []
# for pixel in pixels:
#     # Check if the pixel matches the background color
#     if pixel[:3] == background_color:
#         # Make this pixel transparent
#         new_pixels.append((255, 255, 255, 0))  # Fully transparent
#     else:
#         # Keep the pixel as is
#         new_pixels.append(pixel)

# # Update the image with the new pixels
# img.putdata(new_pixels)

# # Save the image with a transparent background
# img.save("output_image_with_transparency.png", "PNG")
# img.show()


# #Threshold option
# from PIL import Image

# def is_close(color1, color2, threshold=30):
#     return sum(abs(c1 - c2) for c1, c2 in zip(color1, color2)) < threshold

# image_path = "input_image.png"
# img = Image.open(image_path).convert("RGBA")
# pixels = img.getdata()

# background_color = (255, 255, 255)  # White background
# threshold = 50

# new_pixels = []
# for pixel in pixels:
#     if is_close(pixel[:3], background_color, threshold):
#         new_pixels.append((255, 255, 255, 0))  # Transparent
#     else:
#         new_pixels.append(pixel)

# img.putdata(new_pixels)
# img.save("output_image_with_transparency.png", "PNG")
# img.show()


