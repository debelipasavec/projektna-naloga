from bottle import route, run, template, TEMPLATE_PATH, post, request, redirect
from datetime import date
import novo
from novo import Stanje

TEMPLATE_PATH.insert(0,'\\Users\\janko\\Desktop\\Projektna\\views')

stanje = novo.primer_stanja 

def url_osebe(id_osebe):
    return f"/oseba/{id_osebe}/"
    
@route('/', method='GET')
def zacetna_stran():
    return template(
        'zacetna_stran.html',
        stanje=stanje,
    )
    
@route('/oseba/<id_osebe:int>/')
def oseba(id_osebe):
    return template(
        'oseba.html',
        oseba=stanje.ljudje[id_osebe],
        id_osebe = id_osebe,
    )

@route('/dodaj-strosek/<id_osebe:int>/', method='POST')
def dodaj_strosek(id_osebe):
    oseba = stanje.ljudje[id_osebe]
    id_osebe = id_osebe
    datum = date.fromisoformat(request.forms['datum'])
    cena = request.forms['cena']
    kaj = request.forms.getunicode('kaj')
    strosek = Strosek(datum, cena, kaj)
    oseba.dodaj_strosek(strosek)
    redirect(url_osebe(id_osebe))

@route("/dodaj-osebo/", method='GET')
def dodaj_osebo_get():
    return template(
        "dodaj_osebo.html", napake={}, polja={}
    )
    
@route("/dodaj-osebo/", method='POST')
def dodaj_osebo_post():
    ime = request.forms.getunicode("ime")
    oseba = Oseba(ime, stroski=[])
    napake = stanje.preveri_osebo(oseba)
    if napake:
        polja = {"ime": ime}
        return template("dodaj_osebo.html", napake=napake, polja=polja)
    else:
        id_osebe = stanje.dodaj_osebo(oseba)
        redirect(url_osebe(id_osebe))
        
@route("/analiza/")
def analiza():
    return template(
        "analiza.html",
        stanje=stanje,
    )

run(host='localhost', port=8080, reloader=True, debug=True)
