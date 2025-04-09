# 🧠 AI-Coding-Assistant  
**Offline AI-Powered Coding Assistant**

A smart, AI-driven coding assistant that works **100% offline**!  
It detects errors, explains code, and suggests fixes for **Python, Java, C, and JavaScript** — all without an internet connection.

Powered by open-source LLMs like **TinyLlama** via **Ollama**, and built using **Flask**.


# 🚀 Features

- 💡 Explains code logic clearly
- 🛠 Detects coding errors and suggests possible fixes
- ⚙️ Works offline using local LLM models
- 🐍 Supports **Python, Java, C, and JavaScript**
- 🧪 User-friendly web interface
- 🔧 Built using Flask, HTML, and JavaScript


# 🧰 Tech Stack

- **Backend:** Python, Flask, Requests, Ollama
- **Frontend:** HTML, CSS, JavaScript
- **LLM Model:** TinyLlama (via Ollama)


# 📦 Requirements

- Python 3.x
- [Ollama](https://ollama.com/) installed and running locally
- TinyLlama model pulled via Ollama

```bash
ollama run tinyllama
```

---

# 🛠 Setup Instructions

## 1️⃣ Clone the Project

```bash
git clone https://github.com/your-username/offline-coding-assistant.git
cd offline-coding-assistant
```

## 2️⃣ Create & Activate a Virtual Environment

```bash
python -m venv venv
```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Start Ollama (in a Separate Terminal)

```bash
ollama run tinyllama
```

## 5️⃣ Run the Flask Server

```bash
python app.py
```

Open your browser at:  
**http://localhost:5000**

---

# 📁 Project Structure

```
offline-coding-assistant/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── script.js
│   └── style.css
└── README.md
```

---

# 👨‍💻 Team: SYNTAX SQUAD

| Name            | Role                |
|-----------------|---------------------|
| Minsu Agrahari  | Backend Developer   |
| Aditi Anand     | Frontend Developer  |
| Rinita Saha     | Frontend Developer  |
| Aneesh Das      | Backend Developer   |

---

# 📢 License

This project is open-source and available under the **MIT License**.

---

💡 *Made with passion, code, and open-source intelligence.*
```

---
