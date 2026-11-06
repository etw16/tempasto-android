# Code-Patches für die italienische Version (alt, neu, Anzahl), angewendet auf die deutsche Quelle
import en_code
_O={a:n for a,b,n in en_code.P}
_N={
"const HAND":"const HAND=t=>kmNow()==='h'?String(t).replace(/si stacca bene dalla ciotola dell’impastatrice/g,'si attacca appena alle mani').replace(/ciotola dell’impastatrice/g,'ciotola').replace(/a velocità 1/g,'con un cucchiaio').replace(/Velocità 1/g,'A mano').replace(/\\(3–4 min\\)/g,'(8–10 min)'):t;",
"const POST":"const POST=/Rucola|Prosciutto|Burrata|Mortadella|Pistacchi|Miele|Fragole|Zucchero a velo|Nutella|Nocciole|tartufo/;",
"const AISLE":"const AISLE=n=>/lievito$|^Lievito fresco|Fior di Latte|Burrata|Ricotta|Gorgonzola|Provola|Parmigiano|Pecorino|Salami|Salame|Salsiccia|Nduja|Prosciutto|Mortadella/.test(n)&&!/Lievito secco/.test(n)?'cold':/Basilico|Funghi|Rucola|Pomodorini|Zucchine|Peperone|Melanzana|Broccoli|Cipolla|Patate|Aglio|Prezzemolo|Rosmarino|Limone|Fragole|Friarielli/.test(n)?'fresh':'dry';",
"const FRESH":"const FRESH=/Fior di Latte|Burrata|Ricotta|Basilico|Rucola|Funghi|Fragole|Pomodorini|Friarielli/;",
"const tagCls":"const tagCls={Piccante:'hot',Dessert:'bianca',Vegan:'veg',Fresco:'veg',Vegetariana:'veg'};",
"!/^Ab /":"!/^Via /.test(x.s.t)",
"r.wait.txt.replace":"r.wait.txt.replace(/ (in frigo|a temperatura ambiente)$/,'')",
"||/^Teig ruht/":"||/^L’impasto riposa/.test(x.s.wait)?'':x.s.wait+'. ';",
"/^(Heute":"/^(Oggi|Domani|Ieri)/",
"/Backen|BACKEN/":"/Infornare|INFORNARE/.test(r.t)",
"/\\b(weiter":"/\\b(avanti|fatto|finito|vai|okay|ok)\\b/",
"/zurück/":"/indietro/.test(t)",
"function spk":"function spk(t){return t.replace(/(\\d)\\.(\\d{3})/g,'$1$2').replace(/(\\d)\\s?g\\b/g,'$1 grammi').replace(/°C/g,' gradi').replace(/\\bmin\\b/g,'minuti').replace(/×/g,' per ').replace(/(\\d)\\s?s\\b/g,'$1 secondi').replace(/–/g,' a ').replace(/·/g,', ');}",
"${msg==='Drehen!'":"${msg==='Gira!'?' turn':''}",
'aria-label="Timer stoppen"':'aria-label="Ferma il timer"',
'<p><b>Tipp</b>':'<p><b>Consiglio</b>${h.tip}</p>',
"${S.pantry[x.k]?'hab ich da'":"${S.pantry[x.k]?'ce l’ho':''}",
'<span class="dn">':'<span class="dn">${d.getDate()}</span>',
"$('glT')":None,
")(?![A-Za-zÄÖÜäöüß])','');":None,
"${bsTxt(o)} pro Pizza":"${bsTxt(o)} a pizza</small>",
"hrTxt=":"hrTxt=tm(bk);",
"hr=B.":"hr=tm(B);",
"$('stAm')":"$('stAm').textContent='';",
"MON=[":"MON=['GEN','FEB','MAR','APR','MAG','GIU','LUG','AGO','SET','OTT','NOV','DIC'];",
"const tm=":"SKIP",
"[['22','22–7']":"[['22','22–7'],['23','23–8'],['0','0–9'],['off','no']]",
}
P=[]
for a,b,n in en_code.P:
    k=next(k for k in _N if a.startswith(k))
    v=_N[k]
    if v=='SKIP':continue
    P.append((a,b if v is None else v,n))
