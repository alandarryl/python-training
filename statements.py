
user_input = input(' what is the weather today')

weather_today = user_input.lower()

if weather_today == 'rainy':
    print("bring an umbrella")
elif weather_today == 'sunny':
    print("wear a hat")
elif weather_today == 'snowy':
    print("wear a coat")
elif weather_today == 'cloudy':
    print("wear a jacket")
else:
    print("i don't know what to wear today")
    



