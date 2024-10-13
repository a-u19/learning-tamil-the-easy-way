from flask import Flask, render_template, url_for, request

app = Flask(__name__)

#route to the index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/viewer')
def viewer():
    file = request.args.get('file')
    print(file)
    return render_template('viewer.html', file=file)

#open any template
@app.route('/<filename>')
def templateFilename(filename):
    return render_template(f'{filename}.html')

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)