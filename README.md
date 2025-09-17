# Integricheck

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/github/license/Khanshs/integricheck)](https://github.com/Khanshs/integricheck/blob/main/LICENSE)  
[![Stars](https://img.shields.io/github/stars/Khanshs/integricheck?style=social)](https://github.com/Khanshs/integricheck/stargazers)  
[![Issues](https://img.shields.io/github/issues/Khanshs/integricheck)](https://github.com/Khanshs/integricheck/issues)  

---

A simple Python-based file integrity checker for learning and practice.  
Users can calculate file hashes, log results, and verify integrity of files against stored records.  
This helps detect file modifications, corruption, or tampering.  

---

## Features
- Calculate file hash (MD5, SHA256, SHA512, etc.)  
- Process files in chunks (efficient for large files)  
- Save integrity records into a log file (`hash_log.txt`)  
- Compare current file hash with stored record  
- Lightweight and easy to use CLI  

---

## Installation & Usage

Clone the repository and run the program:

```bash
git clone https://github.com/Khanshs/integricheck.git
cd integricheck
python File_Integrity_improved.py
```

## Demo 

```bash
Enter file or folder path: ./File_Integrity
[FOLDER] ./File_Integrity/test1.txt
[sha256] Hash: e3b0c44...
...
```

## Folder Structure
```bash
integricheck/
│
├── File_Integrity/              # Test files for checking integrity (can add more files)
│   ├── test1.txt
│   ├── test2.txt
│   └── text3.bat
│
├── File_Integrity_improved.py   # Main Python script
├── README.md                    # Project documentation
└── LICENSE                      # License file
```

## Note 
Integrity logs are saved in hash_log.json
File is processed in chunks (8192 bytes) to support large files efficiently
Project is experimental, mainly for self-learning and practice

## Acknowledgements
Inspired by traditional file integrity monitoring tools
Built as a learning project for practicing Python & Git
Thanks to the open-source community for providing guidance
