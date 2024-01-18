#https://forum.boltiot.com/t/how-to-get-from-input-value-to-python-and-form-in-python/7781/3
#https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['text']
    return variable

"""
@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
        pay = request.form['pay']
        print ("Pay is " + pay)
        return "Data sent. Please check your program log"
"""
if __name__ == '__main__':
    app.run(debug=True, port=5001)