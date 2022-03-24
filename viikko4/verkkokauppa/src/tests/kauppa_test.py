import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 42:
                return 20
            elif tuote_id == 1337:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 42:
                return Tuote(42, "kahvi", 4)
            elif tuote_id == 1337:
                return Tuote(1337, "tee", 20)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        self.kauppa.aloita_asiointi()
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 5)
    
    def test_kahdet_eri_ostokset_oikea_tilisiirto(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(42)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 9)

    def test_kahdet_samat_ostokset_oikea_tilisiirto(self):
        self.kauppa.lisaa_koriin(42)
        self.kauppa.lisaa_koriin(42)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 8)

    def test_lisaa_kahdet_ostokset_joista_toinen_on_loppu(self):
        self.kauppa.lisaa_koriin(42)
        self.kauppa.lisaa_koriin(1337)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 4)
        
    def test_aloita_asiointi_nollaa_ostokset(self):
        self.kauppa.lisaa_koriin(42)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", "33333-44455", 5)
    
    def test_kaytetaan_perakkaisia_viitteita(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]
        
        self.kauppa.lisaa_koriin(42)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 1, ANY, ANY, ANY)
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 2, ANY, ANY, ANY)
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with(ANY, 3, ANY, ANY, ANY)
    