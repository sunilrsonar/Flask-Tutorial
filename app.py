from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Guys, Welcome my website!'

@app.route('/api/<name>')
def second(name):

    length = len(name)

    if length > 5:
        print('Name is too long')
    else:
        print('Name is too short')

#    print(name)
    return 'This is the second page!'

if __name__ == '__main__':
    app.run(debug=True)
