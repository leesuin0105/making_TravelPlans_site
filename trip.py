from flask import Flask, request, render_template, send_file
import openai
import os
import pandas as pd
import html

#api_key = os.environ["api_key"]
openai.api_key = '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'  #api_key

app = Flask(__name__)

dialogs = ""
messages = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    num_days = int(request.form['num_days'])
    place = request.form['place']

    plan = []

    messages = []
    messages.append({"role": "system", "content": "사용자에게 여행 일 수와 여행 장소를 입력받아 위도와 경도를 포함한 여행 계획을 html로 생성해줘"})
    messages.append({"role": "user", "content": f"여행 일 수: {num_days}"})
    messages.append({"role": "user", "content": f"여행 장소: {place}"})

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response = completion.choices[0].message['content']
    plan.append([f"Day {num_days}", response])
    messages.append({"role": "assistant", "content": response})

    return render_template('result.html', plan=plan)


if __name__ == '__main__':
    app.run(debug=True)





