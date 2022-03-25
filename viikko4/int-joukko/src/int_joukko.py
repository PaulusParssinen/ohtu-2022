class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None, joukko=None):
        self.joukko = joukko or []
    
    def kuuluu(self, n): return n in self.joukko
    def mahtavuus(self): return len(self.joukko)
    def to_int_list(self): return list(self.joukko)
    
    def kopioi_taulukko(self, a, b): b = a[:]
    
    def lisaa(self, n):
        if n in self.joukko: 
            return False
        self.joukko.append(n)
        return True

    def poista(self, n):
        if n not in self.joukko: 
            return False
        self.joukko.remove(n)
        return True

    @staticmethod
    def yhdiste(a, b):
        return IntJoukko(joukko=(set(a.joukko) | set(b.joukko)))

    @staticmethod
    def leikkaus(a, b):
        return IntJoukko(joukko=(set(a.joukko) & set(b.joukko)))

    @staticmethod
    def erotus(a, b):
        return IntJoukko(joukko=(set(a.joukko) - set(b.joukko)))

    def __str__(self):
        return "{" + ", ".join(map(str, self.joukko)) + "}"
