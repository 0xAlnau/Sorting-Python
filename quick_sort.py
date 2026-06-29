import random

class quick_sort():
    def __init__(self, llista):
        self.ll = llista


    #implementacio de quick sort
    def sort(self):
        llista = self.ll
        n = len(llista)
        res = []

        if n <= 1:          #cas base
            res = llista
        else:
            random.shuffle(llista)   # per assegurar un temps O(n*log(n)) fem permutació
            pivot = llista[0]
            menors_ig = []
            majors = []

            for i in range(1,n):
                if llista[i] <= pivot:
                    menors_ig.append(llista[i])
                else:
                    majors.append(llista[i])

            self.ll = menors_ig
            menors_ig = self.sort()

            self.ll = majors
            majors = self.sort()

            res = menors_ig + [pivot] + majors

        return res
