import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>Global Language Breaker</title>
    <style>
        :root { --main-blue: #1a73e8; --ceramic-white: #ffffff; --noir-text: #1c1c1e; }
        body { margin: 0; padding: 0; background: var(--ceramic-white); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica; min-height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; -webkit-tap-highlight-color: transparent; }
        .canvas { text-align: center; width: 100%; max-width: 400px; padding: 40px; box-sizing: border-box; }
        
        .title { font-weight: 200; font-size: 0.75em; letter-spacing: 0.6em; color: var(--main-blue); text-transform: uppercase; margin-bottom: 80px; animation: letterSpacing 2s ease-out; }
        @keyframes letterSpacing { from { letter-spacing: 1.5em; opacity: 0; } to { letter-spacing: 0.6em; opacity: 1; } }
        
        .mic-sphere { width: 120px; height: 120px; border-radius: 60px; background: radial-gradient(circle at 30% 30%, #4facfe 0%, #00f2fe 100%); margin: 0 auto 50px; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 30px 60px rgba(79,172,254,0.3); border: none; outline: none; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .mic-sphere:active { transform: scale(0.92); filter: brightness(1.1); box-shadow: 0 10px 30px rgba(79,172,254,0.2); }
        .recording { animation: pulse 1.5s infinite ease-in-out; background: #ff3b30 !important; }
        @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(255,59,48,0.4); } 70% { box-shadow: 0 0 0 30px rgba(255,59,48,0); } 100% { box-shadow: 0 0 0 0 rgba(255,59,48,0); } }

        .output-area { min-height: 120px; font-weight: 300; font-size: 1.3em; color: var(--noir-text); line-height: 1.6; letter-spacing: 0.02em; transition: 0.3s; }
        .translation { margin-top: 20px; color: var(--main-blue); font-weight: 500; font-size: 1.1em; opacity: 0; transform: translateY(10px); transition: 0.5s; }
        .show { opacity: 1; transform: translateY(0); }

        .footer { position: fixed; bottom: 50px; width: 100%; left: 0; font-size: 0.65em; letter-spacing: 3px; }
        .footer a { color: #d1d1d6; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>
    <div class="canvas">
        <div class="title">Global Language Breaker</div>
        
        <button id="micBtn" class="mic-sphere">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
        </button>

        <div id="originalText" class="output-area">Break the Silence.</div>
        <div id="translatedText" class="translation"></div>

        <div class="footer">
            <a href="https://buy.stripe.com/bJedRbefH5yogzZfuDasg09">RESERVE FULL ACCESS $2.99</a>
        </div>
    </div>

    <script>
        const micBtn = document.getElementById('micBtn');
        const original = document.getElementById('originalText');
        const translated = document.getElementById('translatedText');

        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SpeechRecognition) {
            const recognition = new SpeechRecognition();
            recognition.lang = 'ja-JP';

            micBtn.onclick = () => {
                recognition.start();
                micBtn.classList.add('recording');
                original.innerText = "Listening...";
                translated.classList.remove('show');
            };

            recognition.onresult = (event) => {
                const text = event.results[0][0].transcript;
                original.innerText = text;
                micBtn.classList.remove('recording');
                
                // --- ノワール・疑似翻訳エンジン起動 ---
                setTimeout(() => {
                    translated.innerText = "Breaking the language barrier...";
                    translated.classList.add('show');
                }, 800);
            };

            recognition.onerror = () => {
                micBtn.classList.remove('recording');
                original.innerText = "Try again, Master.";
            };
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
