import os
import io
import logging
import asyncio
import pandas as pd
from api_request_parallel_processor import process_api_requests_from_file
from generate_requests import generate_chat_completion_requests
from save_generated_data_to_csv import save_generated_data_to_csv
from flask import Flask, render_template, request, send_from_directory, Response

app = Flask(__name__)
# Global variable to store logs
logs = []
class StreamToLogger(object):
    def write(self, message):
        # Write the message to the application logger
        if "werkzeug" in message:
            return
        logs.append(message)
    def flush(self):
        pass

UPLOAD_FOLDER = 'uploads'
GENERATED_FOLDER = 'generated'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(GENERATED_FOLDER):
    os.makedirs(GENERATED_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        base_url = request.form['base_url']
        api_key = request.form['api_key']
        prompt_settings = request.form['prompt_settings']
        model_name = request.form['model_name']
        file = request.files['file']
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        # Save the output to a file in GENERATED_FOLDER
        generated_filename = 'output.csv'

        # Process the input data and generate the output
        run_prompt(file, prompt_settings, base_url, api_key, 
                   model_name=model_name, save_dir=os.path.join(GENERATED_FOLDER, generated_filename))
        
        return render_template('index.html', generated_filename=generated_filename)

    return render_template('index.html', output='', generated_filename=None)

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=app.config['GENERATED_FOLDER'], path=filename, as_attachment=True)

@app.route('/logs', methods=['GET'])
def get_logs():
    # Join the logs into a single string and return it
    return Response('\n'.join(logs), mimetype='text/plain')

def run_prompt(file, prompt, base_url, api_key, model_name="gpt-3.5-turbo", save_dir="generated"):
    log_stream = StreamToLogger()
    # Configure the logging module to write to the stream
    logging.basicConfig(stream=log_stream, level=logging.INFO)

    data_df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    data = list(data_df[data_df.columns[0]])
    # data = data[:10] limit data for testing

    requests_filepath = "example_requests_to_chat_completion.jsonl"
    requests_output_filepath = "example_requests_to_chat_completion_results.jsonl"
    if os.path.exists(requests_output_filepath):
        os.remove(requests_output_filepath)

    generate_chat_completion_requests(requests_filepath, data, prompt, model_name=model_name)
    # Process multiple api requests to ChatGPT
    asyncio.run(
        process_api_requests_from_file(
            requests_filepath=requests_filepath,
            save_filepath=requests_output_filepath,
            request_url=base_url,
            api_key=api_key,
            max_requests_per_minute=float(90000),
            max_tokens_per_minute=float(170000),
            token_encoding_name="cl100k_base",
            max_attempts=int(5),
            logging_level=int(20),
        )
    )
    # save
    save_generated_data_to_csv(requests_output_filepath, save_dir)

if __name__ == '__main__':
    app.run(debug=True)