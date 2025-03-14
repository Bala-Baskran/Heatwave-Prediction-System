from flask import Flask, request, jsonify, send_file
from config import SECRET_KEY, WEATHER_API_KEY, MAIL_USERNAME, MAIL_PASSWORD
import requests
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Configure Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = MAIL_USERNAME
app.config["MAIL_PASSWORD"] = MAIL_PASSWORD
app.config["MAIL_DEFAULT_SENDER"] = MAIL_USERNAME

mail = Mail(app)

# OpenWeather API URL (Example)
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    return send_file("index.html")  # Serve index.html from the same directory

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.form["city"]
    api_url = f"{WEATHER_API_URL}?q={city}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(api_url)
    weather_data = response.json()

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        alert = "⚠️ Heatwave Alert!" if temperature > 35 else "🌤️ Normal Weather"

        return jsonify({
            "temperature": temperature,
            "description": description,
            "alert": alert
        })
    else:
        return jsonify({"error": "City not found"}), 404

@app.route("/send_alert", methods=["POST"])
def send_alert():
    email = request.form["email"]
    city = request.form["city"]
    temperature = request.form["temperature"]
    alert = request.form["alert"]

    try:
        msg = Message("🌡️ Heat Wave Alert!", recipients=[email])
        msg.body = f"Heatwave Alert for {city}!\nTemperature: {temperature}°C\n{alert}"
        mail.send(msg)
        return jsonify({"message": "Alert email sent successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
