# Baut www/ aus der Web-Version: python3 tools/make_www.py tempasto.html [tempasto-en.html]
# Ohne zweite Datei wird die englische Version mit tools/i18n/build_en.py erzeugt.
# Ergebnis: www/index.html (Deutsch) und www/en.html (Englisch). Die App wählt die Sprache selbst.
import sys, os, re, shutil, subprocess, tempfile
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DE=sys.argv[1] if len(sys.argv)>1 else os.path.join(root,'..','tempasto','tempasto.html')
SRC_EN=sys.argv[2] if len(sys.argv)>2 else None
if not SRC_EN:
    SRC_EN=os.path.join(tempfile.gettempdir(),'tempasto-en.html')
    subprocess.run([sys.executable,os.path.join(root,'tools','i18n','build_en.py'),SRC_DE,SRC_EN],check=True,stdout=subprocess.DEVNULL)
www=os.path.join(root,'www'); os.makedirs(os.path.join(www,'fonts'),exist_ok=True)
F=[('Bricolage Grotesque','bricolage-grotesque',[600,800]),('Figtree','figtree',[400,500,600,700]),('IBM Plex Mono','ibm-plex-mono',[500,600])]
css=''
for fam,pkg,ws in F:
    for w in ws:
        fn=f'{pkg}-latin-{w}-normal.woff2'
        shutil.copy(os.path.join(root,'node_modules','@fontsource',pkg,'files',fn),os.path.join(www,'fonts',fn))
        css+=f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url(fonts/{fn}) format('woff2')}}\n"
shutil.copy(os.path.join(root,'node_modules','@capacitor','core','dist','capacitor.js'),os.path.join(www,'capacitor.js'))
shutil.copy(os.path.join(root,'tools','bridge.js'),os.path.join(www,'bridge.js'))
def page(srcfile,out,lang):
    src=open(srcfile,encoding='utf-8').read()
    # Google Fonts raus, lokale Schriften rein
    src=re.sub(r'<link rel="preconnect"[^>]*>\s*','',src)
    src=re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*','',src)
    assert 'fonts.googleapis' not in src
    title=re.search(r'<title>.*?</title>',src).group(0); src=src.replace(title,'',1)
    html=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light">
{title}
<style>{css}html,body{{background:#F3F4EF}}</style>
<script>window.TEMPASTO_PAGES={{de:'index.html',en:'en.html'}};</script>
<script src="capacitor.js"></script>
<script src="bridge.js"></script>
</head><body>
{src}
</body></html>'''
    open(os.path.join(www,out),'w',encoding='utf-8').write(html)
    print('www/'+out, len(html)//1024, 'KB')
page(SRC_DE,'index.html','de')
page(SRC_EN,'en.html','en')
