# Object-Detector
This is an AI Tool which will be if trained can detect and distinguish the Objects further and give results relavent to it.

## Features

- Cross-platform
- Responsive
- Object detection
- Webcam

## Tech Stack

**Frontend:** HTML, CSS, JavaScript

**Backend:** Python, Flask, Google Teachable Machine

## Run Locally

Clone the project

```bash
  git clone https://github.com/RAJKUMARSHRIVASH/Object-Detector.git
```

Go to the project directory

```bash
  cd Object-Detector
```

Install dependencies

```bash
  pip freeze > requirements.txt
```
```
pip install --upgrade pip
```
```
pip install -r requirements.txt
```
## **How to Set Up a Virtual Environment in Python**

Here are the steps to create a virtual environment in Python:
1. Install the `virtualenv` package:
```
pip install virtualenv
```
2. Navigate to your project directory and create a virtual environment. Here,`my_env` is the name of the virtual environment.
```
cd my_project/ virtualenv my_env
```
3. Now, you have to activate the virtual environment. On `macOS` and `Linux`, you can do this:
```
source my_env/bin/activate
```
On `Windows`:
```
my_env\Scripts\activate
```
4. After the activation, your terminal prompt will change to show the name of the activated environment.

Now, you can install packages into this isolated environment. For example:
```
pip install flask
```
This will install Flask in the **`my_env`** environment, not in your global Python environment. All Python commands like **`python`**, **`pip`**, etc., used in this environment will apply to **`my_env`** only.

1. When you're done with your work, you can deactivate the environment to return to your global Python environment:
```
deactivate
```

Start the server

```bash
  python main.py
```

Open the app on a browser locally
```
http://localhost:5000/
```

## API Reference

#### Welcome 

```http
  GET /
```

#### POST

```http
  POST /classify
```

## Demo
```
https://object-detector.onrender.com
```
## Screenshots

![App Screenshot](https://i.imgur.com/wvZyg9E.png)
## Author

- [@Raj Kumar Sen](https://github.com/RAJKUMARSHRIVASH)

