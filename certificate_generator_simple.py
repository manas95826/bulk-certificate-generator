import os
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO

def generate_certificate(template_path, name, output_path, font_path, font_size=180, text_color=(255, 255, 255), y=570):
    """
    Generate a certificate with the participant's name, centered on the line after 'Proudly Presented To-'.
    
    Args:
        template_path (str): Path to the certificate template image
        name (str): Name of the participant
        output_path (str or BytesIO): Path where the generated certificate will be saved or a BytesIO object
        font_path (str): Path to the TTF font file
        font_size (int): Size of the font for the name
        text_color (tuple): RGB color for the text
        y (int): Y coordinate for the text position
    """
    # Open the template image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    
    # Use the provided TTF font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"Font load error: {e}. Using default font (may be small and not bold).")
        font = ImageFont.load_default()
    
    # Calculate text width and position
    text_width = draw.textlength(name, font=font)
    x = (img.width - text_width) // 2
    # Draw the text at (x, y)
    draw.text((x, y), name, font=font, fill=text_color)
    
    # Save the certificate
    if isinstance(output_path, BytesIO):
        img.save(output_path, format='PNG')
    else:
        img.save(output_path)
    return output_path

def process_certificate(args):
    """Helper function to process a single certificate for threading"""
    template_path, name, output_path, font_path, font_size, text_color, y = args
    try:
        generate_certificate(template_path, name, output_path, font_path, font_size, text_color, y)
        return f"Generated certificate for {name}"
    except Exception as e:
        return f"Error generating certificate for {name}: {str(e)}"

def main():
    # Configuration
    template_path = "online.png"  # Path to your certificate template
    csv_path = "data.csv"  # Path to your CSV file
    output_dir = "generated_certificates_1"  # Directory to save generated certificates
    font_path = "Montserrat-Bold.ttf"  # Path to your TTF font file
    font_size = 100  # Adjust as needed
    y = 1050  # Y-coordinate for text placement
    
    # Thread pool configuration optimized for M4 Pro
    # M4 Pro has excellent multi-threading capabilities and can handle high concurrent loads
    # For I/O-bound tasks like image processing, we can use a higher thread count
    # The M4 Pro's unified memory architecture and efficient thread scheduling
    # allows for better handling of multiple concurrent tasks
    max_workers = 512  # Optimized for M4 Pro's capabilities
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read participant data from CSV
    df = pd.read_csv(csv_path)
    
    # Prepare arguments for each certificate generation task
    tasks = []
    for index, row in df.iterrows():
        name = row['name']
        output_path = os.path.join(output_dir, f"{name.replace(' ', '_')}_certificate.png")
        tasks.append((template_path, name, output_path, font_path, font_size, (255, 255, 255), y))  # Changed text color to white
    
    # Process certificates using thread pool
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_task = {executor.submit(process_certificate, task): task for task in tasks}
        
        # Process completed tasks as they finish
        for future in as_completed(future_to_task):
            result = future.result()
            print(result)

if __name__ == "__main__":
    main() 