from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
result = pickle.load(open('hello2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello',methods=['POST'])
def hello():
    '''
    For rendering results on HTML GUI
    '''
  #  name = [str(x) for x in request.form.values()]


    #return render_template('index.html', hello_text='my name is {},{}'.format(result,name))
    return render_template('index.html', hello_text='Hello!! my name is {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)
