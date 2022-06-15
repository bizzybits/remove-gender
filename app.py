import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        response = openai.Completion.create(model="text-davinci-002",
                                            prompt=generate_prompt(text),
                                            temperature=0.7,
                                            max_tokens=64,
                                            top_p=1.0,
                                            frequency_penalty=0.0,
                                            presence_penalty=0.0)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(text):
    return """Summarize this for a second-grade student: {}""".format(
        text.capitalize())
