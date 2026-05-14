from flask import Flask   #import the Flask class from the flask package

app=Flask(__name__)   #here app is the instance of class Flask, and we have given argument as __name__
                      #__name__ is a special Python variable that holds the name of the current module
                      #this __name__ will be initialized to __main__
                      #which means its the main class

@app.route('/') #a route decorator that maps the URL '/' (the root URL) to the "hello" function
def hello():
    return "Hello World! This is my first flask application!!" # return the text

if __name__=='__main__': # If this is the main app, the code inside the if block will execute.
    app.run(debug=True) # starts the Flask web server in debug mode