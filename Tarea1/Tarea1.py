conjunto_A={1,2,3,4,5,6}
conjunto_B={4,5,6,7,8,9}

print(f"Conjunto_A: {conjunto_A}")
print(f"Conjunto_B: {conjunto_B}")

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos
print(f"Los elementos que se encuentran en en A o en B, o en ambos son: {conjunto_A|conjunto_B}")

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B

print(f"Los elementos que se encuentran en ambos conguntos A y B son: {conjunto_A&conjunto_B}")

#Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

print(f"Los elementos que se encuentran en A o en B, pero no en ambos son: {conjunto_A-conjunto_B}")

#Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.

print(f"El conjunto A es subconjunto de B: {conjunto_A.issubset(conjunto_B)}")

#Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto

print(f"El conjunto A posee {len(conjunto_A)} elementos")