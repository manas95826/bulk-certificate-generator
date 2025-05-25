import streamlit as st
import os
import pandas as pd
import shutil
from certificate_generator_simple import generate_certificate
import tempfile
from zipfile import ZipFile
import io

# Page configuration
st.set_page_config(
    page_title="Geek Room Certificate Generator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        padding-bottom: 5rem;  /* Add padding to prevent content from being hidden behind footer */
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 4px;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stProgress > div > div > div {
        background-color: #4CAF50;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 1rem;
        font-size: 0.9rem;
        color: #666;
        border-top: 1px solid #ddd;
        z-index: 1000;
    }
    .main-header {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 2rem;
    }
    .sub-header {
        color: #34495e;
        margin-top: 2rem;
    }
    .stFileUploader {
        border: 2px dashed #ccc;
        border-radius: 5px;
        padding: 1rem;
    }
    /* Ensure footer is always visible */
    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">Geek Room Certificate Generator</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666;">Create beautiful certificates with ease</p>', unsafe_allow_html=True)

# Create two columns for file uploaders
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h3 class="sub-header">Step 1: Upload Files</h3>', unsafe_allow_html=True)
    template_file = st.file_uploader("📄 Upload Certificate Template (PNG)", type=['png'])
    csv_file = st.file_uploader("📊 Upload CSV File", type=['csv'])

with col2:
    st.markdown('<h3 class="sub-header">Step 2: Configure Settings</h3>', unsafe_allow_html=True)
    y_coordinate = st.number_input("📍 Y-coordinate for name placement", value=570, help="Vertical position where the name will be placed")
    font_size = st.number_input("🔤 Font Size", value=100, help="Size of the font for the name")

# Instructions for CSV format
with st.expander("📋 CSV Format Instructions"):
    st.markdown("""
    ### CSV File Requirements
    Your CSV file should follow this format:
    
    | name |
    |------|
    | John Doe |
    | Jane Smith |
    
    **Important Notes:**
    - The file must be a comma-separated values (CSV) file
    - Must contain a column named 'name'
    - Names should be in the 'name' column
    - No special characters in names
    """)

if template_file and csv_file:
    st.markdown('<h3 class="sub-header">Step 3: Generate Certificates</h3>', unsafe_allow_html=True)
    if st.button("🎨 Generate Certificates"):
        # Create temporary directory for processing
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save uploaded files
            template_path = os.path.join(temp_dir, "template.png")
            with open(template_path, "wb") as f:
                f.write(template_file.getvalue())
            
            # Read CSV
            df = pd.read_csv(csv_file)
            
            # Create output directory
            output_dir = os.path.join(temp_dir, "generated_certificates")
            os.makedirs(output_dir, exist_ok=True)
            
            # Process each certificate
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for idx, row in df.iterrows():
                name = row['name']
                output_path = os.path.join(output_dir, f"{name.replace(' ', '_')}_certificate.png")
                
                try:
                    generate_certificate(
                        template_path=template_path,
                        name=name,
                        output_path=output_path,
                        font_path="Montserrat-Bold.ttf",
                        font_size=font_size,
                        text_color=(255, 255, 255),
                        y=y_coordinate
                    )
                except Exception as e:
                    st.error(f"❌ Error generating certificate for {name}: {str(e)}")
                
                # Update progress
                progress = (idx + 1) / len(df)
                progress_bar.progress(progress)
                status_text.text(f"🔄 Processing: {idx + 1}/{len(df)} certificates")
            
            # Create ZIP file
            zip_buffer = io.BytesIO()
            with ZipFile(zip_buffer, 'w') as zip_file:
                for root, dirs, files in os.walk(output_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, output_dir)
                        zip_file.write(file_path, arcname)
            
            # Prepare ZIP for download
            zip_buffer.seek(0)
            
            # Download button
            st.download_button(
                label="📥 Download Certificates (ZIP)",
                data=zip_buffer,
                file_name="certificates.zip",
                mime="application/zip"
            )
            
            st.success("✅ Certificate generation completed!")

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ by Manas Chopra
    </div>
""", unsafe_allow_html=True)

# Add some spacing at the bottom to ensure content isn't hidden
st.markdown("<br><br><br>", unsafe_allow_html=True) 