from flask import Flask, render_template
from PIL import Image
app = Flask(__name__)

@app.route('/')
def index():
    test = "=" * 9000
    return render_template('index.html', test=test)

@app.route('/fizzbuzz')
def fizzbuzz():
    return 'Fizzbuzz'

@app.route('/ErikPasswordGen')
def erikPassGen():    
    import string
    # Import secret module which allows you to generate strong passwords
    import secrets

    #-----------------------------------------------------
    # press control + d to highlight all same variables
    # to tab multiple lines, highlight desired lines and press Tab
    #-----------------------------------------------------

    # password is set as a string
    password = ' '

    # loop 8 times
    for i in range(0, 8):
    # generate both lowercase and uppercase strings from the secrets library
        password += secrets.choice(string.ascii_lowercase)
        password += secrets.choice(string.ascii_uppercase)
    # print password
    return password

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)