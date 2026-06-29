class merge_sort():
    def __init__(self, llista):
        self.ll = llista


    #retorna la primera meitat de la llista de la classe
    def first_half(self):
        llista = self.ll
        res = []
        n = len(llista)
        i = 0

        while i < n // 2:
            res.append(llista[i])
            i += 1

        return res


    #retorna la segona meitat de la llista de la classe
    def second_half(self):
        llista = self.ll
        res = []
        n = len(llista)
        i = n // 2

        while i < n:
            res.append(llista[i])
            i += 1

        return res


    #donades dues llistes ja ordenades les junta i retorna una altra llista ordenada
    def merge(self, ll1, ll2):
        p = len(ll1)
        q = len(ll2)
        n = p + q
        res = [0 for _ in range(n)]
        a = 0 #index per ll1
        b = 0 #index per ll2

        for i in range(n):
            if a == p: #ll1 ja ficada
                res[i] = ll2[b]
                b += 1

            elif b == q: #ll2 ja ficada
                res[i] = ll1[a]
                a += 1

            elif ll1[a] <= ll2[b]:
                res[i] = ll1[a]
                a += 1
            else:
                res[i] = ll2[b]
                b += 1

        return res

    #implementació de merge sort
    def sort(self):
        n = len(self.ll)

        if n <= 1:          # cas base, ja està ordenada
            return self.ll
        else:               # cas recursiu
            fst_h = self.first_half()
            snd_h = self.second_half()

            self.ll = fst_h
            ll1 = self.sort()

            self.ll = snd_h
            ll2 = self.sort()

            self.ll = self.merge(ll1, ll2)

            return self.ll
