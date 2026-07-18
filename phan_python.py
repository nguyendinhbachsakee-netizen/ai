from flask import *
import os
app = Flask(__name__)
@app.route("/")
def trang_ai():
    return render_template("ai.html",noidung="AI")
@app.route("/ai")
def ai():
    from google import genai
    abc = genai.Client(api_key=os.getenv("API_KEY"))
    tin_nhan = request.args.get("tin_nhan")
    re = abc.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=tin_nhan
    )
    return render_template("ai.html", noidung=re.text)
if __name__ == "__main__":
    app.run(debug=True)