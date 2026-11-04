# Baut www/ aus der Web-Version: python3 tools/make_www.py ../tempasto/tempasto.html
import sys, os, re, shutil
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(sys.argv[1] if len(sys.argv)>1 else os.path.join(root,'..','tempasto','tempasto.html'),encoding='utf-8').read()
# Google Fonts raus, lokale Schriften rein
src=re.sub(r'<link rel="preconnect"[^>]*>\s*','',src)
src=re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*','',src)
assert 'fonts.googleapis' not in src
title=re.search(r'<title>.*?</title>',src).group(0); src=src.replace(title,'',1)
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
html=f'''<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light">
{title}
<style>{css}html,body{{background:#F3F4EF}}</style>
<script src="capacitor.js"></script>
<script src="bridge.js"></script>
</head><body>
{src}
</body></html>'''
open(os.path.join(www,'index.html'),'w',encoding='utf-8').write(html)
print('www/index.html', len(html)//1024, 'KB')
