# Erzeugt die englische Version: python3 i18n/build_en.py tempasto.html tempasto-en.html
import sys,os,re
D=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,D)
import scan,en_code,en_html
src=open(sys.argv[1],encoding='utf-8').read()
warn=[]
# 1 Code
for a,b,n in en_code.P+[("window.TP_LANG='de';","window.TP_LANG='en';",1),
  ('<title>Tempasto · Pizzateig planen</title>','<title>Tempasto · Pizza dough planner</title>',1),
  ('aria-label="Sprache: Deutsch. Auf Englisch umstellen"><b>DE</b><span>EN</span>','aria-label="Language: English. Switch to German"><span>DE</span><b>EN</b>',1)]:
    c=src.count(a)
    if c!=n:warn.append(f'CODE {c}x statt {n}x: {a[:70]}')
    src=src.replace(a,b)
# 2 Literale
T={}
for l in open(os.path.join(D,'en_lit.tsv'),encoding='utf-8'):
    l=l.rstrip('\n')
    if not l or l.startswith('# '):continue
    k,v=l.split('\t',1)
    T[k[1:] if k.startswith('#') else scan.H(k)]=v
a=src.index('<script');a=src.index('>',a)+1;e=src.rindex('</script>')
# alle Skripte ab dem zweiten <script> (das erste ist der Sprachumschalter)
first_end=src.index('</script>')
a2=src.index('<script',first_end);a2=src.index('>',a2)+1
lits=scan.js_literals(src,a2,e)
used=set();out=[];last=0
for s0,t0 in lits:
    x=src[s0:t0];h=scan.H(x)
    if h in T:
        out.append(src[last:s0]);out.append(T[h]);last=t0;used.add(h)
out.append(src[last:]);src=''.join(out)
for h in T:
    if h not in used:warn.append(f'LIT unbenutzt: {h} {T[h][:50]}')
# 3 HTML
hp=src.index('<script',first_end)
html,rest=src[:hp],src[hp:]
g0=html.index('<p class="g-lead">');g1=html.index('</button>',html.index('id="introOpen"'))+9
html=html[:g0]+en_html.GUIDE_EN+html[g1:]
for a,b in en_html.P:
    if b is None:continue
    if a not in html:warn.append(f'HTML fehlt: {a[:70]}');continue
    html=html.replace(a,b)
src=html+rest
open(sys.argv[2],'w',encoding='utf-8').write(src)
# Reste
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
    if scan.GER.search(x) and not re.fullmatch(r"'[^']*(Ä|Ö|Ü|ä|ö|ü|ß)[^']*'",x) or re.search(r'[äöüß]',x):
        warn.append('JS-REST L%d: %s'%(src.count('\n',0,s0)+1,x[:90].replace('\n',' ')))
print('\n'.join(warn));print(len(warn),'Hinweise',file=sys.stderr)
