# app.py
from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/process', methods=['POST'])
def process():
    # Get input from the form
    input_data = request.form.get('input_data')

    # Save input data to a file
    input_file_path = 'input.txt'
    with open(input_file_path, 'w') as file:
        file.write(input_data)

    # Run Voila to execute the Jupyter Notebook
    subprocess.run(['voila', 'D:\pcl project\flask\preprocess_data.ipynb', '--port=0'])

    # Read the output from the notebook
    output_file_path = os.path.join('templates', 'D:\pcl project\flask\templates\output.html')
    with open(output_file_path, 'r') as file:
        output_html = file.read()

    return render_template('result.html', output_html=output_html)

if __name__ == '__main__':
    app.run(debug=True)

