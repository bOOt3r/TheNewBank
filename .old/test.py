
from classes.customer import Customer as c 

customers = []

with open('./dataBase/customer_database.txt') as dbrd:

  for x in dbrd:
    y = x.strip().split(':')

  print(y)

 # for x in y:
 #   customers.append(c(x[0], x[1], x[2]))
