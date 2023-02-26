from flask import Flask,request,jsonify
import util
app=Flask(__name__)

@app.route('/dummy',methods=['GET'])
def dummy():
    response=jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict',methods=['GET','POST'])
def predict():
    sl=float(request.form['sepal_length'])
    sw=float(request.form['sepal_width'])   
    pl=float(request.form['petal_length'])
    pw=float(request.form['petal_width'])
    print(sl,sw,pl,pw)
    response=jsonify({
        'prediction':util.estimation(sl,sw,pl,pw)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    util.load_saved_artifacts()
    app.debug=True
    app.run()