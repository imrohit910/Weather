import weatherapi
city=input("Enter Your City Name: ")
Result=weatherapi.weather({"city":city})
# iterate in result dictionary
print("weather report")
for key,value in Result.items():
    print(key,value)
