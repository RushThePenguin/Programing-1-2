def main():
  eggs = int(input("Enter the number of eggs purchased: "))
  dozens = eggs//12
  remainder = eggs % 12
  cost = 0.0
  price = 0.0
  
  if dozens > 0 and dozens < 4:
    price = .5
  if dozens >= 4 and dozens < 6:
    price = .45
  if dozens >= 6 and dozens < 11:
    price = .40
  if dozens >= 11:
    price = .35


  cost = dozens * price + (remainder * (1.0/12.0 * price))
  print("The bill is equal to " + str(cost))
      
  pass


if __name__== "__main__":
  main()