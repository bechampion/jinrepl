from jinja2 import Template
import ast

def parser(i):
    if "--" in i:
        code=i.split("--")[0]
        vars=ast.literal_eval(i.split("--")[1].replace(" ",""))
    else:
        code=i
    try:
        if "vars" not in locals():
            vars = {}
        print Template(code).render(vars)
    except Exception as e:
        print e

def main():
    while True:
        i = raw_input('jinrepl> ')
        if not i:
            break
        parser(i)
if __name__ == "__main__":
    main()
