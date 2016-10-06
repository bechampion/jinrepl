from jinja2 import Template
from termcolor import colored
import readline
import ast
import sys

def parser(i):
    if "--" in i:
        code=i.split("--")[0]
        vars=ast.literal_eval(i.split("--")[1].replace(" ",""))
    else:
        code=i
    try:
        if 'vars' not in locals():
            vars = {}
        print colored('> ','green') +  Template(code).render(vars)
    except Exception as e:
        print colored('e: ','red') , e

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
    main()
