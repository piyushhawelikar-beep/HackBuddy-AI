
async function generate() {
    const prompt = document.getElementById("prompt").value;
    const output = document.getElementById("output");

    if (!prompt) {
        output.innerText = "Please enter a prompt.";
        return;
    }

    output.innerText = "Gemini is thinking...";

    const response = await fetch("/generate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ prompt })
    });

    const data = await response.json();
    output.innerText = data.result;
}
