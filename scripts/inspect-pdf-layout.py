import fitz # PyMuPDF
import os

pdf_path = "public/downloads/topik/TOPIK II/36/TOPIK-2-36-exam.pdf"
if not os.path.exists(pdf_path):
    # Try backup path if deleted
    pdf_path = "public/downloads/topik/TOPIK II/36/TOPIK-2-36-exam.pdf" # It's in the same place

doc = fitz.open(pdf_path)
print(f"Exam PDF has {len(doc)} pages.")

# Let's inspect pages from page 17 onwards (Reading section starts around page 17-18)
# We want to see where images are located in the PDF pages
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    images = page.get_images(full=True)
    if images:
        print(f"Page {page_num + 1} has {len(images)} images.")
        # Print a snippet of text on this page to identify the question numbers
        text = page.get_text()
        q_matches = re.findall(r'(\d+)\.', text)
        print(f"  Detected question numbers on page: {q_matches}")
        for img_idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            print(f"    Image {img_idx+1}: size={len(base_image['image'])}, ext={base_image['ext']}")
