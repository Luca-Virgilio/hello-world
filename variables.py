
"""
non bisogna inserire il terminatore ;
non è necessario specificare il tipo delle variabili. esso viene associato dinamicamente
i tipi sono: int, String, bool ... é indifferente esprimere una stringa con apici singoli
o doppi
!!! Non si utilizzano le graffe e gli spazi/tab vengono interpretati
"""
# name = 'John'
# x = 3
# y = 5
# sum = x + y
# # l'operatore + funziona per concatenare solo le stringhe. se si vuole inserire un numero
# # bisogna castarlo a stringa

# print('Hello '+ name +'. I\'m '+str(sum))

# # altrimenti è possibile utilizzare print f con l'inserimento delle variabili
# print(f'Hello {name}. I\'m {sum}')
# print('Hello {name}. I\'m {sum}'.format(name=name, sum=sum))

# # Esistono diverse funzioni invocabili su una stringa:
# # len è la lunghezza di una stringa, lista ecc...
#  print(len(name))

# s ='hello everyone' 
# # funzione replace
# print(s.replace('everyone','world'))

# # dividi in una lista
# print(s.split())

# # count letter
# letter = 'e'
# print(s.count(letter))

# # trova la posizione del primo carattere
# print(s.find('e'))

# esistono diverse strutture in python. Liste, tuple, set, dictornary. 
# è possibie dichiararli invocando il loro costruttore oppure semplicemente utilizzando le 
# giuste parentesi. 

# num_list = [1,2,3,4,5]
# num2_list = list((1,2,3,4,5))

# # è possibile accedere ad un singolo elemento indicando la sua posizione. si parte da 0
# print(num_list[3])

# # append aggiunge un elemento
# num_list.append(6)
# # revers inverte l'ordine
# num_list.reverse()
# #sort ordina la lista
# num_list.sort()
# # conta il numero di occorrenze del numero 1 
# print(num_list.count(1))

# print(num_list)
# print(num2_list) 

# # una tupla è una struttura non modificabile
# # ogni elemento ha un indice
# color_tup = ('red', 'yellow', 'green', 'green')
# color2_tup = tuple(('red', 'yellow', 'green'))

# # trovare l'indice in cui compare il primo elemento
# print(color_tup.index('green'))
# # oppure utilizzare l'indice per accedere all'elemento
# print(color2_tup[0])
# # la funzione del cancella qualsiasi cosa
# del color2_tup

# print(color_tup)
# print(color2_tup)

# #!!! per indicare che una tupla contiene un solo elemento, bisogna inserire la virgola
# single = ('oneValue',)
# print(type(single))

# # un set è un insieme di elementi non ripetuti senza indici
# team = {'italy', 'france', 'spain' }
# team2 = set(('italy', 'france', 'spain')) 

# # aggiungere o rimuovere elementi
# team.add('germany')
# team.add('spain')
# team.remove('france')

# # si può cancellare tutti gli elementi
# team2.clear()

# print(team)
# print(team2)

# # dictonary è una struttura dati chiave valore.
# person = {
#     'first_name':'Duvan',
#     'last_name':'Zapata',
#     'goal':7
# }
# person2 = dict (first_name='Duvan', last_name='Zapata', goal=7)

# # utilizzando la chiave è possibile ottenere il valore
# print(person['goal'])
# print(person2['goal'])
# # oppure si può utilizzare la funzione get
# print(person.get('first_name'))

# # è possibile aggiungere chiavi/valori
# person['age'] = 26
# # copiare si usa la funzione copy, oppure un assegnamento
# person3 = person.copy()
# person3 ['nation']='Colombia'

# # rimuovere un attributo, oppure si usa la funzione del sull'attributo
# person.pop('goal')
# del(person['age'])

# print(person)
# print(person3)

# # List of dict
# people = [
#     {'name': 'Martha', 'age': 30},
#     {'name': 'Kevin', 'age': 25}
# ]

# print(people[1]['name'])

