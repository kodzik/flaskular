from webapp import create_app
from flask import render_template

app = create_app('testing') # <---- CHOOSE CONFIG NAME 

# @cross_origin()
@app.route('/')
def index_route():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)