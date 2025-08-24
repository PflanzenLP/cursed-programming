# i actively use:
import os
image_path = os.path.join(os.path.dirname(__file__), "image.png")
with open(image_path):
    ...

# instead of:
with open("image.png"):
    ...