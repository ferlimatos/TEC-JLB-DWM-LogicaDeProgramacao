temperatura = float(input("Informe uma temperatura: "))
escala = input("Para qual escala você deseja conventer? De Celsius para Fahrenheit ou de Fahrenheit para Celsius? ")

escala = escala.strip().lower()

if escala == "celsius para fahrenheit":
  fahrenheit = temperatura * 9/5 + 32
  print(f"A conversão da temperatura em {temperatura}Cº para fahrenheit é {round(fahrenheit, 2)}Fº.")
elif escala == "fahrenheit para celsius":
  celsius = (temperatura-32)*5/9
  print(f"A conversão da temperatura em {temperatura}Fº para celsius é {round(celsius, 2)}Cº.")
else:
  print("Essa conversão não está disponível.")