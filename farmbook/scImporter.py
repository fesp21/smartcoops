from farmbook.models import Coop

file = open('coops.txt')

for line in file:
  columns = line.split(',')
  coop = Coop()
  coop.coopId = int(columns[0])
  coop.save()

file.close()
