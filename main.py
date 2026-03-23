import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <div style="min-height:100vh; background:linear-gradient(135deg, #f5f7fa 0%, #e4e8ed 100%); font-family:sans-serif; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:20px;">
        <div style="max-width:400px; width:100%; background:white; padding:40px; border-radius:40px; text-align:center; box-shadow:0 20px 60px rgba(0,0,0,0.05);">
            <h1 style="color:#1a73e8; font-weight:300; letter-spacing:2px;">Tomori Pure AI</h1>
            <p style="color:#7f8c8d; line-height:1.6;">世界最高水準の翻訳体験を、<br>セラミックの透明感とともに。</p>
            <div style="margin:30px 0; padding:20px; background:#fbfcfd; border-radius:20px; border:1px solid #edf2f7;">
                <span style="color:#a0aec0; font-size:0.8em; letter-spacing:1px;">STANDARD PLAN</span>
                <div style="font-size:2.2em; font-weight:bold; color:#2d3748; margin:5px 0;">$2.99<span style="font-size:0.4em; color:#a0aec0;">/mo</span></div>
            </div>
            <a href="https://buy.stripe.com/bJedRbefH5yogzZfuDasg09" style="display:block; background:#1a73e8; color:white; padding:18px; text-decoration:none; border-radius:20px; font-weight:bold; box-shadow:0 10px 25px rgba(26,115,232,0.2);">
                今すぐ購読して開始
            </a>
            <p style="margin-top:30px; font-size:0.75em; color:#cbd5e0; font-style:italic;">
                事務長ステラ：主、ここが私たちの「現金化」の起点ですわ。
            </p>
        </div>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
