from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('hello.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello',methods=['POST'])
def hello():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    answer(x)



    return render_template('index.html', prediction_text=.format(answer))


if __name__ == "__main__":
    app.run(debug=True)
