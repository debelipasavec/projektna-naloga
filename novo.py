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
            
    def koliko_je_placal(self):
        vsota = 0
        for strosek in self.stroski:
            vsota += strosek.cena()
        return vsota  
    
    def koliko_potrebuje(self):
        potrebno = Skupina.cena_na_osebo()
        je_placal = self.koliko_je_placal
        skupno = potrebno - je_placal
        if skupno < 0:
            return f'Dobiti moraš {skupno} €.'
        elif skupno > 0:
            return f'Dolžen si {skupno} €.'
        else:
            return f'Bravo, nimaš dolgov!'
        
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
class Skupina:
    ime: str
    ljudje: List[Oseba]
    
    def spremeni_ime(self, novo_ime):
        self.ime = novo_ime
    
    def dodaj_osebo(self, oseba):
        if oseba in self.ljudje:
            print("Oseba že obstaja.")
        else:
            self.ljudje.append(oseba)
        
    def odstrani_osebo(self, oseba):
        if oseba in self.ljudje:
            print("Oseba ne obstaja.")
        else:
            self.ljudje.remove(oseba)
    
    def st_ljudi(self):
        return len(self.ljudje)
    
    def skupni_stroski(self):
        vsota = 0
        for oseba in self.ljudje:
            koliko = oseba.koliko_je_placal()
            vsota += koliko
        return vsota
    
    def cena_na_osebo(self):
        return round(self.skupni_stroski / self.st_ljudi, 2) 
    
    def v_slovar(self):
        return {
            "ime": self.ime,
            "ljudje": [oseba.v_slovar() for oseba in self.ljudje],
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            ime=slovar["ime"],
            ljudje=[Oseba.iz_slovarja(sl) for sl in slovar["ljudje"]],
        ) 
    
@dataclass
class Stanje:
    skupine: List[Skupina]
    
    def dodaj_skupino(self, skupina):
        if skupina in self.skupine:
            print("Skupina že obstaja.")
        else:
            self.ljudje.append(skupina)
        
    def odstrani_skupino(self, skupina):
        if skupina in self.ljudje:
            print("Skupina ne obstaja.")
        else:
            self.ljudje.remove(skupina)
    
    def koliko_skupin(self):
        return len(self.skupine)
    
    def v_slovar(self):
        return {
            "skupine": [skupina.v_slovar() for skupina in self.skupine],
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        return cls(
            skupine=[Skupina.iz_slovarja(sl) for sl in slovar["skupine"]],
        )
    
    def v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            json.dump(self.v_slovar(), dat, ensure_ascii=False, indent=4)

    @classmethod
    def iz_datoteke(cls, ime_datoteke):
        with open(ime_datoteke) as dat:
            return cls.iz_slovarja(json.load(dat))
