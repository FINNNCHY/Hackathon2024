from flask import Flask, render_template, request, jsonify
import constants
import os
os.environ['AZURE_OPENAI_API_KEY'] = constants.API_KEY
os.environ['AZURE_OPENAI_ENDPOINT'] = constants.AZURE_OPENAI_ENDPOINT
os.environ['OPENAI_API_VERSION'] = constants.OPENAI_API_VERSION

import openai

client = openai.AzureOpenAI()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def get_bot_response():
    user_input = request.form['msg']
    response = {"response": str(real_request(user_input))}
    return jsonify(response)

def real_request(msg):
    msgs= [
        
        {
            "role":"user",
            "content": "Use this document as a reference https://docs.direct.worldline-solutions.com/en/api-reference, do not explain your answers just return the answer"
        },
        {
            "role":"user",
            "content": "Any response you give, return it in html format with the root element as a div with inline css, the response will be rendered on a website"
        },
        {
            "role":"user",
            "content": msg
        }
    ]
    response = client.chat.completions.create(model='gpt-4-vision', messages=msgs, max_tokens=4096)
    return response.choices[0].message.content

if __name__ == "__main__":
    app.run(port=8888)
