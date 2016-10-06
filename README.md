This is an attempt to make a repl of jinja Template.render()

sort of works like this:

```python
jinrepl> {% for i in [1,2,3,4] %} {{ i }} {% endfor %}
 1  2  3  4
jinrepl>
```

or filter:
```python
jinrepl> {{ [1,2,3,4]  | first }}
> 1
jinrepl>
```

```python
jinrepl> {% for i in items %} My Items {{i}}  {% endfor %} -- {'items':[1,2,3,4]}
>  My Items 1   My Items 2   My Items 3   My Items 4
jinrepl>
```

```python
jinrepl> {% set var=1 %} {{var}}
>  1
jinrepl> 
```

```python
jinrepl> {{ dada.keys() }} -- {'dada':{'names':['jerry','garcia'] , 'hobbies':['linux','linux']}}
> ['names', 'hobbies']
jinrepl> {% set a={'names':['jerry','garcia'] , 'hobbies':['linux','linux']} %} {{a.keys()}}
>  ['names', 'hobbies']
jinrepl>
```





Todo:
* Color syntax
* redo up arrows DONE
* env aware 
* loads more

