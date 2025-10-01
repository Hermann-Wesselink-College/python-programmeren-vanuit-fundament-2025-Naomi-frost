# Opdracht 1 tot en met 7 van pragraaf 2.10
from datetime import datetime
datumtijd = datetime.now()
month = datumtijd.month
print(str(month) )
from datetime import datetime
datumtijd = datetime.now()
day = datumtijd.day
print(str(day) )
from datetime import datetime
datumtijd = datetime.now()
year = datumtijd.year
print(str(year) )
from datetime import datetime
datum = datetime.now()
dag = datum.day
maand = datum.month
jaar = datum.year
print(str(dag) + "-" + str (maand) + "-" + str (year) )
from datetime import datetime
datum = datetime.now()
dag = datum.day
maand = datum.month
jaar = datum.year
minuut = datumtijd.minute
uur = datumtijd.hour
datum = str(dag) + "-" + str (maand) + "-" + str (jaar) 
tijd = str(uur) + "-" + str (minuut)
print("de datum van vandaag is " + datum + " . het is nu  " + tijd + " . ") 