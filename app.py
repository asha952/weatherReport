from flask import Flask, render_template, request, app
import requests


@app.route('/weather')
def weather():
    return render_template('weather_form.html')


@app.route('/weather_results')
def weather_results_page():
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    users_city = request.args.get('city')
    params = {
        'q': users_city,
        'appid': 'a6e42a57571246296ace899c0fc83ba7'
    }
    response = requests.get(weather_url, params=params)
    response_json = response.json()
    city = response_json['name']
    temp = response_json['main']['temp']

    return render_template('weather_results.html', city=city, temp=temp)


if __name__ == '__main__':
    app.run()