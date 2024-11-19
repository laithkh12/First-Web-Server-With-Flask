# Flask Hello World App 🚀

Welcome to the **Flask Hello World** app! This is a simple web application that demonstrates basic Flask routing and setup.

## 🛠️ Features

- **Home Route (`/`)**: Returns a "Hello World!" message.
- **Goodbye Route (`/bye`)**: Returns a "Bye!" message.

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

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/bye')
def say_bye():
    return "Bye!"

if __name__ == '__main__':
    app.run()
```
2. Set the FLASK_APP environment variable:
For Windows (PowerShell):
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
Now, visit http://127.0.0.1:5000/ in your browser, and you should see the "Hello World!" message. Visiting http://127.0.0.1:5000/bye will return "Bye!".
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
