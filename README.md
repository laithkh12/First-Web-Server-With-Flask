# Flask Decorators App 🎉

Welcome to the **Flask Decorators App**! This Flask web application demonstrates the usage of custom decorators and dynamic URL parameters.

## 🛠️ Features

- **Home Route (`/`)**: Displays a styled "Hello World!" message.
- **Goodbye Route (`/bye`)**: Returns a "Bye!" message with custom decorations (bold, emphasis, and underline).
- **Greet Route (`/username/<name>/<int:number>`)**: A dynamic route that greets the user by name and age.

## 🚀 Installation

Follow these steps to get your app up and running.

### Prerequisites

- **Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
- **Flask**: Install Flask using pip.

```bash
pip install flask
```
---
## Setup
1. Save the following Python code in a file called hello.py:
```python
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
```
2. Set the FLASK_APP environment variable: For Windows (PowerShell):
```bash
$env:FLASK_APP = "hello.py"
```
For macOS/Linux:
```bash
export FLASK_APP=hello.py
```
3. Run the Flask development server:
```bash
python -m flask run
```
Now, visit http://127.0.0.1:5000/ in your browser, and you should see the "Hello World!" message. Visiting http://127.0.0.1:5000/bye will return "Bye!" with decorations, and http://127.0.0.1:5000/username/<name>/<int:number> will greet you with a personalized message.
---
## ⚙️ Environment Configuration
If you want to run this app in production, it's recommended to set up a production-ready server like Gunicorn or uWSGI.
---
## 📚 Learn More
- Flask Documentation: https://flask.palletsprojects.com/
- Python Documentation: https://docs.python.org/
---
## 💡 License
This project is open-source and available under the MIT License.
---
Happy coding! 🎉
