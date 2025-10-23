import requests
from datetime import datetime
import smtplib

MY_LAT = 33.425522 # Your latitude
MY_LONG = -111.941254 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if 28 < iss_latitude < 38 and -116 < iss_longitude < -106 and sunset <= time_now.hour <= sunrise:
    my_email = 'pythonsmtp8@gmail.com'
    password = 'wzoh tbqz ttnv ahff'
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    # tls stands for transport layer security, it is a way of securing our connection to the email server
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email,
                        msg="Subject: ISS ABOVE YOUR HEAD\n\nLool up! ISS is above your head")
    connection.close()



