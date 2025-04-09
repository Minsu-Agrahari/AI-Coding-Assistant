# 🧠 AI-Coding-Assistant  
**Offline AI-Powered Coding Assistant**

A smart, AI-driven coding assistant that works **offline**!  
It detects errors, explains code, and suggests fixes for **Python, Java, C, and JavaScript** — all without needing an internet connection.

Powered by **open-source LLMs** (like `CodeLlama`) via **Ollama**, and built using **Flask**.


# 🚀 Features

- 💡 Explains code logic
- 🛠 Detects errors and suggests fixes
- ⚙️ Works offline using local models
- 🐍 Supports Python, Java, C, JavaScript
- 🧪 Simple web-based UI
- 🔧 Built with Flask + HTML + JS


# 🧰 Tech Stack

- **Backend:** Python, Flask, Requests, Ollama
- **Frontend:** HTML, CSS, JavaScript
- **LLM Model:** CodeLlama (via Ollama)


## 📦 Requirements

- Python 3.x
- [Ollama](https://ollama.com/) (installed & running locally)
- CodeLlama model pulled via Ollama:

```bash
ollama run codellama
```


# 🛠 Setup Instructions

## 1️⃣ Clone the project

```bash
git clone https://github.com/your-username/offline-coding-assistant.git
cd offline-coding-assistant
```

### 2️⃣ Create & activate virtual environment

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

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start Ollama (in a separate terminal)

```bash
ollama run codellama
```

### 5️⃣ Run the Flask server

```bash
python app.py
```

Then open your browser at:  
**http://localhost:5000**

---

## 📁 Project Structure

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

## 👨‍💻 Team: SYNTAX SQUAD

| Name            | Role         |
|-----------------|--------------|
| Minsu Agrahari  | Team Leader  |
| Aditi Anand     | Developer    |
| Rinita Saha     | Developer    |
| Aneesh Das      | Developer    |

---

## 📢 License

This project is open-sourced under the **MIT License**.

---
```

You're doing great — this is shaping up into an awesome project! 🚀