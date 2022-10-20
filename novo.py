from dataclasses import dataclass
from datetime import date
from typing import List
import json
        
@dataclass        
class Strosek:
    datum: date
    cena: float
    kaj: str

    def v_slovar(self):
        return {
            "datum": self.datum.isoformat(),
            "cena": self.cena,
            "kaj": self.kaj,
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            datum=date.fromisoformat(slovar["datum"]),
            cena=slovar["cena"],
            kaj=slovar["kaj"],
        )
    
@dataclass
class Oseba:
    ime: str
    stroski: List[Strosek]
    
    def spremeni_ime(self, novo_ime):
        self.ime = novo_ime
    
    def dodaj_strosek(self, strosek):
        if strosek in self.stroski:
            print("Strošek že obstaja.")
        else:
            self.stroski.append(strosek)
        
    def odstrani_strosek(self, strosek):
        if strosek not in self.stroski:
            print("Strošek ne obstaja.")
        else:
            self.stroski.remove(strosek)
    
    def premakni_strosek(self, other, strosek):
        self.odstrani_strosek(strosek)
        other.dodaj_strosek(strosek)
            
    def koliko_je_placal(self):
        vsota = 0
        for strosek in self.stroski:
            vsota += strosek.cena()
        return vsota  
          
    def v_slovar(self):
        return {
            "ime": self.ime,
            "stroski": [strosek.v_slovar() for strosek in self.stroski],
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            ime=slovar["ime"],
            stroski=[Strosek.iz_slovarja(sl) for sl in slovar["stroski"]],
        )

@dataclass
class Stanje:
    ljudje: List[Oseba]
        
    def dodaj_osebo(self, oseba):
        if oseba in self.ljudje:
            print("Oseba že obstaja.")
        else:
            self.ljudje.append(oseba)
            return len(self.ljudje) - 1
        
    def odstrani_osebo(self, oseba):
        if oseba in self.ljudje:
            print("Oseba ne obstaja.")
        else:
            self.ljudje.remove(oseba)
            
    def preveri_osebo(self, nova_oseba):
        for oseba in self.ljudje:
            if oseba.ime == nova_oseba.ime:
                return {'ime': "Oseba že obstaja."}
    
    def dodaten_strosek(self, datum, cena, kaj, ime):
        strosek = Strosek(datum, cena, kaj)
        ime.dodaj_strosek(strosek)
    
    def st_ljudi(self):
        return len(self.ljudje)
    
    def skupni_stroski(self):
        return format(round(sum(oseba.koliko_je_placal() for oseba in self.ljudje), 2), '.2f')
        
    
    def cena_na_osebo(self):
        stroski = sum(oseba.koliko_je_placal() for oseba in self.ljudje)
        dol = len(self.ljudje)
        return round(stroski / dol, 2)
        #return format(round(stroski / dol, 2), '.2f') 
    
    def koliko_potrebuje(self, ime):
        potrebno = Stanje.cena_na_osebo(self)
        je_placal = ime.koliko_je_placal()
        skupno = round(potrebno - je_placal, 2)
        if skupno < 0:
            return f'Dobiti moraš {- skupno} €.'
        elif skupno > 0:
            return f'Dati moraš {skupno} €.'
        else:
            return f'Bravo, nimaš dolgov!'
    
    def v_slovar(self):
        return {
            "ljudje": [oseba.v_slovar() for oseba in self.ljudje],
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            ljudje=[Oseba.iz_slovarja(sl) for sl in slovar["ljudje"]],
        ) 
    
    def v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            json.dump(self.v_slovar(), dat, ensure_ascii=False, indent=4)

    @classmethod
    def iz_datoteke(cls, ime_datoteke):
        with open(ime_datoteke) as dat:
            return cls.iz_slovarja(json.load(dat))


nina = Oseba('Nina', [Strosek(date(2022, 4, 23), 20.4, 'hrana'), Strosek(date(2022, 4, 26), 4, 'karte')])
zala = Oseba('Zala', [])

flus = Oseba('Flus', [Strosek(date(2022, 5, 3), 1, 'kava'), Strosek(date(2022, 2, 26), 15.4, 'krana')])
crt = Oseba('Crt', [Strosek(date(2022, 4, 6), 7.5, 'mleko')])

primer_stanja = Stanje([nina, zala, flus, crt])
