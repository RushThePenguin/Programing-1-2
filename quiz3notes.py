text = input("Enter Text: ")
for index in range(len(text)):
  print(text[index], end=" ")
print()
for letter in text: # for-each loop
  print(letter)

def main():
  text = "cool beans"
  print("In main: " + text)

main()
print("After main: " + text)