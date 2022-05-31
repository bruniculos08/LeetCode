# your code goes here
n = int(input())
if(n%2 == 0):
	print("Par")
else:
	print("Impar")

# your code goes here
vogais = ['a', 'e', 'i', 'o', 'u']
string = str(input())
newString = ""
for letter in string:
    if letter in vogais:
        newString += letter.upper()
    else:
        newString += letter
print(newString)

# your code goes here
n = int(input())

for i in range(n):
	hexNumber = str(input())
	result = 0
	for j in range(len(hexNumber)):
		if(hexNumber[j] == 'A'):
			result = result + 10*pow(16, len(hexNumber)-j-1)
		elif(hexNumber[j] == 'B'):
			result = result + 11*pow(16, len(hexNumber)-j-1)
		elif(hexNumber[j] == 'C'):
			result = result + 12*pow(16, len(hexNumber)-j-1)
		elif(hexNumber[j] == 'D'):
			result = result + 13*pow(16, len(hexNumber)-j-1)
		elif(hexNumber[j] == 'E'):
			result = result + 14*pow(16, len(hexNumber)-j-1)
		elif(hexNumber[j] == 'F'):
			result = result + 15*pow(16, len(hexNumber)-j-1)
		else:
			result = result + int(hexNumber[j])*pow(16, len(hexNumber)-j-1)
	print(result)