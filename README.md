# Projektna naloga

Predstavila vam bom projektno nalogo, ki sem jo napisala (ali skodirala - kakor vam je ljubše) pri predmetu Uvod v programiranje na Fakulteti za matematiko in fiziko, oddelek za Matematiko, Univerza v Ljubljani.

## Deljenje stroškov

Prav gotovo ste se kdaj odpravili na potovanje ali izlet s prijatelji. Skupaj ste se zelo zabavali, počeli norčije (ali mirno uživali na plaži), ko pa je prišlo do deljenja stroškov, je vaš pogovor izgledal nekako takole:

Marko: Janez, Mojca, kaj bi mi vrnila za karto za živalski vrt, ki sem vama jo plačal? Malo mi zmanjkuje denarja, zvečer bi pa rad šel v disko ...
Janez: Seveda, se mogoče spomniš, koliko je stala? Lahko delimo...
Mojca (se vrnine v besedo): Če smo že pri vračanju, pravzaprav sta mi vidva OBA dolžna, saj sem vama plačala večerjo v tisti fini restavraciji! Skoraj sem obubožala, ko sta "pozabila" denarnico v hotelu!
Janez: No, ne tako hitro Mojca, ti lisica!!! Tudi jaz sem plačal tisti nakup v zlatarni, kjer smo si kar privoščili! 
Marko: ... Ne da se mi računati vsega tega, vrjamem pa, da se tudi vama ne - smo samo ubogi študentje, ki želimo uživati v počitnicah brez matematike ... Ko bi le obstajal kak program, ki bi nam pomagal ...

In na srečo Marka, Janeza in Mojce tak program le obstaja. Že slišim, kako vzdihujejo od sreče.

## Opis programa

Z zgornjim skečem sem vas želela popeljati v samo idejo programa, ki pa se mi je utrnila letos septembra, ko sem se tako kot zgornji trije študentje odpravia na par tedensko popotovanje s prijatelji.

Sam program deluje precej preprosto - v skupino dodajate svoje potovalne prijatelje, pod vsakega prijatelja pa lahko vpišete, kje (kaj in koliko) je do sedaj "počastil" svojo skupino (npr. večerje, skupni shopping v butičnih trgovincah, vstopnice ...). Program samodejno izračuna skupne stroške prijatelja, pove pa tudi, koliko mu je skupina še dolžna oziroma je dolžan njej sam. 
Biti dolžan pomeni na skupni (fizični) "kup" položiti določeno količino denarja, dobiti pa iz "kupa" vzeti.

## Kako program zagnati?

Zagnati program je precej preprosto:
* iz repozitorija si naložite zip datoteko,
* odprete datoteko spletni_vmesnik.py v izbranem urejevalniku in
  * v vrstici 7 popravite absolute path do datoteke views, ki je v sklopu datotek, ki ste si jih naložili
    primer: TEMPLATE_PATH.insert(0,"\\Users\\mami\\Downloads\\Projektna\\views"),
  * v vrstici 22 si morate prav tako popraviti absolute path, ki vas pripelje samo do mape, kamor ste si naložili mojo projektno
    primer: os.chdir("\\Users\\oci\\Documents\\super\\kul\\program\\Projektna\\"),
*  poženite datoteko in kliknite na povezavo, ki se vam izpiše v terminalu,
*  odprla se vam bo spletna stran, kamor se morate prijaviti. Vaše uporabniško ime je kakršno vam srce poželi, geslo pa je uporabniško ime v drugo smer (npr. uporabniško ime je uporabnik, geslo pa kinbaropu).

## Težave

Pri pisanju je bila edina velika težava, na katero sem naletela ta, da se mi spletni vmesnik ni poganjal iz mape, kjer so bile shranjene ostale datoteke. Razlog za to mi je neznan, težavo pa sem odpravila s tem, da sem 2x uporabila absolute path do map. 
Druga težava pa je bila ta, da se mi Git na računalniku ni hotel pognati (pomoč sem poiskala tudi pri bratrancu, ki pa ga žal tudi ni znal "popraviti"). Torej sem datoteke na žalost morala nalagi samo preko GitHuba.

## Stil

Stila izgleda strani nisem spisala sama, uporabljala sem spletno ogrodje [Materialize](https://materializecss.com/).
