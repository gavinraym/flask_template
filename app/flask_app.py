from flask import Flask, request, render_template, Response
import jinja2

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    '''By using render_template, we can utilize html scripts
    instead of having to write all of our code here in python.
    This is very handy because VSCode will help us write our
    code in the html script.''' 
    
    # Note: you do not have to write the entire path. It will 
    # know to look in the [templates] folder for the file.
    return render_template('home.html')

@app.route("/project", methods=['GET','POST'])
def project():
    '''On this next page, I'm going to show you how to use 
    jinja to easily pass variables to your html script.'''

    # Here I'm brining in a list of heavy metal lyrics and
    # saving them to the variable [var].
    with open('app/data/hm_lyrics.csv', 'r') as f:
        var = [_.split(',') for _ in f.readlines()]

    # We can then pass the variable to our html template by
    # adding it to the render_template method.
    return render_template(
        'project.html',
        var1=var,
        #You can add as many variables as you like here!
        )

    # Note: var1=var -- The left side of = will determine the
    # variable name as we will use it in the html script. In 
    # this case, var1.

if __name__ == "__main__":
    # Don't forget to turn debug to False when launching
    app.run(host='0.0.0.0', port=8080, debug=True)