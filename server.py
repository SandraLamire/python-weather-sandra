from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

# homepage route
@app.route('/')
@app.route('/index')
def index():
    # for 1rst test
    # return "Hello World!"
    return render_template('index.html')
    
@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    # Check for empty string or sting with only spaces
    if not bool(city.strip()):
        city = "Rennes"
    
    weather_data = get_current_weather(city)
    
    # If city not found by API = {'cod': '404', 'message': 'city not found'}
    if not weather_data['cod'] == 200:
        # return "City not found" but best practice to have a template for that case
        return render_template('city-not-found.html')
    
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )    
 
# local run => open Chrome in localhost:8000  
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    # display : 
    #  * Serving Flask app 'server'
    #  * Debug mode: off
    # WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    #  * Running on all addresses (0.0.0.0)
    #  * Running on http://127.0.0.1:8000
    #  * Running on http://192.168.20.56:8000

    # switch to production mode with cmd :
    # pip install waitress
    serve(app, host="0.0.0.0", port=8000)




