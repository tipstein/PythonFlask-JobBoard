from flask import Flask
from flask import render_template

app = Flask(__name__)

def my_decorator(route):
    def jobs():
        return render_template( index.html )  
    route(jobs + "/")
