numbers = []

for element in range(1,11):
    numbers.append(element)

print(numbers)

numbers2 = [element*2 for element in range(1,11)]
print(numbers2)

numbersIf = [i for i in range(1,11) if i%2==0]

print(numbersIf)