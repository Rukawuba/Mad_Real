from flask import Flask, request, jsonify, redirect
import util

util.load_saved_artifacts()


app = Flask(__name__)

@app.route("/")
def redirect_to_prediction():
  return redirect(url_for('predict_home_price'))


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqm = float(request.form['total_sqm'])
    location = request.form['location']
    room = int(request.form['room'])
    bath = int(request.form['bath'])


    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqm,room,bath)
    })


    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


if __name__ == "__main__":
    print('Starting Python Flask Server For Madrid..')
    app.run()