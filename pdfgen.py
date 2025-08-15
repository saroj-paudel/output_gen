from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
from PIL import Image

def convert_images_to_pdf(image_folder, output_pdf):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(
        ('.png'))]

    if not image_files:
        print("No image files found in the folder.")
        return
    total_images = len(image_files)
    total_size = 0
    # Sort the image files by file name
    image_files = sorted(image_files)
    progress = 0
    # Create a new PDF file
    c = canvas.Canvas(output_pdf, pagesize=A4)

    # Loop through each image and add it to the PDF
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        total_size += os.path.getsize(image_path)
        try:
            img = Image.open(image_path)
            img_width, img_height = img.size
            aspect_ratio = img_width / img_height
            pdf_width, pdf_height = A4
            # pdf_height = pdf_width / aspect_ratio  # Adjusting height based on aspect ratio
            c.setPageSize((pdf_width, pdf_height))
            c.drawImage(image_path, 0, 0, img_width, img_height,)
            c.showPage()
            
        except Exception as e:
            print(f"Failed to process {image_file}: {str(e)}")

        progress += 1
        print(f"PDF file {progress} is in processing ...")
        # progress_callback(progress, total_images, total_size)
    c.save()
    print(f"PDF file '{output_pdf}' created successfully.")
    return total_size

convert_images_to_pdf("output","myOut.pdf")