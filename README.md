

# 📂 File Uploader App

A simple Python GUI application to **upload** and **download** files via **SFTP** using `ftpretty` and `tkinter`.

This app allows users to select a file from their computer, upload it to a remote SFTP server, and download a preset file from the server.

---

## ✨ Features

- Upload any file from your computer to an SFTP server.
- Download a file (`hello.txt`) from the server.
- User-friendly interface built with **Tkinter**.
- Uses **ftpretty** for SFTP operations.

---

## 📂 Project Structure

```
├── main.py           # GUI application code
├── file_uploader.py  # Handles upload and download via SFTP
└── README.md         # (this file)
```

---

## 🚀 How to Run


### 1. Install dependencies
```bash
pip install ftpretty
```

> Note: Tkinter comes pre-installed with Python on most systems.

### 2. Run the application
```bash
python main.py
```

---

## 🛠 How it Works

- **Upload Button**:
  - Opens a file dialog for you to select a file (default: `.png` or any file).
  - Uploads the selected file to the `/my_upload/` directory on the SFTP server.

- **Download Button**:
  - Downloads `/my_upload/hello.txt` from the server.
  - Saves it locally with the name `done`.

---

## ⚙️ Configuration

The server connection details are hardcoded in `file_uploader.py`:

```python
user = "file_uploader"
password = "mjHV7znKmGdjxsddHfojKWo4lZfk0dO1"
host = "ap-southeast-1.sftpcloud.io"
```
You can modify these if you're connecting to a different server.

---

## 📸 Screenshots

| File Uploader  | 
|:-------------:|
![file_uploader](https://github.com/user-attachments/assets/8f4ba53f-73ff-4072-abb4-b56c08dc784c)


---

## 🙌 Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) – Python's standard GUI library.
- [ftpretty](https://pypi.org/project/ftpretty/) – Simple SFTP/FTP library.
