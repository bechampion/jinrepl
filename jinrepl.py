import jinja2
from termcolor import colored
import rlcompleter, readline
import ast
import sys

def complete_itercond(text,state):
    cond_ends = ["endif","endfor","endblock"]
    results = [x for x in list(jinja2.parser._statement_keywords)+cond_ends if x.startswith(text.split(jinja2.defaults.BLOCK_START_STRING)[-1].replace(" ",""))]+[None]
    return jinja2.defaults.BLOCK_START_STRING.join(text.split(jinja2.defaults.BLOCK_START_STRING)[:-1]) + jinja2.defaults.BLOCK_START_STRING+' ' +  results[state]

def complete_filters(text,state):
    results=[x for x in map(lambda x: x.replace("do_","") if x.startswith("do_") else x ,jinja2.filters.FILTERS.keys()) if x.startswith(text.split('|')[-1].replace(" ",""))]+[None]
    return "|".join(text.split('|')[:-1]) + '| ' +  results[state]

def complete_empty():
    return [None]

def complete(text,state):
        if '|' in text: return complete_filters(text,state)
        if text.startswith(jinja2.defaults.BLOCK_START_STRING): return complete_itercond(text,state)
        else: return complete_empty()

def parser(i):
    ## this has to change, to shitty
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

def init_readline():
    #some __init__()
    readline.set_completer_delims('\t\t')
    readline.parse_and_bind('tab: complete')
    readline.set_completer(complete)

def main():
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
    init_readline()
    main()
