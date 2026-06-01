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

#   <font color='#4B9DA9'> Obsah </font>

Pre previazania jednotlivých stránok do uceleného dokumentu vytvárame obsah, ktorý je zvyčajne umiestnený v úvode publikácie. Obsah môže mať formu stromu, kde kmeňom je základné člemenie publikácie na kapitoly reprezentuúce vetvy stromu. Vetvy môžu mať vlastný obsah odkazujúci na jednotlivé podkapitoly. *Sphinx* takúto štrruktúru potom v publikácii reprezentuje pomocou rozbalovacieho menu.  

## <font color='#547792'> Tvorba obsahu </font>

### <font color='#E37434'> {toctree} </font>

Pre tvorbu obsahu je v *Sphinx* deklarovaná direktíva **{toctree}**.

    ```{toctree} 
    :name: string                 - referencia na položku obsahu 
    :caption: string              - názov položky obsahu (kapitola a pod.)
    :numbered:                    - bez argumentu čísluje všetky položky obsahu, 
    :numbered: nuumber            - argument určuje hĺbku číslovania 
    :titlesonly: boolean          - v obsahu zobrazuje len názov dokumentu (prvý heading)
    :reversed:                    - zobrazenie položiek v opačnom poradi
    :hidden:
    :includehidden:
    :glob:
    
    súbor_1                       - položky obsahu
    súbor_2
    ```

Pri súboroch v zdrojovom adresári nezaradených v obsahu *Sphinx* pri kompilácii vygeneruje varovania.



