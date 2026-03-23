import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Language Breaker</title>
    <style>
        body { margin: 0; background: #ffffff; font-family: "Helvetica Neue", Arial, sans-serif; min-height: 100vh; display: flex; align-items: center; justify-content: center; color: #1a1a1a; overflow: hidden; }
        .canvas { text-align: center; width: 100%; max-width: 600px; padding: 20px; animation: fadeIn 2s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        
        .title { font-weight: 100; font-size: 0.9em; letter-spacing: 0.5em; color: #1a73e8; text-transform: uppercase; margin-bottom: 60px; opacity: 0.8; }
        
        .mic-sphere { width: 100px; height: 100px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #4facfe 0%, #00f2fe 100%); margin: 0 auto 40px; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 20px 50px rgba(79,172,254,0.2); transition: 0.5s; border: none; outline: none; }
        .mic-sphere:active { transform: scale(0.9); filter: brightness(1.1); }
        
        .input-placeholder { font-weight: 200; font-size: 1.2em; color: #ccc; letter-spacing: 1px; margin-bottom: 100px; min-height: 1.5em; }
        
        .footer-link { position: fixed; bottom: 40px; font-size: 0.7em; letter-spacing: 2px; }
        .footer-link a { color: #eee; text-decoration: none; transition: 0.3s; }
        .footer-link a:hover { color: #1a73e8; }
    </style>
</head>
<body>
    <div class="canvas">
        <div class="title">Global Language Breaker</div>
        
        <button class="mic-sphere" onclick="startRecognition()">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
        </button>

        <div id="output" class="input-placeholder">Tap to break the barrier</div>

        <div class="footer-link">
            <a href="https://buy.stripe.com/bJedRbefH5yogzZfuDasg09">SUPPORT THE PROJECT $2.99</a>
        </div>
    </div>

    <script>
        function startRecognition() {
            const output = document.getElementById('output');
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (SpeechRecognition) {
                const recognition = new SpeechRecognition();
                recognition.lang = 'ja-JP';
                recognition.onstart = () => { output.innerText = "Listening..."; output.style.color = "#1a73e8"; };
                recognition.onresult = (event) => { output.innerText = event.results[0][0].transcript; };
                recognition.start();
            } else {
                alert("Speech recognition not supported in this browser.");
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
