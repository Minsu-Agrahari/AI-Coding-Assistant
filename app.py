# 🔧 Key Features:
# Accepts code and language from the frontend via a /process POST route.
# Returns the AI-generated result as JSON to the frontend.

from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Home route that loads the main webpage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('indexPage2.html')

# API route to handle code processing requests from frontend
@app.route('/process', methods=['POST'])
def process_code():
    try:
        # Get the code and language from the POST request
        data = request.get_json()
        code = data.get('code')
        language = data.get('language')

        # Prepare prompt for the LLM model (TinyLlama)
        prompt = f"Analyze the following {language} code. Detect any errors, suggest fixes, and explain what the code does.\n\nCode:\n{code}"

        # Run the model using TinyLlama through Ollama
        response = ollama.chat(model='tinyllama', messages=[{"role": "user", "content": prompt}])

        # Extract the response content
        result = response['message']['content']

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
