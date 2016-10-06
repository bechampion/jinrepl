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

Todo:
* Color syntax
* redo up arrows DONE
* env aware 
* loads more

