from flask import Flask, render_template, request

app = Flask(name)

def ai_buddy(topic):
    t = topic.lower()

    data = {
        "artificial intelligence": (
            "AI allows machines to think and act like humans.",
            "AI simulates human intelligence.",
            "1. What is AI?\n2. One use of AI?\n3. Advantage of AI?"
        ),
        "machine learning": (
            "Machine Learning helps systems learn from data.",
            "ML is a subset of AI.",
            "1. What is ML?\n2. One ML algorithm?\n3. Application of ML?"
        ),
        "python": (
            "Python is an easy and powerful programming language.",
            "Python is widely used in AI and web.",
            "1. What is Python?\n2. One feature?\n3. Use of Python?"
        ),
        "physics": (
            "Physics studies matter, energy and motion.",
            "Physics explains natural laws.",
            "1. What is Physics?\n2. One branch?\n3. Importance?"
        ),
        "data science": (
            "Data Science extracts knowledge from data.",
            "Data Science uses data analysis.",
            "1. What is Data Science?\n2. Tools used?\n3. Applications?"
        ),
        "cloud computing": (
            "Cloud computing provides online computing services.",
            "Cloud delivers storage and servers online.",
            "1. What is Cloud Computing?\n2. One service?\n3. Advantage?"
        )
    }

    for key in data:
        if key in t:
            return data[key]

    return (
        f"{topic} is an important study topic.",
        f"{topic} is useful in real life.",
        f"1. What is {topic}?\n2. One use?\n3. Importance?"
    )


@app.route("/", methods=["GET", "POST"])
def home():
    explanation = summary = quiz = ""

    if request.method == "POST":
        topic = request.form["topic"]
        explanation, summary, quiz = ai_buddy(topic)

    return render_template("index.html",
                           explanation=explanation,
                           summary=summary,
                           quiz=quiz)

if name == "main":
    app.run(debug=True)