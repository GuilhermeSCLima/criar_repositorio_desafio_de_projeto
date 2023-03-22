stayAsking = True

while stayAsking:
  number = int(input("Digite um numero: "))
  
  isDivisibleBy3 = True if number % 3 == 0 else False
  isDivisibleBy5 = True if (number % 5) == 0 else False

  if isDivisibleBy3 and isDivisibleBy5:
    print("foobar")
  elif isDivisibleBy3:
    print("foo")
  elif isDivisibleBy5:
    print("bar")
  else:
    print("baz")

  stayQuestion = input("Deseja continuar?? (s/n) ")
  
  stayAsking = True if (stayQuestion == "s" or stayQuestion == "S") else False

print("Obrigado por utilizar meu simples programa. S2 <3")