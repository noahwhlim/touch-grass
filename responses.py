import requests

def get_weather(city) -> str:
    API_KEY = "API_KEY"
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_KEY}").json()

    feels_like = data["main"]["feels_like"]
    if (feels_like <= 40):
        return "Too cold"
    elif (feels_like > 40):
        return "Go touch some grass"
    else:
        return "Too hot"


def handle_responses(message) -> str:
    p_message = message.lower().split()
    query = ""
    if (p_message[0] == "!grass"):
        for i in range(1, len(p_message)):
            query += p_message[i] + " "
        return get_weather(p_message[1])

        # print(p_message)
        # return get_weather(p_message[1])
