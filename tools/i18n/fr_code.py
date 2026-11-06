# Code-Patches Französisch
import en_code
_N={
"const HAND":"const HAND=t=>kmNow()==='h'?String(t).replace(/se détache bien de la cuve du pétrin/g,'colle à peine aux mains').replace(/de la cuve du pétrin/g,'du saladier').replace(/la cuve du pétrin/g,'le saladier').replace(/cuve du pétrin/g,'saladier').replace(/en vitesse 1/g,'à la cuillère').replace(/Vitesse 1/g,'À la main').replace(/\\(3–4 min\\)/g,'(8–10 min)'):t;",
"const POST":"const POST=/Roquette|Prosciutto|Burrata|Mortadelle|Pistaches|Miel|Fraises|Sucre glace|Nutella|Noisettes|truffe/;",
"const AISLE":"const AISLE=n=>/levure$|^Levure fraîche|Fior di Latte|Burrata|Ricotta|Gorgonzola|Provola|Parmigiano|Pecorino|Salami|Salame|Salsiccia|Nduja|Prosciutto|Mortadella/.test(n)&&!/Levure sèche/.test(n)?'cold':/Basilic|Champignons|Roquette|Tomates cerises|Courgettes|Poivron|Aubergine|Brocoli|Oignon|Pommes de terre|Ail|Persil|Romarin|Citron|Fraises|Friarielli/.test(n)?'fresh':'dry';",
"const FRESH":"const FRESH=/Fior di Latte|Burrata|Ricotta|Basilic|Roquette|Champignons|Fraises|Tomates cerises|Friarielli/;",
"const tagCls":"const tagCls={Épicée:'hot',Dessert:'bianca',Vegan:'veg',Fraîche:'veg',Végétarienne:'veg'};",
"!/^Ab /":"!/^Direction /.test(x.s.t)",
"r.wait.txt.replace":"r.wait.txt.replace(/ (au frigo|à température ambiante)$/,'')",
"||/^Teig ruht/":"||/^La pâte repose/.test(x.s.wait)?'':x.s.wait+'. ';",
"/^(Heute":"/^(Aujourd’hui|Demain|Hier)/",
"/Backen|BACKEN/":"/Enfourner|ENFOURNER/.test(r.t)",
"/\\b(weiter":"/\\b(suivant|fait|fini|go|okay|ok)\\b/",
"/zurück/":"/retour/.test(t)",
"function spk":"function spk(t){return t.replace(/(\\d)[\\s\\u202f\\u00a0](\\d{3})/g,'$1$2').replace(/(\\d)\\s?g\\b/g,'$1 grammes').replace(/°C/g,' degrés').replace(/\\bmin\\b/g,'minutes').replace(/×/g,' fois ').replace(/(\\d)\\s?s\\b/g,'$1 secondes').replace(/–/g,' à ').replace(/·/g,', ');}",
"${msg==='Drehen!'":"${msg==='Tourne-la !'?' turn':''}",
'aria-label="Timer stoppen"':'aria-label="Arrêter le minuteur"',
'<p><b>Tipp</b>':'<p><b>Astuce</b>${h.tip}</p>',
"${S.pantry[x.k]?'hab ich da'":"${S.pantry[x.k]?'j’en ai':''}",
'<span class="dn">':'<span class="dn">${d.getDate()}</span>',
"$('glT')":None,
")(?![A-Za-zÄÖÜäöüß])','');":")(?![A-Za-zÀ-ÿ])','i');",
"${bsTxt(o)} pro Pizza":"${bsTxt(o)} par pizza</small>",
"hrTxt=":"hrTxt=tm(bk);",
"hr=B.":"hr=tm(B);",
"$('stAm')":"$('stAm').textContent='';",
"MON=[":"MON=['JANV.','FÉVR.','MARS','AVR.','MAI','JUIN','JUIL.','AOÛT','SEPT.','OCT.','NOV.','DÉC.'];",
"const tm=":"SKIP",
"[['22','22–7']":"[['22','22–7'],['23','23–8'],['0','0–9'],['off','non']]",
}
P=[]
for a,b,n in en_code.P:
    k=next(k for k in _N if a.startswith(k));v=_N[k]
    if v=='SKIP':continue
    P.append((a,b if v is None else v,n))
