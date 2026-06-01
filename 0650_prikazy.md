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

# <font color='#4B9DA9'> Direktívy </font>

Blok direktívy začína a končí apostrofmi ` ``` `. Formát direktív má všeobecný tvar:

    ```{meno_direktívy} argument   - záhlavie
    :par1: hodnota1                - zoznam parametrov
    :par2: hodnota2
    
    obsah direktívy                - text, program, povely
    
    ```                            - ukončenie direktívy

    
```{admonition} Poznámka
:class: warning

Medzi názvom parametra a jeho hodnotou musí byť medzera, inak interpreter hlási chybu 

    :name:obrazok      - WARNING: undefined label: `obrazok`
    :name: obrazok     - správny tvar

```

Zoznam parametrov je špecifický pre danú direktívu a závisí od jej implementácie. Direktívy je možné vnárať, vtedy sa počet apostrofov zvyšuje o hĺbku vnorenia direktív. Pre lepšiu prehľadnosť je možné text direktív vzájomne odsadovať maximálne o 3 znaky, pri väčšom odsadení bude text direktívy interpretovaný ako neformátovaný textový blok. 


    `````{direktiva_1}         -----+
                                    |
       ````{direktiva_2}       ---+ |
                                  | |
          ```{direktiva_3}     -+ | |
                                | | |
          ```                  -+ | |
       ````                    ---+ |
                                    |
       ````{direktiva_4}       -+   |
                                |   |
       ````                    -+   |
                                    |
    `````                      -----+ 

    
V nasledujúcej tabuľke je zoznam najčastejšie používaných direktív, podrobnejší popis je dostupný v dokumentácii. 

```{csv-table} Zoznam direktív
    :delim: ;
    :name: tab1
    :header: Príkaz; Parametre; Popis; 
    :width: 85%
    :widths: auto
    :align: center

    {math}; label; matematické vzťahy
    {table}; name \n align width; jednoduchá tabulka
    {csv-table}; name align width; tabulka formátovaná v CSV
    {list-table}; name align width; tabulka formátovaná v zozname

```


