from flask import Flask, request, render_template
from model import classifier
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/", methods=['GET','POST'])
def classifierA():
    if request.method == "POST":
        url = request.form.get("url")
        out = classifier(url)
        return render_template("index.html",out=out)

    return render_template("index.html",out="")

if __name__ == "__main__":
    app.run(debug=True)