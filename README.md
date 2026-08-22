# 🧠 Academic Integrity Predictor

An AI-powered plagiarism detection system that uses **Sentence Transformers** and **semantic similarity** to compare documents beyond simple keyword matching.

Unlike traditional plagiarism checkers, this project understands the meaning of sentences and can detect paraphrased or semantically similar content.

---

## 🚀 Features

- 📄 Text vs Text Comparison
- 📂 One-to-One File Comparison
- 📚 One-to-Many File Comparison
- 📝 Supports TXT, PDF, and DOCX files
- 🧠 Semantic Similarity using Sentence Transformers
- 🎯 Sentence-level Similarity Highlighting
- 🌐 Flask-based Web Application
- 🎨 Modern Responsive User Interface

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### AI / Machine Learning
- Sentence Transformers
- all-mpnet-base-v2
- PyTorch

### Libraries
- pdfplumber
- python-docx
- NLTK

---

## 📁 Project Structure

```
Academic-Integrity-Predictor/
│
├── app.py
├── model.py
├── plagiarism.py
├── utils.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dineshmishra17/Academic-Integrity-Predictor.git
```

Move into the project directory

```bash
cd Academic-Integrity-Predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. Upload or enter text.
2. Extract text from PDF, DOCX, or TXT files.
3. Generate sentence embeddings using Sentence Transformers.
4. Compute cosine similarity.
5. Highlight semantically similar sentences.
6. Display plagiarism percentage and comparison results.

---

## 📊 Supported Comparison Modes

- Text ↔ Text
- File ↔ File
- One File ↔ Multiple Files

---

## 📌 Future Improvements

- Web-based plagiarism detection
- PDF report generation
- CSV export
- User authentication
- Dashboard analytics
- Cloud deployment
- Database integration

---

## 📸 Screenshots

<img width="1892" height="911" alt="image" src="https://github.com/user-attachments/assets/35829c0f-5cf7-465b-9f67-babaf67bca4e" />


Example:

<img width="1883" height="912" alt="image" src="https://github.com/user-attachments/assets/734f27ef-894c-4cc9-95d9-8dcc344a51c0" />


## 👨‍💻 Author

**Dinesh Mishra**

GitHub: https://github.com/dineshmishra17

---

## 📜 License

This project is developed for educational and learning purposes.
