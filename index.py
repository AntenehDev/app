from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello, world'

@app.route('/<int:num>')
def mul(num):
    multiples=[]
    for i in range(1, 11):
        sum = num * i
        multiples.append(sum)
    return multiples
    
if __name__ == '__main__':
    app.run(debug=False)
