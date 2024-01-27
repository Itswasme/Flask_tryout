from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<p>Hello, ik heb les 11 afgerond en hierbij stuur ik u een screenshot </p>"

if __name__ == '__main__':   
    app.run(port=5000,debug=False)


