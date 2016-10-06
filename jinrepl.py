import jinja2
from termcolor import colored
import rlcompleter, readline
import ast
import sys



def complete(text,state):
        texttemp = text
        if '|' in text:
            results=[x for x in map(lambda x: x.replace("do_","") if x.startswith("do_") else x ,dir(jinja2.filters)) if x.startswith(text.split('|')[-1].replace(" ",""))]+[None]
            return "|".join(text.split('|')[:-1]) + '| ' +  results[state]
        else:
            return [None]
def parser(i):
    if "--" in i:
        code=i.split("--")[0]
        vars=ast.literal_eval(i.split("--")[1].replace(" ",""))
    else:
        code=i
    try:
        if 'vars' not in locals():
            vars = {}
        print colored('> ','green') +  jinja2.Template(code).render(vars)
    except Exception as e:
        print colored('e: ','red') , e

def main():
    readline.set_completer_delims('\t\t')
    readline.parse_and_bind('tab: complete')
    readline.set_completer(complete)

    try:
        while True:
            i = raw_input('jinrepl' + colored('> ','red'))
            if not i: pass
            if len(i) > 0 : parser(i)
            if i == "exit": sys.exit(0) 
            
    except KeyboardInterrupt:
        print "\n"
        sys.exit(0)
    except Exception as e:
        print e

if __name__ == "__main__":
    main()
