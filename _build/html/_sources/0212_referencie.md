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

#   <font color='#4B9DA9'> Odkazy a referencie </font>

V texte dokumentu sa môžeme odkazovať pomocou referencií na lokálne dokumenty na dokumenty a stránky z internetu, ako aj na miesta v publikácii, ako sú kapitoly, odstavce (paragrafy) alebo časti textu. Referencie môžu byť sučasťou rozširujúcich direktív dokumentu, ako sú obrázky, poznámky, matematické vzťahy a podobne.  

Pre vkladanie odkazov je potrebné v *conf.py* aktivovať rozšírenia pre *Markdown*

    myst_enable_extensions = [
        ...
        "attrs_inline",
        "attrs_block",
        ...
        ]

```{admonition} Upozornenie 
:class: attention
:name: rekompilacia 

Pri vytvorení a použití odkazov medzi rôznymi súbormi publikácie je potrebné aktualizovať internú tabuľku krížových referencií skompilovaním celého projektu publikácie. 
```
    
##  <font color='#547792'> Odkaz na kapitolu </font>

Referenciu na kapitolu vytvoríme jej menom v zátvorkách nasledovaných znakom **=** bez medzier.

    (heading-target)=                   - meno odkazu na kapitolu
    # Názov kapitoly
    
```{admonition} Príklad použitia
:class: tip, dropdown

V cieľovom texte dokumentu, na ktorý budeme odkazovať, umiestnime referenciu k príslušnému názvu kapitoly alebo podkapitoly

    (ref_tabulky)=
    # Tabuľky

V zdrojovom texte, z ktorého sa odkazujeme na kapitolu, referenciu použijeme

    Toto je odkaz na [kapitolu](ref_tabulky), ktorá popisuje vytváranie tabuliek. 

Toto je odkaz na [kapitolu](ref_tabulky), ktorá popisuje vytváranie tabuliek. 
    
```

##  <font color='#547792'> Odkaz na paragraf </font>    

    {#paragraph-target}              - meno referencie na paragraf (so znakom #) 
    Text odstavca v dokumente.

```{admonition} Príklad použitia
:class: tip, dropdown

V cieľovom texte dokumentu, na ktorý budeme odkazovať, umiestnime referenciu k paragrafu 

    {#ref_list_table}
    Direktíva **(list-table)** je určená pre

V zdrojovom texte, z ktorého sa odkazujeme na paragraf, referenciu použijeme 

    Toto je odkaz na [paragraf](ref_list_table)

Toto je odkaz na [paragraf](ref_list_table) popisujúci použitie direktívy *{list-table}*.
```    

    
##  <font color='#547792'> Odkaz na text </font>      

V publikácii sa môžeme odkazovať aj na konkrétne miesta v cieľovom texte označením miesta v texte a priradením referencie. Označené miesto v texte nie je v zdrojovom v dokumente zvýraznené.

    This is a [span with an attribute]{#span-target}.

```{admonition} Príklad použitia
:class: tip, dropdown

Do cieľového textu dokumentu umiestnime referenciu  

    Parameter *tag* určuje formu zobrazenia, [tagy]{#ref_tag} označené ako ...
    
Na referenciu sa odkážene v zdrojovom texte 

    Pomocou [parametrov](ref_tag) môžeme upraviť formu zobrazenia ...
    
Pomocou [parametrov](ref_tag) môžeme upraviť formu zobrazenia ...
```
    
##  <font color='#547792'> Odkaz na direktívu </font>  

Väčšina direktív pre úpravu a rozširovanie textu *{image}, {figure}, {table}* ... má parameter *:name:*, ktorým definujeme referenciu na direktívu. Direktívy pre vkladanie tabuliek, matematických vzťahov *{math}* a zdrojového textu *{code-block}* majú pre označenie referencie parameter *:label:* alebo špeciálny formát, ktorý je popísaný v ich [dokumentácii](math_insert).

````{admonition} Príklady použitia
:class: tip, dropdown

    ```{note}                     - direktíva
    :name: referencia             - definícia referencie

    Text direktívy.
    ```
Príklad použitia 
    
    Odkaz na upozornenie o potrebe [preloženia](rekompilacia) 
    projektu po vytvorení a použití referencií. 
    
    Odkaz na [obrázok](img0302a) z kapitoly *Rastrová grafika*.

Odkaz na upozornenie o potrebe [preloženia](rekompilacia) projektu po vytvorení a použití referencií. 

Odkaz na [obrázok](img0302a) z kapitoly *Rastrová grafika*.
````
    
    
##  <font color='#547792'> Odkaz na externý dokument </font>  
    
Odkazy na lokálne dokumenty alebo www stránky majú formát

    [text](path)      - relatatívna cesta k internému dokumentu
    [text](url)       - url csta k dokumentu na intranete/internete
    
    
```{admonition} Príklad použitia
:class: tip, dropdown

    Manuál k prostrediu pre tvorbu matematických vzťahov [amsldoc](./doc/amsldoc.pdf).
    
    Online dokumentácia k [MyST](https://myst-parser.readthedocs.io/en/latest/intro.html). 

Manuál k prostrediu pre tvorbu matematických vzťahov [amsldoc](./doc/amsldoc.pdf).

Online dokumentácia k [MyST](https://myst-parser.readthedocs.io/en/latest/intro.html). 
```


##  <font color='#547792'> Numerické odkazy </font>  

Ak sa potrebujeme v texte odkazovať na číslo obrázku, matematického vzťahu, listingu alebo tabulky, použijeme v texte formát odkazu v tvare

    {numref}`referencia`

```{admonition} Príklad použitia
:class: tip, dropdown

    Odkaz na obrázok číslo {numref}`img0302a` z kapitoly *Rastrová grafika*.

Odkaz na obrázok číslo {numref}`img0302a` z kapitoly *Rastrová grafika*.

```
