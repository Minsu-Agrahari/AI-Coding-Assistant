from flask import Flask, render_template, request, jsonify
import subprocess
import ollama

app = Flask(__name__)

# Home route that loads the main webpage
@app.route('/')
def index():
    return render_template('index.html')

# API route to handle code processing requests from frontend
@app.route('/process', methods=['POST'])
def process_code():
    try:
        # Get the code and language from the POST request
        data = request.get_json()
        code = data.get('code')
        language = data.get('language')

        # Prepare prompt for the LLM model (Codellama)
        prompt = f"Analyze the following {language} code. Detect any errors, suggest fixes, and explain what the code does.\n\nCode:\n{code}"

        # Run the model using Ollama
        response = ollama.chat(model='codellama', messages=[{"role": "user", "content": prompt}])

        # Extract the response content
        result = response['message']['content']

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
