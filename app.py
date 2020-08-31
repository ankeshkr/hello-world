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
    int_features = [str(x) for x in request.form.values()]
    ans=answer(x)



    return render_template('index.html', hello_text=.format(ans))


if __name__ == "__main__":
    app.run(debug=True)
