#Comillas simples
cads = 'Texto entre \ncomillas simples'
#Comillas dobles
cadd = "Texto entre \n\tcomillas dobles"
#Comillas triples
cadc = """ Texto linea 1
linea 2
linea 3
...
linea n
"""

#print type (cads) nos dira str string

print cads
print cadd
print cadc

#Repeticion y concatenacion de textos
cad = "Cadena" * 3 #repite 3 veces el texto
cad1 = "Cadena 1 "
cad2 = "Cadena 2 "

print cad + cad2


#booleano
bT = True
bF = False

bAnd = True and False #Ambos son verdadero return True
bOr = True or False #cualquiera es verdadero return True
bNot = not True

print bAnd
print bOr
print bNot
