from flask import Flask
import random

blog1 = "Привет! Это мой блог о моих успехах в программировании. <br>Моя очередная библиотека - это Flask. Она, собственно, и помогла написать мне этот блог. <br> На днях я изучил tkinter и написал Сапёра. Ушло у меня на это.. часов 5."

app = Flask(__name__)

@app.route("/")
def facts():
    return blog1

app.run(debug=True)
