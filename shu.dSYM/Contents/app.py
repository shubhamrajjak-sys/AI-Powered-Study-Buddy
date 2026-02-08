from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Topic Search App</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 40px; }
        input { padding: 10px; width: 200px; }
        button { padding: 10px; }
        .box { margin-top: 20px; font-size: 20px; }
    </style>
</head>
<body>
    <h2>📱 Topic Search App</h2>
    <form method="post">
        <input name="topic" placeholder="Type a topic">
        <button type="submit">🔍 Search</button>
    </form>

    {% if result %}
    <div class="box">
        <b>Output:</b><br>
        {{ result }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        topic = request.form["topic"].lower()

        if topic == "ai":
            result = "Artificial Intelligence makes machines smart."
        elif topic == "python":
            result = "Python is an easy and powerful programming language."
        elif topic == "flask":
            result = "Flask is a lightweight web framework."
        else:
            result = "Topic not found ❌"

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
