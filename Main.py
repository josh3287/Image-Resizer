# Install pillow
# Open image
# Print current size
# specify size needed
# Save new image
from PIL import Image

image = Image.open('AUTUMN.jpeg')

print(f"Current size: {image.size}")
