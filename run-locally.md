# Steps for running hackasaurus web application locally:

##Clone the repository.

```
git clone https://github.com/rogermyang/TStream.git
```

##Navigate into the src directory. 

```
cd .\path\to\TStream\src\
```

##Create a virtualenv and activate it:

```
python3 -m venv venv
```

On Windows cmd:

```
$ py -3 -m venv venv
```

##Activate the virtual environment. 

```
.\venv\Scripts\activate
```

##Run flask application	

Setting FLASK_APP on linux:

```
export FLASK_APP=app.py
```

Or on Windows cmd:

```
set FLASK_APP=app.py
```

Or on Windows Powershell:

```
$env:FLASK_APP = "app.py"
```


Then run the flask application:

```
flask run
```

##Check out application

Go to http://127.0.0.1:5000/ in a browser.

