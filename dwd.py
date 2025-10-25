from PIL import Image

# Open the image
img = Image.open("input_image.jpg")

# Rotate the image by a specific angle (e.g., 90 degrees counter-clockwise)
rotated_img = img.rotate(90)

# Rotate the image by a specific angle and expand the canvas to fit the entire image
# rotated_img_expanded = img.rotate(45, expand=True)

# Save the rotated image
rotated_img.save("rotated_image_pillow.jpg")

# To rotate by fixed 90-degree increments efficiently (no arbitrary angles)
# rotated_90_clockwise = img.transpose(Image.ROTATE_90)
# rotated_180 = img.transpose(Image.ROTATE_180)
# rotated_270_clockwise = img.transpose(Image.ROTATE_270)
