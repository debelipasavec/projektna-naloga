from datetime import date
import json

class Oseba:
    def __init__(self, kdo):
        self.kdo = kdo
        
    def spremeni_ime(self, novo_ime):
        self.kdo = novo_ime
    
    def v_slovar(self):
        return {
            "ime": self.kdo,
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Oseba(
            slovar["ime"],
        )
slovar = {'ime':'Nina'}
Oseba.iz_slovarja(slovar)
Oseba.kdo

class Skupina:
    def __init__(self, ime, vsi_ljudje = [], vsi_stroski = {}, znesek = 0):
        self.ime = ime
        self.vsi_ljudje = vsi_ljudje
        self.vsi_stroski = vsi_stroski
        self.znesek = znesek
        
    def dodaj_cloveka(self, kdo):
        if kdo in self.vsi_ljudje:
            print('Uporabnik že obstaja.')
        else:
            self.vsi_ljudje.append(kdo)
        
    def odstrani_cloveka(self, kdo):
        if kdo not in self.vsi_ljudje:
            print('Uporabnik ne obstaja.')
        else:
            self.vsi_ljudje.remove(kdo)
    
    def dodaj_strosek(self, kdo, cena, kaj):
        strosek = (date.today(), cena, kaj)
        self.znesek += cena
        if kdo not in self.vsi_stroski:
            self.vsi_stroski[kdo] = [strosek]
        else:
            if strosek in self.vsi_stroski.get(kdo):
                print('Strošek že obstaja.')
            else:
                self.vsi_stroski[kdo].append(strosek)
        
    def odstrani_strosek(self, kdo, cena, kaj):
        strosek = (date.today().isoformat(), cena, kaj)
        self.znesek -= cena
        if strosek not in self.vsi_stroski.get(kdo):
            print('Strošek ne obstaja.')
        else:
            self.vsi_stroski[kdo].remove(strosek)
    
    def koliko_ljudi(self):
        return len(self.vsi_ljudje)
            
    def koliko_je_placal(self, kdo):
        stroski = self.vsi_stroski
        if kdo not in self.vsi_ljudje:
            print('Uporabnik ne obstaja.')
        elif kdo not in stroski:
            return 0
        else:
            placano = 0
            sez = stroski.get(kdo)
            for strosek in sez:
                placano += strosek[1]
            return placano
        
    #def koliko_placa_vsak(self):
    #    znesek = self.znesek
    #    v_skupini = self.koliko_ljudi()
    
    def v_slovar(self):
        return {
            "ime": self.ime,
            "vsi_ljudje": self.vsi_ljudje,
            "vsi_stroski": self.vsi_stroski,
            "znesek": self.znesek,
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Skupina(
            slovar["ime"],
            [Oseba.iz_slovarja(slovar_ljudi) for slovar_ljudi in slovar["osebe"]],
            slovar["vsi_stroski"],
            slovar["znesek"],
        )
    
class Stanje():
    def __init__(self, skupine):
        self.skupine = skupine
        
    def dodaj_skupino(self, skupina):
        self.skupine.append(skupina)
    
    def v_slovar(self):
        return {
            "skupine": [skupina.v_slovar() for skupina in self.skupine],
        }

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Skupina.iz_slovarja(sl_skupine)
                for sl_skupine in slovar["skupine"]
            ]
        )
        return stanje

    def shrani_v_datoteko(self, datoteka):
        with open(datoteka, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii=False)

    @staticmethod
    def preberi_iz_datoteke(datoteka):
        with open(datoteka) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)
