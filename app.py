lfrom flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
hello = pickle.load(open('hello.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello',methods=['POST'])
def hello():
    '''
    For rendering results on HTML GUI
    '''
    name = [str(x) for x in request.form.values()]
    ans=hello.answer(name)



    return render_template('index.html', hello_text=.format(ans))


if __name__ == "__main__":
    app.run(debug=True)
