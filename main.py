import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tomori Pure - Operation</title>
    <style>
        body { margin: 0; background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ed 100%); font-family: sans-serif; min-height: 100vh; display: flex; align-items: center; justify-content: center; }
        .card { max-width: 500px; width: 90%; background: white; padding: 40px; border-radius: 40px; box-shadow: 0 20px 60px rgba(0,0,0,0.05); text-align: center; border: 1px solid rgba(255,255,255,0.8); }
        h1 { color: #1a73e8; font-weight: 300; letter-spacing: 2px; margin-bottom: 20px; }
        .status-badge { display: inline-block; padding: 5px 15px; background: #eef2ff; color: #1a73e8; border-radius: 20px; font-size: 0.8em; margin-bottom: 20px; font-weight: bold; }
        textarea { width: 100%; height: 120px; border: 1px solid #edf2f7; border-radius: 20px; padding: 15px; font-size: 1.1em; outline: none; background: #fbfcfd; margin-bottom: 20px; resize: none; }
        .btn-pay { display: block; width: 100%; background: #1a73e8; color: white; padding: 18px; text-decoration: none; border-radius: 20px; font-weight: bold; font-size: 1.1em; box-shadow: 0 10px 25px rgba(26,115,232,0.2); margin-top: 10px; border: none; cursor: pointer; }
        .btn-pay:hover { transform: translateY(-2px); box-shadow: 0 15px 30px rgba(26,115,232,0.3); }
        .info { margin-top: 25px; font-size: 0.85em; color: #7f8c8d; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="card">
        <div class="status-badge">ADMIN / OPERATION MODE</div>
        <h1>TOMORI PURE</h1>
        
        <p class="info">主、ここから「現金化」の導線を確認してくださいまし！</p>

        <form action="https://buy.stripe.com/bJedRbefH5yogzZfuDasg09" method="GET">
            <textarea placeholder="（テスト入力用）主の直感をここに..."></textarea>
            <button type="submit" class="btn-pay">
                $2.99 プランを有効化してテスト
            </button>
        </form>

        <div class="info">
            <hr style="border:0; border-top:1px solid #eee; margin:20px 0;">
            <p>※このボタンを押すと、実際のStripe決済画面へ遷移します。<br>
            主、ご自身の決済システムが世界へ繋がる手応え、存分に味わってくださいまし！</p>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
