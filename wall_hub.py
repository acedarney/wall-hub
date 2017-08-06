from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open('api_key.txt') as f:
        key = f.read()
    return render_template('header_footer.html', key=key)


if __name__ == '__main__':
    app.run()
