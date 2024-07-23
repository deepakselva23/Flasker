from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    # print(a)
    raise Exception("This is a test exception!")
    return '<h1> Hello Worldss</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('400.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=False)