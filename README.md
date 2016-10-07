This is an attempt to make a repl of jinja Template.render()

#What it does so far:

* evals all kinds of jinja templates
* shows exceptions
* all moving shortcuts that work on bash work on jinrepl too (Ctrl , arrows etc)
* autocompletes filters
* autocompletes conditionals and iterators 
* autocomplete end for conditionals and iterators.
* opens the one true editor and renders the contents 

#What's left to be done

* the parsing is very rudimentary
* color syntax
* environment aware ,  as in variables declared in different lines should be still ok to refer to
* everything else

## Loops
```python
jinrepl> {% for i in [1,2,3,4] %} {{ i }} {% endfor %}
 1  2  3  4
jinrepl>
```

## Filters

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
## Render with variables
I'm using  "--" as a separator , this has to change because it's ugly

```python
jinrepl> {{ dada.keys() }} -- {'dada':{'names':['jerry','garcia'] , 'hobbies':['linux','linux']}}
> ['names', 'hobbies']
jinrepl> {% set a={'names':['jerry','garcia'] , 'hobbies':['linux','linux']} %} {{a.keys()}}
>  ['names', 'hobbies']
jinrepl>
```

##Autocomplete (For filters only )

```python
jinrepl> {{1 |
{{1 | abs             {{1 | escape          {{1 | last            {{1 | reverse         {{1 | title
{{1 | attr            {{1 | filesizeformat  {{1 | length          {{1 | round           {{1 | trim
{{1 | batch           {{1 | first           {{1 | list            {{1 | safe            {{1 | truncate
{{1 | capitalize      {{1 | float           {{1 | lower           {{1 | select          {{1 | upper
{{1 | center          {{1 | forceescape     {{1 | map             {{1 | selectattr      {{1 | urlencode
{{1 | count           {{1 | format          {{1 | pprint          {{1 | slice           {{1 | urlize
{{1 | d               {{1 | groupby         {{1 | random          {{1 | sort            {{1 | wordcount
{{1 | default         {{1 | indent          {{1 | reject          {{1 | string          {{1 | wordwrap
{{1 | dictsort        {{1 | int             {{1 | rejectattr      {{1 | striptags       {{1 | xmlattr
{{1 | e               {{1 | join            {{1 | replace         {{1 | sum
jinrepl> {{1 |
```

## Autocomplete now for conditionals and iterators

```python
jinrepl> {% i
{% if       {% import   {% include
jinrepl> {% if 1==1 %} works! {% end
{% if 1==1 %} works! {% endblock  {% if 1==1 %} works! {% endfor    {% if 1==1 %} works! {% endif
jinrepl> {% if 1==1 %} works! {% endif %}
>  works!
jinrepl>
```

## Vim integration"" :

### Call vim!:

```python
jinrepl>
jinrepl> vim
```
### Add your j2 content:

![alt tag](https://raw.githubusercontent.com/bechampion/jinrepl/master/demoimg/vimedit.png)

### :wq it!

![alt tag](https://raw.githubusercontent.com/bechampion/jinrepl/master/demoimg/vimresult.png)














