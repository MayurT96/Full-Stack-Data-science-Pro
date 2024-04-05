from flask import Flask, render_template # type: ignore
import requests # type: ignore

app = Flask(__name__)

@app.route("/")
def index():
    data = get_data_from_api()
    return render_template("index.html", data=data)

def get_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    app.run(debug=True)