# Erzeugt eine Sprachversion: python3 i18n/build_lang.py <en|it|fr|es> tempasto.html tempasto-<lang>.html
# Tabellen je Sprache: <lang>_code.py (P), <lang>_html.py (P, GUIDE), <lang>_lit.tsv
import sys,os,re,importlib
D=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,D)
import scan
LANG,SRC,OUT=sys.argv[1],sys.argv[2],sys.argv[3]
TITLE={'en':'Tempasto · Pizza dough planner','it':'Tempasto · Pianifica l’impasto','fr':'Tempasto · Planifier la pâte à pizza','es':'Tempasto · Planifica la masa'}
LBL={'en':'Choose language','it':'Scegli la lingua','fr':'Choisir la langue','es':'Elegir idioma'}
code=importlib.import_module(LANG+'_code');hm=importlib.import_module(LANG+'_html')
src=open(SRC,encoding='utf-8').read()
warn=[]
for a,b,n in code.P+[("window.TP_LANG='de';",f"window.TP_LANG='{LANG}';",1),
  ('<title>Tempasto · Pizzateig planen</title>',f'<title>{TITLE[LANG]}</title>',1)]:
    c=src.count(a)
    if c!=n:warn.append(f'CODE {c}x statt {n}x: {a[:70]}')
    src=src.replace(a,b)
T={}
for l in open(os.path.join(D,LANG+'_lit.tsv'),encoding='utf-8'):
    l=l.rstrip('\n')
    if not l or l.startswith('# '):continue
    k,v=l.split('\t',1)
    T[k[1:] if k.startswith('#') else scan.H(k)]=v
first_end=src.index('</script>')
a2=src.index('<script',first_end);a2=src.index('>',a2)+1;e=src.rindex('</script>')
used=set();out=[];last=0
for s0,t0 in scan.js_literals(src,a2,e):
    h=scan.H(src[s0:t0])
    if h in T:out.append(src[last:s0]);out.append(T[h]);last=t0;used.add(h)
out.append(src[last:]);src=''.join(out)
for h in T:
    if h not in used:warn.append(f'LIT unbenutzt: {h} {T[h][:50]}')
hp=src.index('<script',first_end)
html,rest=src[:hp],src[hp:]
g0=html.index('<p class="g-lead">');g1=html.index('</button>',html.index('id="introOpen"'))+9
html=html[:g0]+getattr(hm,'GUIDE',None or getattr(hm,'GUIDE_EN',''))+html[g1:]
for a,b in hm.P:
    if b is None:continue
    if a not in html:warn.append(f'HTML fehlt: {a[:70]}');continue
    html=html.replace(a,b)
src=html+rest
if LANG=='en':
    import en_us;src,_nd=en_us.apply(src)
src=src.replace('<html lang="de"','<html lang="'+LANG+'"')
open(OUT,'w',encoding='utf-8').write(src)
G=re.compile(r'[äöüÄÖÜß]|\b(und|der|die|das|nicht|mit|Teig|wenn|noch|Uhr|Pizzen|Kühlschrank|Backen|Erledigt|Später|Weiter|Zurück|Schritt)\b')
hp=src.index('<script',src.index('</script>'))
txt=re.sub(r'<style>.*?</style>|<svg.*?</svg>','',src[:hp],flags=re.S)
for m in re.findall(r'>([^<>]+)<',txt):
    if G.search(m):warn.append('HTML-REST: '+m.strip()[:80])
for m in re.findall(r'(?:aria-label|placeholder|alt)="([^"]+)"',txt):
    if G.search(m):warn.append('ATTR-REST: '+m[:80])
a=src.index('>',hp)+1;e=src.rindex('</script>')
for s0,t0 in scan.js_literals(src,a,e):
    x=src[s0:t0]
    if re.search(r'[äöüß]',x) or scan.GER.search(x) and not re.search(r'[A-Za-z]{3}',re.sub(scan.GER,'',x)):
        warn.append('JS-REST L%d: %s'%(src.count('\n',0,s0)+1,x[:90].replace('\n',' ')))
print('\n'.join(w for w in warn if not w.startswith('LIT unbenutzt')));print(len(warn),'Hinweise',file=sys.stderr)
