import fitz # PyMuPDF
import os
import json

def extract_pdf_to_text(pdf_path, output_txt_path):
    print(f"Extracting text from: {pdf_path}")
    doc = fitz.open(pdf_path)
    text_blocks = []
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        # Using blocks to preserve reading order roughly
        blocks = page.get_text("blocks")
        # Sort blocks by y0 (vertical) then x0 (horizontal)
        blocks.sort(key=lambda b: (b[1], b[0]))
        
        page_text = []
        for b in blocks:
            if b[4].strip(): # Ignore empty blocks
                # b[4] is the text content of the block
                page_text.append(b[4].strip())
                
        text_blocks.append(f"--- PAGE {page_num + 1} ---")
        text_blocks.append("\n".join(page_text))
        
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(text_blocks))
    print(f"Saved text to: {output_txt_path}")

def extract_images_from_pdf(pdf_path, output_dir):
    print(f"Extracting images from: {pdf_path}")
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    
    img_count = 0
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            image_filename = f"p{page_num + 1:03d}-img{img_index:02d}.{image_ext}"
            image_filepath = os.path.join(output_dir, image_filename)
            
            # Avoid extracting tiny meaningless images like decorative dots/logos
            if len(image_bytes) > 2000:
                with open(image_filepath, "wb") as f:
                    f.write(image_bytes)
                img_count += 1
                
    print(f"Extracted {img_count} useful images to: {output_dir}")

base_dir = "public/downloads/topik/TOPIK II/36"

# 1. Extract Text
extract_pdf_to_text(os.path.join(base_dir, "TOPIK-2-36-exam.pdf"), os.path.join(base_dir, "TOPIK-2-36-exam-utf8.txt"))
extract_pdf_to_text(os.path.join(base_dir, "TOPIK-2-36-answers.pdf"), os.path.join(base_dir, "TOPIK-2-36-answers-utf8.txt"))
extract_pdf_to_text(os.path.join(base_dir, "TOPIK-2-36-transcript.pdf"), os.path.join(base_dir, "TOPIK-2-36-transcript-utf8.txt"))

# 2. Extract Images from Exam
extract_images_from_pdf(os.path.join(base_dir, "TOPIK-2-36-exam.pdf"), os.path.join(base_dir, "media"))
