from flask import Flask, render_template #imports the Flask class and the render_template function from the Flask library.

app = Flask(__name__) #here app is the instance of class Flask, and we have given argument as __name__
                      #__name__ is a special Python variable that holds the name of the current module
                      #this __name__ will be initialized to __main__
                      #which means its the main class

@app.route('/') # a route decorator that maps the URL '/' (the root URL) to the "home" function
def home():
    return render_template('index.html') # calls the render_template function, 
                                        # which looks for an index.html file in the templates directory of the project, 
                                        # renders it, and returns the rendered HTML to the client (the web browser). 
    

if __name__ == '__main__': # If this is the main app, the code inside the if block will execute.
    app.run(debug=True) # starts the Flask web server in debug mode