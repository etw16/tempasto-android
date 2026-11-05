# Findet Text-Literale im JS-Teil von tempasto.html
import re,hashlib,sys,json
def js_literals(src,start,end):
    out=[];i=start;n=end;prev=''
    def skip_str(i,q):
        j=i+1
        while j<n:
            c=src[j]
            if c=='\\':j+=2;continue
            if c==q:return j+1
            if q=='`' and c=='$' and src[j+1]=='{':
                j=skip_expr(j+2)
                continue
            j+=1
        raise Exception('unterminated at %d'%i)
    def skip_expr(j):
        depth=1;p=''
        while j<n:
            c=src[j]
            if c in '\'"`':j=skip_str(j,c);p='a';continue
            if c=='/' and p in '(,=:[!&|?{};+-*%<>~^' :
                j=skip_re(j);p='a';continue
            if c=='{':depth+=1
            elif c=='}':
                depth-=1
                if depth==0:return j+1
            if not c.isspace():p=c
            j+=1
        raise Exception('expr')
    def skip_re(j):
        k=j+1;cls=False
        while k<n:
            c=src[k]
            if c=='\\':k+=2;continue
            if c=='[':cls=True
            elif c==']':cls=False
            elif c=='/' and not cls:
                k+=1
                while k<n and src[k].isalpha():k+=1
                return k
            elif c=='\n':return j+1
            k+=1
        return k
    while i<n:
        c=src[i]
        if src.startswith('</script>',i):
            # jump to next <script>
            m=src.find('<script',i+1)
            if m<0 or m>=n:break
            i=src.find('>',m)+1;prev='';continue
        if c=='/' and src[i+1]=='/' :
            i=src.find('\n',i);prev=';';continue
        if c=='/' and src[i+1]=='*':
            i=src.find('*/',i)+2;continue
        if c in '\'"`':
            j=skip_str(i,c);out.append((i,j));i=j;prev='a';continue
        if c=='/' and (prev=='' or prev in '(,=:[!&|?{};+-*%<>~^'):
            i=skip_re(i);prev='a';continue
        if c.isalnum() or c in '_$)]':
            # handle keyword return
            m=re.match(r'[A-Za-z_$][\w$]*',src[i:i+30])
            if m:
                w=m.group(0);i+=len(w);prev=';' if w in('return','typeof','case','in','of') else 'a';continue
            prev='a';i+=1;continue
        if not c.isspace():prev=c
        i+=1
    return out
GER=re.compile(r'[äöüÄÖÜß„“]|\b(der|die|das|und|ist|nicht|mit|den|dem|ein|eine|einen|du|dich|dir|dein|deine|wenn|auf|zum|zur|im|aus|bei|noch|jetzt|heute|morgen|Uhr|Teig|Teiglinge?|Pizzen|Hefe|Mehl|Wasser|Salz|Kneten|Backen|Ofen|Stunden?|Minuten?|Tag|Tage|vor|nach|für|oder|sind|wird|kann|Schritt|Plan|Zeitplan|Kühlschrank|Raum|Belag|Soße|Erledigt|Später|Weiter|Zurück|Abbrechen|Teilen|Kopieren|Gehzeit|Vorteig|Sicherung|Daten|Rezept|Einkauf|Mehr|Start|Erinnerung|frisch|kalt|warm|Glut|Stein|Blech|Holz|Gas|Elektro|Backofen|Klassik|Scharf|Alle|Gemüse|Käse|Schinken|Pilze|Zwiebel|Knoblauch|Oliven|Kapern|Sardellen|Basilikum)\b')
def H(t):return hashlib.sha1(t.encode()).hexdigest()[:6]
def scan(path):
    src=open(path,encoding='utf-8').read()
    a=src.index('<script');a=src.index('>',a)+1
    e=src.rindex('</script>')
    lits=js_literals(src,a,e)
    res=[]
    for s,t in lits:
        txt=src[s:t]
        if GER.search(txt):res.append((s,t,txt))
    return src,res
if __name__=='__main__':
    src,res=scan(sys.argv[1])
    seen={}
    for s,t,txt in res:
        h=H(txt)
        if h in seen:seen[h][1]+=1;continue
        seen[h]=[txt,1,src.count('\n',0,s)+1]
    print(len(res),len(seen),sum(len(v[0]) for v in seen.values()),file=sys.stderr)
    for h,(txt,c,ln) in seen.items():
        print(f'#{h} L{ln}'+(f' x{c}' if c>1 else '')+'\t'+txt)

def candidates(src):
    a=src.index('<script');a=src.index('>',a)+1;e=src.rindex('</script>')
    out=[]
    for s,t in js_literals(src,a,e):
        x=src[s:t];b=x[1:-1]
        if not GER.search(x):
            if not re.search(r'[A-Za-zÄÖÜäöü]{2}',b):continue
            if re.fullmatch(r'[a-z0-9_\-:.#\[\]=" >,()*+~^$|@%/]*',b):continue
            if re.fullmatch(r'[a-z]+[A-Z][\w]*',b):continue
            if re.fullmatch(r'[#.][\w\-\s>.#,:()\[\]=\'"*]+',b):continue
            if re.match(r'\s*<(svg|path|circle|g |ellipse|rect|line|polyline|defs|stop|linearGradient)',b):continue
            if re.fullmatch(r'[A-Z]+:.*|[A-Z]+',b) and b not in('MENU','JETZT','BACKEN','MAI','APRIL','JANUAR','FEBRUAR','JUNI','JULI','AUGUST','SEPTEMBER','OKTOBER','NOVEMBER','DEZEMBER','MÄRZ'):continue
        out.append((s,t,x))
    return out
