---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

% #   <font color='#4B9DA9'> level 1 </font>
% ##  <font color='#547792'> level 2 </font>
% ### <font color='#E37434'> level 3 </font>
% {dropdown} <font color='#84B179'> Text </font>

#   <font color='#4B9DA9'> Zdrojové kódy </font>

##  <font color='#547792'> Použitie zdrojových kódov </font>

V texte publikácie môžeme použiť zdrojové kódy programov 

* ako pasívne fragmenty kódov, ukážky programov, implementáncie algoritmov v rôznych programovacích jazykoch so zvýraznenou syntaxou vo forme listingov 
* vo forme in-line vykonateľných programov a skriptov so zobrazením výstupov, ako sú demonštračné výpočty, grafy a pod. generovaných počas kompilácie v texte publikácie
* ako volania programov tretích strán nad rozsah rozšírení platformy *Sphinx*

### <font color='#E37434'> *{code-block}* </font>
 
Direktíva **{code-block}** je určená pre pasívne zobrazenie kódu programu.

    ```{code-cell} programovaci_jazyk
    :label: string                - referencia na výpis programu (listing)
    :caption: string              - názov listingu
    :linenos: boolean             - zobrazeni čísel riadkov
    :lineno-start: number         - poradové číslo začiatku číslovania riadkov
    :emphasize-lines: list        - zoznam čísel riadkov, ktoré budú zvýraznené
    :filename: string
    
    zdrojový kód programu
    ```

````{dropdown}  <font color='#84B179'> Použitie direktívy {code-block} </font>

Direktíva *{code-block}* v texte dokumentu:

    ```{code-block} python
    :name: lst_208a
    :caption: Výpis programu
    :linenos: true
    :emphasize-lines: 3,4

    from numpy import sqrt, pow

    for i in range(10):
      print(i, pow(i,2), sqrt(i) )
        
    ```
Výsledok direktívy v renderovanom dokumente.

```{code-block} python
:name: lst_208a
:caption: Výpis programu
:linenos: true
:emphasize-lines: 3,4

from numpy import sqrt, pow

for i in range(10):
  print(i, pow(i,2), sqrt(i) )
```
````

 ### <font color='#E37434'> *{code-cell}* </font>
 
Direktíva *{code-cell}* vloží do textu vykonateľný kód programu a zobrazí jeho výstup v texte dokumentu. 

    ```{code-cell} interpreter    - python, ipython3
    :tag: [string, ...]
    
    zdrojový kód programu
    ```
Parameter *tag* určuje formu zobrazenia, tagy označené ako *hide-...* skryjú kód, jeho výstup alebo kód s výstupom do rolovacieho okna, parametre označené ako *remove-...* odstránia príslušnú časť alebo aj celý kód zo zdrojového textu po jeho vykonaní. 
    
* hide-input
* hide-output
* hide-cell
* remove-input
* remove-output
* remove-cell

      ```{code-cell} ipython3  
      :tags: [hide-input, hide-output]

      from numpy import sqrt, pow

      for i in range(11):
          print(f' {i:2d}   {pow(i,2): 4d}   {sqrt(i):2.4f}')
      ```

```{code-cell} ipython3  
:tags: [hide-input, hide-output]


from numpy import sqrt, pow

for i in range(11):
    print(f' {i:2d}   {pow(i,2): 4d}   {sqrt(i):2.4f}')

```
