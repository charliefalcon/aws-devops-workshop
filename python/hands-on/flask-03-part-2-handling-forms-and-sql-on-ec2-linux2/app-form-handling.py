from flask import Flask, render_template

form_handling_app = flask (__name__)


@app.route('/', methods = [GET, POST])
def home():

    return render_template("index.html", )















if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)