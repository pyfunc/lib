#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example demonstrating how to convert a PDF to base64 encoded image.
This example shows how to use the PDF conversion functionality in pyfunc2.
"""

import os
import sys
import base64
from PIL import Image
from pdf2image import convert_from_path

def convert_pdf_to_base64(pdf_path, extension="png", dpi=100):
    """
    Converts the first page of a PDF to base64 (PNG/JPEG) directly from memory.

    Args:
        pdf_path (str): Path to the PDF file
        extension (str): Output image format ('png' or 'jpg')
        dpi (int): Resolution for the output image

    Returns:
        str: Base64 encoded string of the image

    Requires:
        pip install pdf2image pillow
        Poppler must be installed on the system
    """
    # Convert PDF to a list of images (each page as a separate image)
    images = convert_from_path(pdf_path, dpi=dpi, fmt=extension, single_file=True)

    if not images:
        raise ValueError("Failed to convert PDF to image.")

    img = images[0]  # Get the first page

    # Save image to in-memory file
    import io
    in_mem_file = io.BytesIO()

    # Choose format based on extension
    fmt = extension.upper()
    if fmt == "JPG":
        fmt = "JPEG"

    img.save(in_mem_file, format=fmt)
    in_mem_file.seek(0)

    # Read bytes and encode to base64
    img_bytes = in_mem_file.read()
    base64_encoded_result_bytes = base64.b64encode(img_bytes)
    base64_encoded_result_str = base64_encoded_result_bytes.decode('ascii')

    return base64_encoded_result_str


def main():
    """
    Main function to demonstrate the PDF to base64 conversion.
    """
    # Check if a PDF path was provided
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_base64_example.py <path_to_pdf> [extension] [dpi]")
        print("Example: python pdf_to_base64_example.py sample.pdf png 150")
        return

    # Get parameters from command line arguments
    pdf_path = sys.argv[1]
    extension = sys.argv[2] if len(sys.argv) > 2 else "png"
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 100

    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        return

    try:
        # Convert PDF to base64
        base64_result = convert_pdf_to_base64(pdf_path, extension, dpi)

        # Print the first 100 characters of the base64 string
        print(f"Base64 encoded {extension.upper()} (first 100 chars):")
        print(base64_result[:100] + "...")

        # Optionally save the base64 string to a file
        output_file = f"{os.path.splitext(pdf_path)[0]}_base64.txt"
        with open(output_file, "w") as f:
            f.write(base64_result)

        print(f"\nFull base64 string saved to: {output_file}")

        # Show how to use the base64 string in HTML
        print("\nHTML usage example:")
        print(f'<img src="data:image/{extension};base64,{base64_result[:20]}..." />')

    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nMake sure you have installed the required dependencies:")
        print("pip install pdf2image pillow")
        print("And Poppler is installed on your system.")


if __name__ == "__main__":
    main()

# python examples/pdf_to_base64_example.py example_invoice.pdf png 150
