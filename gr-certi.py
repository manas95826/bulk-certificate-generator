import streamlit as st
from PIL import Image
import os
from certificate_generator_simple import generate_certificate
import io

def main():
    st.title("Certificate Generator")
    st.write("Enter your name to generate a personalized certificate!")

    # Input for name
    name = st.text_input("Enter your name:")
    
    # Dropdown for certificate type
    certificate_type = st.selectbox(
        "Select Certificate Type",
        ["Vibathon", "Code Cubicle 4"]
    )

    # Single button for certificate generation
    if st.button("Generate Certificate", key="generate_btn"):
        if not name:
            st.warning("Please enter your name first!")
            return
            
        try:
            # Configuration based on certificate type
            if certificate_type == "Vibathon":
                template_path = "online.png"
                font_path = "Montserrat-Bold.ttf"
                font_size = 100
                y = 1050
                text_color = (255, 255, 255)  # White text
            else:  # Code Cubicle 4
                template_path = "online-1.png"
                font_path = "Montserrat-Bold.ttf"
                font_size = 100
                y = 1350  # Different y-value for Code Cubicle 4
                text_color = (0, 0, 0)  # Black text
            
            # Create a BytesIO object to store the certificate
            img_buffer = io.BytesIO()
            
            # Generate certificate directly to memory
            generate_certificate(
                template_path=template_path,
                name=name,
                output_path=img_buffer,  # Pass BytesIO instead of file path
                font_path=font_path,
                font_size=font_size,
                text_color=text_color,
                y=y
            )
            
            # Seek to the beginning of the BytesIO object
            img_buffer.seek(0)
            
            # Create download button
            st.download_button(
                label="Download Certificate",
                data=img_buffer,
                file_name=f"{name.replace(' ', '_')}_{certificate_type.lower().replace(' ', '_')}_certificate.png",
                mime="image/png",
                key="download_btn"
            )
            
            # Display preview
            st.image(img_buffer, caption="Certificate Preview", use_container_width=True)
            
        except Exception as e:
            st.error(f"Error generating certificate: {str(e)}")

if __name__ == "__main__":
    main() 