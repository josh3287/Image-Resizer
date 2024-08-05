# Install pillow
# Open image
# Print current size
# specify size needed
# Save new image
from PIL import Image

image = Image.open('AUTUMN.jpeg')

print(f"Current size: {image.size}")


resized_image = image.resize((500, 500))

resized_image.save('Pythonchngedsize.jpeg')