from bucket_sort import *
from insertion_sort import *
from merge_sort import *
from quick_sort import *

class Sorting():
    def __init__(self, llista):
        self.ll = llista

    def bucket_sort(self):
        llista = self.ll
        bucket = bucket_sort(llista)
        return bucket.sort()

    def insertion_sort(self):
        llista = self.ll
        insertion = insertion_sort(llista)
        return insertion.sort()

    def merge_sort(self):
        llista = self.ll
        merge = merge_sort(llista)
        return merge.sort()

    def quick_sort(self):
        llista = self.ll
        quick = quick_sort(llista)
        return quick.sort()
