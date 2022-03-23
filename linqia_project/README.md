# Instruction

This repo has been updated to work with `Python v3.8` and up.

### How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip3 install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python main.py
```

This server will start on port 5000 by default. You can change this in `main.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```

### Demo

This demo simply shows how the program works.

https://user-images.githubusercontent.com/71042259/159678749-d8ce4418-cc95-43be-bf01-13896184b91f.mp4


