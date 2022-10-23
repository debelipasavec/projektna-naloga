from bottle import route, run, template, TEMPLATE_PATH, post, request, redirect
from datetime import date
import novo
from novo import Stanje

TEMPLATE_PATH.insert(0,'\\Users\\janko\\Desktop\\Projektna\\views')

SIFRIRNI_KLJUC = "To je poseben šifrirni ključ"

def ime_uporabnikove_datoteke(uporabnisko_ime):
    return f"stanja_uporabnikov\\{uporabnisko_ime}.json"


def stanje_trenutnega_uporabnika():
    uporabnisko_ime = request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    if uporabnisko_ime == None:
        redirect("/prijava/")
    else:
        uporabnisko_ime = uporabnisko_ime
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    try:
        os.chdir("\\Users\\janko\\Desktop\\Projektna\\")
        stanje = Stanje.iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje([])
        stanje.v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    uporabnisko_ime = request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    stanje.v_datoteko(ime_datoteke)

@route('/prijava/', method='GET')
def prijava_get():
    return template(
        "prijava.html"
    )

@route('/prijava/', method='POST')
def prijava_post():
    uporabnisko_ime = request.forms.getunicode("uporabnisko_ime")
    geslo = request.forms.getunicode("geslo")
    if uporabnisko_ime == geslo[::-1]:
        response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
        redirect("/")
    else:
        return "Napaka ob prijavi"

@route('/odjava/', method='POST')
def odjava_post():
    response.delete_cookie("uporabnisko_ime", path="/")
    redirect("/")

def url_osebe(id_osebe):
    return f"/oseba/{id_osebe}/"
    
@route('/', method='GET')
def zacetna_stran():
    stanje = stanje_trenutnega_uporabnika()
    return template(
        'zacetna_stran.html',
        stanje=stanje,
        ljudje=stanje.ljudje,
    )

@route('/oseba/<id_osebe:int>/', method='GET')
def oseba(id_osebe):
    stanje = stanje_trenutnega_uporabnika()
    return template(
        'oseba.html',
        stanje = stanje,
        id_osebe=id_osebe,
        oseba=stanje.ljudje[id_osebe],
    )

@route('/dodaj-strosek/<id_osebe:int>/', method='POST')
def dodaj_strosek(id_osebe):
    stanje = stanje_trenutnega_uporabnika()
    oseba = stanje.ljudje[id_osebe]
    id_osebe = id_osebe
    datum = date.fromisoformat(request.forms['datum'])
    cena = request.forms['cena']
    kaj = request.forms.getunicode('kaj')
    strosek = Strosek(datum, cena, kaj)
    oseba.dodaj_strosek(strosek)
    shrani_stanje_trenutnega_uporabnika()(stanje)
    redirect(url_osebe(id_osebe))

@route("/dodaj-osebo/", method='GET')
def dodaj_osebo_get():
    return template(
        "dodaj_osebo.html", napake={}, polja={}
    )
    
@route("/dodaj-osebo/", method='POST')
def dodaj_osebo_post():
    stanje = stanje_trenutnega_uporabnika()
    ime = request.forms.getunicode("ime")
    oseba = Oseba(ime, stroski=[])
    napake = stanje.preveri_osebo(oseba)
    if napake:
        polja = {"ime": ime}
        return template("dodaj_osebo.html", napake=napake, polja=polja)
    else:
        id_osebe = stanje.dodaj_osebo(oseba)
        shrani_stanje_trenutnega_uporabnika()(stanje)
        redirect(/url_osebe(id_osebe))
        
@route("/analiza/")
def analiza():
    stanje = stanje_trenutnega_uporabnika()
    return template(
        "analiza.html",
        stanje=stanje,
        ljudje=stanje.ljudje,
    )

run(host='localhost', port=8080, reloader=True, debug=True)
