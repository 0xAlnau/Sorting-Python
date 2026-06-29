class bucket_sort():
    def __init__(self, llista):
        self.ll = llista


    #implementació de bucket sort (només enters amb valors entre [0, m-1])
    def sort(self):
        llista = self.ll
        res = []

        if llista == []: #ens donen llista buida
            res = []
        elif min(llista) < 0: #hi ha valor negatiu
            raise ValueError("Només s'accepten valors en el rang [0,m-1]")
        else: #sort normal
            n = len(llista)
            m = max(llista)
            buckets = [0 for _ in range(m+1)]

            for i in range(n):
                j = llista[i]
                buckets[j] += 1

            res = []
            for i in range(m+1):
                repeticions = buckets[i]
                for j in range(repeticions):
                    res.append(i)

        return res
