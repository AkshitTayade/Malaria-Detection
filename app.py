import os
from flask import render_template, Flask, request, url_for, redirect, flash, send_from_directory
from predictions import result

app = Flask(__name__, template_folder='templates')
app.secret_key = 'akshittayade'
app.set("port", 8080)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return(render_template('1st.html'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    
    target = os.path.join(APP_ROOT, 'static/')

    if not os.path.isdir(target):
        os.mkdir(target)

    if request.method == 'POST':
        f = request.files['file_loc']

        img_name = str(f.filename)

        if f is None:
            return(redirect(request.url))
    
        else:
            path = [target, f.filename]
            dst = "/".join(path)
            #print(dst)
            f.save(dst)

    img_path = dst
    #print(img_path)

    predicted_value = result(img_path)
    #print(output)

    if predicted_value == 'Parasitized':
        output = 'Patient is detected with Malaria'
        color = 'red'

    else:
        output = 'Patient is normal'
        color = 'green'



    return(render_template('1st.html', img_name = img_name, output = output, color=color))

@app.route('/sampleimages', methods=['GET', 'POST'])
def download():
    #Sample_Images.zip
    return(send_from_directory(os.getcwd(), filename='Sample_Images.zip'))


if __name__ == "__main__":
    app.run(debug=True)


