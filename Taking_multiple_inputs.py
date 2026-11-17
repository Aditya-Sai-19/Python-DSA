#take single element as input
temp = int(input("what is the temperature today?\nAns: "))
print(f"Thanks! for the input \nToday's temperature is noted as {temp} degrees celcius")

#Taking Multiple values as input from the user 
Temps = list(map(int,input("what are the temperatures of yesterday,today and what will be tomorrow's respectively:").split()))
print(f"Noted! \nThe yesterday's temperature is {Temps[0]} degrees celcius\nToday's Temperature is {Temps[1]} degrees celcius\nTomorrow's expected temperature is {Temps[2]} degrees celcius")
