from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_heartdisease():
    x1 = int(request.form.get('title'))
    x2 = int(request.form.get('director'))
    x3 = int(request.form.get('country'))
    x4 = int(request.form.get('rating'))
    x5 = int(request.form.get('duration'))
    x6 = int(request.form.get('listed_in'))

    # prediction
    result = model.predict(np.array([x1,x2,x3,x4,x5,x6]).reshape(1,6))
    fin_result = float(round(result[0],2))
    
    if fin_result==0:
        fin_result='Movie'
    else:
        fin_result='TV Show'

    return render_template('index.html',fin_result=fin_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

app.static_folder = 'static'
