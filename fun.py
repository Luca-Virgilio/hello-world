# per definire una funzione si utilizza la parola def, input tra parentesi e :
def sumN (x,y=0):
    return x + y


# lambda function
moltiplicazione = lambda n1,n2: n1*n2

# print(sumN(10,5))
# print(sumN(2))
# print(moltiplicazione(6,7))

x = 10
y = 7

if x > y:
    print(sumN(x,y))
else:
    print(moltiplicazione(x,y))

num = [1,2,3,4,5]

# is o is not
if y in num:
    print('yes, there is')
else:
    print('no')

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
  print(f'Current Person: {person}')

# Break
for person in people:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# Continue
for person in people:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# range
for i in range(len(people)):
  print(people[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1
