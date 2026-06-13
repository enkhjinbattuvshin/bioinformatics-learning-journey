#Paste this into your extract.py file, save it, and run it

import fitz  # This is the PyMuPDF library
import os

# 1. Setup our files and folders
pdf_filename = "paper.pdf"
output_folder = "extracted_figures"

# Create a folder to hold the images if it doesn't exist yet
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print("Opening your PDF...")
doc = fitz.open(pdf_filename)
image_count = 0

# 2. Go through every page and pull out the images
for page_num in range(len(doc)):
    page = doc[page_num]
    images = page.get_images(full=True)
    
    for img_index, img in enumerate(images, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Name the file (e.g., Page_3_Image_1.png)
        image_name = f"Page_{page_num + 1}_Image_{img_index}.{image_ext}"
        image_path = os.path.join(output_folder, image_name)
        
        # Save the image to your computer
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        
        image_count += 1

print(f"Success! Extracted {image_count} total images into the '{output_folder}' folder.")
