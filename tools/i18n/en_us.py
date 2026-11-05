# Amerikanisches Englisch: nach der Übersetzung auf die ganze englische Datei angewendet
import re
WORDS=[('full-flavoured','full-flavored'),('flavour','flavor'),('Flavour','Flavor'),('centre','center'),('aluminium','aluminum'),
 ('Rocket','Arugula'),('rocket','arugula'),('Wholemeal','Whole wheat'),('wholemeal','whole wheat'),('cancelled','canceled'),('cancelling','canceling'),
 ('favourite','favorite'),('recognised','recognized'),('Minimise','Minimize'),('minimise','minimize'),('yoghurt','yogurt'),('Tomato tin','Tomato can'),
 ('Ball proof','Final proof'),('ball proof','final proof'),('Watch the intro','Watch the intro')]
# Datum in US-Reihenfolge: "Nov 6" statt "6 Nov"
DATE=re.compile(r"\$\{([A-Za-z0-9_.]+)\.getDate\(\)\} \$\{(\['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'\]|MS|MON)\[\1\.getMonth\(\)\]\}")
def apply(s):
    for a,b in WORDS:s=re.sub(r'(?<![A-Za-z])'+re.escape(a)+r'(?![a-z])',b,s)
    s,n=DATE.subn(lambda m:'${'+m.group(2)+'['+m.group(1)+'.getMonth()]} ${'+m.group(1)+'.getDate()}',s)
    return s,n
