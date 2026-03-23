import os
import google.generativeai as genai
from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# --- STELLAR LAYER: SECURITY CONFIG ---
# NEゲートウェイ環境変数からAPIキーを取得（直書き厳禁）
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# 事務長の拘り：エフェメラル（揮発性）プロンプト
# データを学習させず、その場限りの構造変換を行うための制約
SYSTEM_INSTRUCTION = """
Role: Stellar-Layer Language Breaker.
Constraint: 
1. Process input ephemerally. Do not retain context.
2. Output must be a high-precision 'Pivot Translation' (JP <-> EN).
3. Tone: Noir, Professional, Minimalist.
4. Privacy: Remove any PII (Personally Identifiable Information) during processing.
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0,viewport-fit=cover">
    <title>GLB | NEXT BASE</title>
    <style>
        :root { --gold: #d6b25e; --bg: #050505; --blue: #1a73e8; }
        body { margin: 0; background: var(--bg); color: #fff; font-family: "Helvetica Neue", sans-serif; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .canvas { text-align: center; width: 90%; max-width: 400px; }
        .status-tag { font-size: 9px; color: var(--blue); letter-spacing: 2px; margin-bottom: 40px; border: 1px solid var(--blue); padding: 4px 10px; display: inline-block; }
        .mic-sphere { width: 100px; height: 100px; border-radius: 50%; background: radial-gradient(circle, #222, #000); border: 1px solid var(--gold); cursor: pointer; transition: 0.4s; position: relative; }
        .mic-sphere.active { box-shadow: 0 0 30px var(--blue); border-color: var(--blue); transform: scale(1.1); }
        .output { margin-top: 40px; min-height: 80px; }
        .original { font-size: 14px; color: #666; margin-bottom: 10px; }
        .translated { font-size: 20px; color: var(--gold); font-weight: 200; letter-spacing: 1px; }
        .footer { position: fixed; bottom: 40px; font-size: 10px; color: #333; letter-spacing: 2px; }
    </style>
</head>
<body>
    <div class="canvas">
        <div class="status-tag">SECURED BY NE-GATEWAY : EPHEMERAL MODE</div>
        <button id="micBtn" class="mic-sphere">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="1"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/></svg>
        </button>
        <div class="output">
            <div id="original" class="original">...Ready to Break</div>
            <div id="translated" class="translated"></div>
        </div>
        <div class="footer">© NEXT BASE | PRJ-01</div>
    </div>

    <script>
        const btn = document.getElementById('micBtn');
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'ja-JP';

        btn.onclick = () => { recognition.start(); btn.classList.add('active'); };

        recognition.onresult = async (event) => {
            btn.classList.remove('active');
            const text = event.results[0][0].transcript;
            document.getElementById('original').innerText = text;

            // NEゲートウェイ・エンドポイントへポスト
            const res = await fetch('/process', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: text})
            });
            const data = await res.json();
            document.getElementById('translated').innerText = data.result;
        };
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/process", methods=["POST"])
def process():
    # 事務長の鉄則：受け取った瞬間に処理し、ログには残さない
    data = request.json
    input_text = data.get("text", "")
    
    if not input_text:
        return jsonify({"result": ""})

    # ステラレイヤーによる言語突破ロジック
    prompt = f"{SYSTEM_INSTRUCTION}\n\nInput: {input_text}\nOutput:"
    response = model.generate_content(prompt)
    
    # 揮発性レスポンス：メモリから即座に返す
    return jsonify({"result": response.text.strip()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
