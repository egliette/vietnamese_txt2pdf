# 📋 Vietnamese TXT to PDF Converter

Converting either a single TXT file or all TXT files in a directory to PDF format.

## 💬 Prerequisites

- Python 3.12.0

## ⚙️ Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/txt-to-pdf-converter.git
cd txt-to-pdf-converter
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
### Convert a Single TXT File

To convert a single TXT file to PDF, use the --file flag:

```bash
python convert.py --file path/to/your/file.txt --target output_file.pdf
```

### Convert All TXT Files in a Directory
To convert all TXT files in a directory to individual PDFs, use the --dir flag:

```bash
python convert.py --dir path/to/your/directory --target output_directory
```

## ✍️ Example

### Convert a single file
```bash
python convert.py --file book.txt --target book.pdf
```

### Convert all files in a directory
```bash
python convert.py --dir books --target books_pdf
```

## 📎 References

- [Ankida New Basic Font](https://www.fontsquirrel.com/fonts/andika-basic)
