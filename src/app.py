from flask import Flask, request, render_template, redirect, url_for

from .functions import getWeatherData, extractWeatherData, splitWeatherData, extractWeatherTime, splitWeatherTime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.values['city']
        return redirect(url_for('weather', city = city))
    
    return render_template('index.html')

@app.route('/<city>', methods=['GET', 'POST'])
def weather(city):
    if request.method == 'POST':
        city = request.values['city']
        return redirect(url_for('weather', city = city))

    all = getWeatherData(city)

    weatherData = extractWeatherData(all)
    weatherData = splitWeatherData(weatherData)

    weatherTime = extractWeatherTime(all)
    weatherTime = splitWeatherTime(weatherTime)

    return render_template('weather.html', data = weatherData, time = weatherTime, location = city)

if __name__ == '__main__':
    app.run()