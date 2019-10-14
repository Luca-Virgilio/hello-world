# moduli contengono un insieme di funzioni utilizzabili nella nostra applicazione
# è possibile importare solo le funzioni di un singolo oggetto
from datetime import date
# modulo intero
import time

# oppure è possibile istallare una librerie esterna: pip module
from camelcase import CamelCase

# importare un modulo/file scritto
from validator import validate_email

today = date.today()
timestamp = time.time()

c = CamelCase()

#print(c.hump("wa are the champions"))
email = 'test@test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Email is bad')
