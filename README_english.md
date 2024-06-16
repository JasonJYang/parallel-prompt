# Parallel prompt of GPT
Hi, we have built a web page application which can be used for parallel prompt processing using GPT api.   
中文说明点击：[README](https://github.com/DorisWangDR/parallel-prompt/blob/main/README.md)

## 1 instruction
1) Open a command line and create a new environment:  
`conda create -n chatgpt_env python=3.11`
2) Navigate to this folder:  
`cd C:\<文件夹路径>`
3) In this folder run:  
`pip install -r requirements.txt`

## 2 Use the webpage
1) Continue running:  
   `python app.py`
2) Find the web link in the text displayed by the command line:  
   `* Running on http://127.0.0.1:5000`
   Copy the link to open in the browser.
   Enter the Base URL, KEY of your API and prompt.
   Select the model name.
   Upload the file.
   Click RUN to run, the running time may vary from a few minutes to a few hours, the time depends on the amount of data.
   After running, the download button will appear, download the output.
