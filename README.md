# Bulk Certificate Generator 🎓

A powerful and user-friendly web application built with Streamlit that allows you to generate multiple certificates in bulk using a template and a CSV file. Perfect for events, workshops, courses, and any occasion where you need to create multiple certificates quickly and efficiently.


## ✨ Features

- 🖼️ **Easy Template Upload**: Upload your certificate template in PNG format
- 📊 **Bulk Processing**: Process multiple certificates at once using a CSV file
- 🎨 **Customizable**: Adjust font size and text positioning
- 📦 **Batch Download**: Download all generated certificates as a single ZIP file
- ⚡ **Fast Processing**: Efficient certificate generation with progress tracking
- 🎯 **User-Friendly Interface**: Clean and intuitive design
- 📱 **Responsive Design**: Works on both desktop and mobile devices

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/manas95826/bulk-certificate-generator.git
   cd bulk-certificate-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📋 Requirements

- Python 3.7+
- Streamlit
- Pillow (PIL)
- Pandas
- Montserrat-Bold.ttf font file

## 📝 CSV Format

Your CSV file should follow this format:

| name |
|------|
| John Doe |
| Jane Smith |

**Important Notes:**
- The file must be a comma-separated values (CSV) file
- Must contain a column named 'name'
- Names should be in the 'name' column
- Avoid special characters in names

## 🛠️ Configuration

The application allows you to customize:
- Font size
- Y-coordinate for name placement
- Text color (default: white)

## 💻 Usage

1. **Upload Files**
   - Upload your certificate template (PNG format)
   - Upload your CSV file with participant names

2. **Configure Settings**
   - Adjust the Y-coordinate for name placement
   - Set the font size

3. **Generate Certificates**
   - Click the "Generate Certificates" button
   - Wait for the processing to complete
   - Download the ZIP file containing all certificates

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Made with ❤️ by [Manas Chopra](https://github.com/manas95826)

## 🙏 Acknowledgments

- Streamlit for the amazing web framework
- Pillow for image processing capabilities
- All contributors and users of this project

## ⭐ Support

If you find this project helpful, please give it a star on GitHub! Your support means a lot.

---

<p align="center">
  Made with ❤️ by Manas Chopra
</p> 