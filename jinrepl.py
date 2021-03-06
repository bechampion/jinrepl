import jinja2
import os
from termcolor import colored
import rlcompleter, readline
import ast
import sys
import datetime

def complete_itercond(text,state):
    cond_ends = ["endif","endfor","endblock"]
    results = [x for x in list(jinja2.parser._statement_keywords)+cond_ends if x.startswith(text.split(jinja2.defaults.BLOCK_START_STRING)[-1].replace(" ",""))]+[None]
    return jinja2.defaults.BLOCK_START_STRING.join(text.split(jinja2.defaults.BLOCK_START_STRING)[:-1]) + jinja2.defaults.BLOCK_START_STRING+' ' +  results[state]

def complete_filters(text,state):
    results=[x for x in map(lambda x: x.replace("do_","") if x.startswith("do_") else x ,jinja2.filters.FILTERS.keys()) if x.startswith(text.split('|')[-1].replace(" ",""))]+[None]
    return "|".join(text.split('|')[:-1]) + '| ' +  results[state]

def complete_empty():
    return [None]

def exception_handler(e,empty=False):
    stre=str(e)
    if empty == True:
        stre = "Jinja2 empty response / variable undefinded??"
    msg="j2 Exception"
    magicnum = int(len(stre) - len(msg))/2
    print colored('-'*magicnum+msg+'-'*magicnum,'red')
    print stre
    print colored('-'*len(stre),'red')
    print
    return 0


def response_handler(response):
    if len(response) == 0:
        exception_handler("",True)
        return 0 
    msg = "j2"
    magicnum = int(len(str(response)) - len(msg))/2
    print colored('-'*magicnum+msg+'-'*magicnum,'green')
    print str(response)
    print colored('-'*len(response),'green')
    print
    return 0

def complete(text,state):
        if '|' in text: return complete_filters(text,state)
        if text.startswith(jinja2.defaults.BLOCK_START_STRING): return complete_itercond(text,state)
        else: return complete_empty()

def parser(i):
    ## this has to change, to shitty
    if "--" in i:
        try:
            code=i.split("--")[0]
            vars=ast.literal_eval(i.split("--")[1].replace(" ",""))
        except Exception as e:
            exception_handler(e)
            return 0 
    else:
        code=i
    try:
        if 'vars' not in locals():
            vars = {}
        response_handler(jinja2.Template(code).render(vars))
    except Exception as e:
        exception_handler(e)

def tmp_truncate():
    f = open(vim_tmp,'w')
    f.truncate()
    f.close()

def vim_parser():
    os.system("vim -c 'startinsert' %s" % vim_tmp)
    try:
        response_handler(jinja2.Environment(loader=jinja2.FileSystemLoader("/"+vim_tmp.split("/")[1])).get_template("/"+vim_tmp.split("/")[2]).render())
    except Exception as e:
        exception_handler(e)
    return 0

def init_readline():
    readline.set_completer_delims('\t\t')
    readline.parse_and_bind('tab: complete')
    readline.set_completer(complete)

def init_constants():
    global vim_tmp
    global env
    vim_tmp = "/tmp/jinrepl"
    return 0

def prompt():
    return "["+colored(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),'blue')+"] jinrepl"+colored("> ",'green')


def main():
    try:
        while True:
            i = raw_input(prompt())
            if i == "vim": vim_parser()
            elif not i: pass
            elif len(i) > 0 : parser(i)
            elif i == "exit": sys.exit(0) 
            else: pass 
            
    except KeyboardInterrupt:
        print "\n"
        sys.exit(0)
    except Exception as e:
        print e

if __name__ == "__main__":
    init_constants()
    tmp_truncate()
    init_readline()
    main()
