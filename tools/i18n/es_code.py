# Code-Patches Spanisch
import en_code
_N={
"const HAND":"const HAND=t=>kmNow()==='h'?String(t).replace(/se despega bien de la cuba de la amasadora/g,'apenas se pega a las manos').replace(/de la cuba de la amasadora/g,'del bol').replace(/a la cuba de la amasadora/g,'al bol').replace(/la cuba de la amasadora/g,'el bol').replace(/cuba de la amasadora/g,'bol').replace(/a velocidad 1/g,'con una cuchara').replace(/Velocidad 1/g,'A mano').replace(/\\(3–4 min\\)/g,'(8–10 min)'):t;",
"const POST":"const POST=/Rúcula|Prosciutto|Burrata|Mortadela|Pistachos|Miel|Fresas|Azúcar glas|Nutella|Avellanas|trufa/;",
"const AISLE":"const AISLE=n=>/levadura$|^Levadura fresca|Fior di Latte|Burrata|Ricotta|Gorgonzola|Provola|Parmigiano|Pecorino|Salami|Salame|Salsiccia|Nduja|Prosciutto|Mortadella/.test(n)&&!/Levadura seca/.test(n)?'cold':/Albahaca|Setas|Rúcula|Tomates cherry|Calabacín|Pimiento|Berenjena|Brócoli|Cebolla|Patatas|Ajo|Perejil|Romero|Limón|Fresas|Friarielli/.test(n)?'fresh':'dry';",
"const FRESH":"const FRESH=/Fior di Latte|Burrata|Ricotta|Albahaca|Rúcula|Setas|Fresas|Tomates cherry|Friarielli/;",
"const tagCls":"const tagCls={Picante:'hot',Dessert:'bianca',Vegan:'veg',Fresca:'veg',Vegetariana:'veg'};",
"!/^Ab /":"!/^¡A la/.test(x.s.t)",
"r.wait.txt.replace":"r.wait.txt.replace(/ (en la nevera|a temperatura ambiente)$/,'')",
"||/^Teig ruht/":"||/^La masa reposa/.test(x.s.wait)?'':x.s.wait+'. ';",
"/^(Heute":"/^(Hoy|Mañana|Ayer)/",
"/Backen|BACKEN/":"/Hornear|HORNEAR/.test(r.t)",
"/\\b(weiter":"/\\b(siguiente|hecho|listo|vamos|okay|ok)\\b/",
"/zurück/":"/atrás/.test(t)",
"function spk":"function spk(t){return t.replace(/(\\d)\\.(\\d{3})/g,'$1$2').replace(/(\\d)\\s?g\\b/g,'$1 gramos').replace(/°C/g,' grados').replace(/\\bmin\\b/g,'minutos').replace(/×/g,' por ').replace(/(\\d)\\s?s\\b/g,'$1 segundos').replace(/–/g,' a ').replace(/·/g,', ');}",
"${msg==='Drehen!'":"${msg==='¡Gírala!'?' turn':''}",
'aria-label="Timer stoppen"':'aria-label="Parar el temporizador"',
'<p><b>Tipp</b>':'<p><b>Consejo</b>${h.tip}</p>',
"${S.pantry[x.k]?'hab ich da'":"${S.pantry[x.k]?'lo tengo':''}",
'<span class="dn">':'<span class="dn">${d.getDate()}</span>',
"$('glT')":None,
")(?![A-Za-zÄÖÜäöüß])','');":")(?![A-Za-zÀ-ÿ])','i');",
"${bsTxt(o)} pro Pizza":"${bsTxt(o)} por pizza</small>",
"hrTxt=":"hrTxt=tm(bk);",
"hr=B.":"hr=tm(B);",
"$('stAm')":"$('stAm').textContent=dd===0||dd===1?'':'el';{const vb=$('stAm').previousSibling;if(vb&&vb.nodeType===3)vb.nodeValue=B.getHours()<17?'Comemos ':'Cenamos ';}",
"MON=[":"MON=['ENE','FEB','MAR','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC'];",
"const tm=":"SKIP",
"[['22','22–7']":"[['22','22–7'],['23','23–8'],['0','0–9'],['off','no']]",
}
P=[]
for a,b,n in en_code.P:
    k=next(k for k in _N if a.startswith(k));v=_N[k]
    if v=='SKIP':continue
    P.append((a,b if v is None else v,n))
