document.getElementById("submit-btn").addEventListener("click", async function() {
    const code = document.getElementById("code").value;
    const language = document.getElementById("language").value;

    const data = {
        code: code,
        language: language
    };

    try {
        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.error) {
            document.getElementById("output").textContent = `Error: ${result.error}`;
        } else {
            document.getElementById("output").textContent = result.result;
        }
    } catch (error) {
        document.getElementById("output").textContent = `Failed to analyze code: ${error.message}`;
    }
});