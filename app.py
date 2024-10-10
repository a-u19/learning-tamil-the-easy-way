from flask import Flask, render_template,request,redirect,flash,make_response,session

app = Flask(__name__)

#route to the index
@app.route('/')
def index():
    return render_template('index.html')


#open any template
@app.route('/<filename>')
def templateFilename(filename):
    return render_template(f'{filename}.html')

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)