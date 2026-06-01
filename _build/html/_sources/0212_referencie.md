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

##  <font color='#547792'> Odkazy </font>

Pre vkladanie odkazov je potrebné v *conf.py* aktivovať rozšírenie pre *Markdown*

    myst_enable_extensions = [
        ...
        "attrs_inline",
        "attrs_block",
        ...
        ]
        

### <font color='#E37434'> Odkaz na názov kapitoly </font>

    (heading-target)=
    ### Názov kapitorly

### <font color='#E37434'> Odkaz na paragraf </font>    

    {#paragraph-target}
    This is a paragraph, with an attribute.
    
### <font color='#E37434'> Odkaz na text </font>      

    This is a [span with an attribute]{#span-target}.

    
### <font color='#E37434'> Odkaz na direktívu </font>  

Odkaz na direktívu pre vloženie poznámky s parametrom *:name:*

    :::{note}
    :name: directive-target

    Toto je poznámka s parametrom :name:
    :::


Odkaz na obrázok zobrazený pomocou direktívy *{tikz}*, ktorá neobsahuje parameter *:name:*

    ```{tikz} Konvertovaný [obrázok]{#image}
    :include: ./img/cart0157.tikz
    :xscale: 20
    ```

### <font color='#E37434'> Použitie odkazov </font> 

    * [reference1](#heading-target)
    * [reference2](#paragraph-target)
    * [obrazok](#image),
    * [reference3](#span-target)
    * [reference4](#directive-target)






