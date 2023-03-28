import folium
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    map = folium.Map()
    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)