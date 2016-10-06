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

Autocomplete (For SOME filters only so far) , dir(jinja2.filters)
```python
jinrepl> {{ 1 |
{{ 1 | FILTERS              {{ 1 | center               {{ 1 | indent               {{ 1 | random               {{ 1 | text_type
{{ 1 | FilterArgumentError  {{ 1 | choice               {{ 1 | int                  {{ 1 | re                   {{ 1 | title
{{ 1 | Markup               {{ 1 | contextfilter        {{ 1 | itemgetter           {{ 1 | reject               {{ 1 | trim
{{ 1 | Undefined            {{ 1 | default              {{ 1 | iteritems            {{ 1 | rejectattr           {{ 1 | truncate
{{ 1 | _GroupTuple          {{ 1 | dictsort             {{ 1 | join                 {{ 1 | replace              {{ 1 | unicode_urlencode
{{ 1 | __builtins__         {{ 1 | environmentfilter    {{ 1 | last                 {{ 1 | reverse              {{ 1 | upper
{{ 1 | __doc__              {{ 1 | escape               {{ 1 | list                 {{ 1 | round                {{ 1 | urlencode
{{ 1 | __file__             {{ 1 | evalcontextfilter    {{ 1 | lower                {{ 1 | select               {{ 1 | urlize
{{ 1 | __name__             {{ 1 | filesizeformat       {{ 1 | make_attrgetter      {{ 1 | selectattr           {{ 1 | wordcount
{{ 1 | __package__          {{ 1 | first                {{ 1 | map                  {{ 1 | slice                {{ 1 | wordwrap
{{ 1 | _select_or_reject    {{ 1 | float                {{ 1 | mark_safe            {{ 1 | soft_unicode         {{ 1 | xmlattr
{{ 1 | _word_re             {{ 1 | forceescape          {{ 1 | mark_unsafe          {{ 1 | sort
{{ 1 | attr                 {{ 1 | format               {{ 1 | math                 {{ 1 | string_types
{{ 1 | batch                {{ 1 | groupby              {{ 1 | pformat              {{ 1 | striptags
{{ 1 | capitalize           {{ 1 | imap                 {{ 1 | pprint               {{ 1 | sum
jinrepl> {{ 1 |
```






Todo:
* Color syntax
* redo up arrows DONE
* env aware 
* loads more

