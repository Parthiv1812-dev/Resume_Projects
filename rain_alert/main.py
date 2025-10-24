import requests
import os
from twilio.rest import Client

api_key = "ffd1747af645c210717766d2254d2400"
#
# lat = 33.4148
# lon = -111.9093

account_sid = 'AC8d5022eaadaecdeeb20c1c80df4e44a4'
auth_token = 'aaff9627b1e7a0fd909c3f13f780a229'

lat = 51.759048
lon = 19.458599

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()
# id = data["list"][0]["weather"][0]["id"]
id_list = []
i = 0
will_rain = False
for i in range(4):
    id_list.append(data["list"][i]["weather"][0]["id"])
    id = data["list"][i]["weather"][0]["id"]
    i += 1
    if int(id) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain, do not forget to bring an umbrella☂️",
        to="whatsapp:+16026481884",
    )
    print(message.status)



# print(id_list)