# Opdrachten 1 tot en met 9 van paragraaf 3.4
bedrag = 100
if bedrag > 150:
	print(bedrag * 1.19)
else:
	print(bedrag * 1.16)
bedrag = 10
if bedrag > 150:
	print(bedrag * 1.19)
elif bedrag < 55:
	print(bedrag * 1.11)
else: 
	print(bedrag * 1.16)
bedrag = float(input("voer een bedrag in") )
if bedrag > 150:
	nieuwBedrag = bedrag * 1.19
	print(nieuwBedrag)
elif bedrag < 55:
	nieuwBedrag = bedrag * 1.11
	print(nieuwBedrag)
else: 
	nieuwBedrag = bedrag * 1.16
	print(nieuwBedrag)
