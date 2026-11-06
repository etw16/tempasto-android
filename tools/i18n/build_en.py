# Englische Version: python3 i18n/build_en.py tempasto.html tempasto-en.html
import sys,os,subprocess
sys.exit(subprocess.call([sys.executable,os.path.join(os.path.dirname(os.path.abspath(__file__)),'build_lang.py'),'en']+sys.argv[1:3]))
