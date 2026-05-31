import os
from PIL import Image

img_dir = r"a:\SEM4_Complete\DAA_text\extracted_images"
for f in sorted(os.listdir(img_dir)):
    if f.endswith(".png"):
        path = os.path.join(img_dir, f)
        img = Image.open(path)
        print(f"{f}: size={img.size}, mode={img.mode}")
