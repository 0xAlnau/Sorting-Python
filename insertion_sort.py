class insertion_sort():
    def __init__(self, llista):
        self.ll = llista


    #avança una posició cada element desde i fins a j
    def advance_one_position(self, i, j):
        ant = self.ll[i]
        while i != j:
            aux = self.ll[i+1] #guardar valor següent
            self.ll[i+1] = ant
            ant = aux
            i = i + 1


    #retorna la llista ordenada rebuda al init
    def sort(self):
        n = len(self.ll)
        #movem els elements que facin falta de 0 fins a i-1 per a posar nou element
        for i in range(1, n):
            e = self.ll[i]
            j = 0
            posat = False
            while not posat and j < i:
                if self.ll[j] > e:
                    self.advance_one_position(j, i)
                    self.ll[j] = e
                    posat = True
                j = j + 1

        return self.ll

