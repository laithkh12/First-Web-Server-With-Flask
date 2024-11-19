from flask import Flask

app = Flask(__name__)

# Define the decorators
def make_bold(f):
    def wrapper():
        return f"<b>{f()}</b>"
    return wrapper

def make_emphasis(f):
    def wrapper():
        return f"<em>{f()}</em>"
    return wrapper

def make_underlined(f):
    def wrapper():
        return f"<u>{f()}</u>"
    return wrapper

@app.route('/')
def hello_world():
    return ("<h1 style='text-align: center'>Hello World!</h1>"
            "<p>This is a paragraph</p>")

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old."

if __name__ == '__main__':
    app.run(debug=True)
