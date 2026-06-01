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

#   <font color='#4B9DA9'> Upozornenia </font>

[Upozornenia](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html) (admonitions) sú krátke zvýraznené úseky textu, ktoré obsahujú poznámky, upozornenia alebo varovania. 

```{note}
Typické jednoduché upozornenie pozostáva z farebne odlíšeného záhlavia a textu upozornenia. Text je štandardný formátovaný text, ktorý môže obsahovať ďaľšie direktívy (obrázky, vzorce a pod.)
```

##  <font color='#547792'> Jednoduché upozornenia </font>

Forma a farebné zobrazenie zvýraznenia závisí od použitej grafickej témy. Na platforme *Sphinx je definovaných niekoľko typov upozornení implementovaných ako direktívy.

      ```{typ_upozornenia}        - typ upozornenia
      :name: string               - referencia na upozornenie 
      
         text                     - formátovaný text 
      ```
         typ_upozornenia:
            note
            attention
            danger
            error
            hint
            important
            seealso
            tip
            warning
      


##  <font color='#547792'> Pomenované upozornenia </font>

Použitím direktívy **{admonition}** môžeme vytvárať pomenované upozornenia. Typ upozornenia môžemedefinovať v parametre **class**.


      ```{admonition} string      - názov upozornenia
      :class: typ_upozornenia     - typ
      :name: string               - referencia na upozornenie 
      
         text                     - formátovaný text 
      ```

Príklad použitia pomenovaného upozornenia.       

```{admonition} Dokumentácia k rozšíreniu {admonition}
:class: tip

Dokumentácia k rozšíreniu **{admonition}** je dostupná [online](https://myst-parser.readthedocs.io/en/latest/syntax/admonitions.html). 
```
      
      
##  <font color='#547792'> Rozbalovacie upozornenia </font>

S pomocou rozšírenia *sphinx-togglebutton* a parametrom **class** s hodnotou *dropdown* získame jednoduché alebo pomenované rozbalovacie upozornenie.

      ```{typ_upozornenia}        - jednoduché upozornenie
      :class: dropdown            - referencia na upozornenie 
      
         text                     - formátovaný text 
      ```


      ```{admonition} string      - názov pomenovaného upozornenia
      :class: dropdown, typ_upozornenia
      
         text                     - formátovaný text 
      ```

Príklad použitia rozbalovacieho upozornenia. 
      
```{admonition} Rozbalovacie pomenované upozornenie
:class: important, dropdown

Po klinutí na záhlavie sa rozbali text upozornenia.

      ```{admonition} Rozbalovacie pomenované upozornenie
      :class: important, dropdown

      text upozornenia
      ```
```
