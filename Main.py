from Sorting import *

print("Introdueix una seqüència de valors a ordenar, tots han de ser del mateix tipus de dades. Per acabar posa un '!':\n")
tipus = input("Indica si vols utilitzar 'Int', 'Float' o 'String': ")
print()
llista = []
valor = ""

while valor != "!":
    valor = input("Valor: ")
    if valor != "!" and valor != "":
        if tipus == 'Int':
            try:
                llista.append(int(valor))
            except ValueError:
                print("Error: introdueixi un enter si us plau.")
        elif tipus == 'Float':
            try:
                llista.append(float(valor))
            except ValueError:
                print("Error: introdueixi un float si us plau.")
        else:
            try:
                llista.append(str(valor))
            except ValueError:
                print("Error: introdueixi un string si us plau.")


print(f"La llista és: {llista}")

print()
print("Ara escull quin mètode d'ordenació vols utilitzar:")
print(" 1 - Bucket Sort (O(n))")
print(" 2 - Insertion Sort (O(n²))")
print(" 3 - Merge Sort (n*log(n))")
print(" 4 - Quick Sort (n*log(n))")
print()

opcio = input("Opció: ")
resultat = []
s = Sorting(llista)

if opcio == "1":
    print("a")

elif opcio == "2":
    resultat = s.insertion_sort()

elif opcio == "3":
    resultat = s.merge_sort()

else:
    print("d")

print()
print(f"La llista ordenada és: {resultat}")
