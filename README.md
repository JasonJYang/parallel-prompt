# Parallel prompt of GPT
我们建立了一个网页实现并行运行ChatGPT Prompt，解决使用ChatGPT api运行代码慢的问题。  
Hi, we have built a web page application which can be used for parallel prompt processing using GPT api.  
The English instruction click here: [README_english](https://github.com/DorisWangDR/parallel-prompt/blob/main/README_english.md)

## 中文使用说明
### 1 安装 
1) 下载压缩包到一个文件夹，解压缩。打开Anaconda prompt命令行，创建一个新的环境：  
`conda create -n chatgpt_env python=3.11`
2) 激活环境：  
`conda activate chatgpt_env`
3) 定位到该文件夹：  
`cd C:\<该文件夹路径>`
4) 在这个文件夹下运行：  
`pip install -r requirements.txt`

### 2 运行 
1) 继续在文件夹下运行：  
`python app.py`
2) 在命令行显示的文本中找到网页链接：  
`* Running on http://127.0.0.1:5000`  
   复制链接到浏览器打开，如下图所示。 输入你的api的Base URL和KEY，Prompt，选择模型名称，上传文件，点击RUN运行，运行时间可能从几分钟到几小时不等，时间取决于数据量大小，运行完之后，下载按钮会出现，一键下载。
<center><img src="https://github.com/DorisWangDR/parallel-prompt/blob/main/website_example.png" alt="website_screenshot" width="50%"/></center>
