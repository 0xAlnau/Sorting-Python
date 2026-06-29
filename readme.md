# Sorting a Python
Aquest petit projecte ha sigut creat amb l'única intenció de reviure conceptes vists anteriorment i de posar en pràctica algorismes explicats a classe.

## Algorismes
Els algorismes d'ordenació implementats han sigut els següents:

- Bucket Sort: té la capacitat d'ordenar en temps O(n), però, cal que la llista a ordenar siguin enters en un rang entre [0, m], on m és el valor màxim de la llista. Fa falta aquesta propietat ja que d'aquesta forma podem tindre m+1 'buckets' on poder anar posant cada element directament. 

- Insertion Sort: és el més senzill de tots però té un cost de O(n²). Aquest es basa en el fet de posar cada element allà on hauria d'estar en la llista ja ordenada. Això es pot fer subdividint la llista en dos trossos, un ja ordenat i l'altre no. El que es va fent és anant agafant elements de la llista no ordenada i col·locar-los en la llista ordenada, posant-los on toca per seguir deixant la llista ordenada.

- Merge Sort: aquest és un algorisme recursiu amb cost O(n*log(n)), on la idea principal es basa en dividir la llista en dos trossos de la mateixa mida, ordenar-los amb el mateix Merge Sort, i llavors juntar les dues llistes ordenades (merge). La gràcia està en que hi ha un cas base on la llista donada ja està ordenada, quan la seva mida és <= 1. 

- Quick Sort: també és recursiu i té un cost de O(n*log(n)), i en aquest el que es fa és agafar un `pivot`, el qual és la referència per crear dues noves llistes, una pels elements menors o iguals al pivot, i una altra per a element majors al pivot. Una vegada tenim les dues llistes el que fem és ordenar les dues llistes amb el mateix Quick Sort, i llavor al final ajuntem `menors + pivot + majors`. Això funciona ja que el cas base és el mateix que a l'anterior, es a dir, quan la mida de la llista és <= 1. Per a garantir el cost vist abans cal que fer una permutació aleatòria de la llista, ja que sinó, si agafem un pivot dolent (un element que a la llista ordenada estigués en un extrem) llavors el cost en cas pijtor seria de O(n²).

## Execució
Per a provar els algorismes només cal fer: `python3 Main.py`

Si es vol provar amb algun input ja prefet només cal fer: `python3 Main.py < Inputs/arxiu.txt`
