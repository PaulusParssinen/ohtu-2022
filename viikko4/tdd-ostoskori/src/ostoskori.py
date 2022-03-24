from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.ostokset())

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.ostokset())

    def lisaa_tuote(self, lisattava: Tuote):
        nimi = lisattava.nimi()
        ostos = self._ostokset.get(nimi)
        if not ostos:
            self._ostokset[nimi] = Ostos(lisattava)
        else:
            ostos.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        nimi = poistettava.nimi()
        ostos = self._ostokset.get(nimi)
        if not ostos: return
        
        ostos.muuta_lukumaaraa(-1)
        if ostos.lukumaara() < 1:
            del self._ostokset[nimi]

    def tyhjenna(self):
        self._ostokset = {}

    def ostokset(self):
        return list(self._ostokset.values())