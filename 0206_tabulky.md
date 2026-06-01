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

#   <font color='#4B9DA9'> Tabuľky </font>

Prehľadná reprezentácia dát pomocou tabuliek je dôležitou súčasťou odborných textov. Pretože sa dáta pre zobrazenie v tabuľkách môžu vyskytovať v rôznych formátoch, plaftorma *Sphinx* umožňuje ich vytváranie niekoľkými [spôsobmi](https://mystmd.org/guide/tables).

##  <font color='#547792'> Vkladanie tabuliek  </font>

Pre vkladanie tabuliek do textu je v *Sphinx* niekoľko direktív, ktoré sú prispôsobené rôznym formátom zobrazovaných dát.

### <font color='#E37434'> *{table}* </font>

Direktíva **{table}** je určená pre zadávanie menších jednoduchých tabuliek v textovom formáte.

    ```{table} meno                   - názov tabulky
    :name: string                     - referencia
    :align: position                  - poloha tabulky v texte left, center, right
    :width: number                    - šírka tabulky v px alebo %

    | name    | name    |             - záhlavie
    | :---:   | :---:   |             - formátovanie  stlpcov ---, :---,  :---:, ---:
    | data    | data    |             - formatované dáta       
    | data    | data    |
    ```

````{dropdown}  <font color='#84B179'> Použitie direktívy {table} </font>
    ```{table} Menný zoznam
    :name: table1
    :align: center
    :width: 600px

    | Meno | Priezvisko |
    | :---: | :---:|
    | Janko | Hraško |
    | Karkulka | Červená |
    ```
    
```{table} Menný zoznam
:name: table1
:align: center
:width: 600px

| Meno     | Priezvisko |
| :---:    | :---:      |
| Janko    | Hraško     |
| Karkulka | Červená    |
```

````
Údaje do tabuľku sa môžu nachádzať aj v externom súbore, pre ich uloženie do tabuľku použijeme vnorenú direktívu **{include}**. 

    ````{table} meno

       ```{include} file              - cesta a súbor s dátami
       ```                          
    ````



### <font color='#E37434'> *{csv-table}* </font>

Direktíva **(csv-table)** je určená pre vytvorenie tabuľky z dát v [CSV formáte](https://sk.wikipedia.org/wiki/Comma-separated_values). Dáta môžu byť umiextnené in-line v zdrojovom texte dokumentu alebo v externom súbore.

    ```{csv-table} nazov tabulky
        :label: string                - referencia na tabulku
        :header: string, string, ...  - mená stĺpcov tabulky
        :header-rows: number          - počet riadkov z CSV tabulky použitých pre záhlavie
        :width: number                - celková šírka tabulky na stránke v px alebo %
        :align: position              - poloha tabulky v texte left, center, right
        :delim: char                  - oddelovač položiek v dátach
        :widths: number, number ...   - relatívne šírky stĺpcov (suma 100)
        :keepspace: boolean           - ak true, nebudú medzery za delimiterom ignorované
        :encoding:
        :escape:
        :file:
        :quote:
        :stub-columns:
        :url:

        data                          - CSV formátované data
    ```

````{dropdown}  <font color='#84B179'> Použitie direktívy {csv-table} </font>
    
    ```{csv-table} Meno tabulky
        :header: Meno,  Priezvisko, Vek
        :header-rows: 0
        :width: 65%
        :widths: 35, 45, 20
        :align: center

        Šrek, Bažinatý, 35
        Oslík, Ukecaný, 10
        Ježibaba, Škaredá, 180
    ```

```{csv-table} Meno tabulky
    :header: Meno,  Priezvisko, Vek
    :header-rows: 0
    :width: 65%
    :widths: 35, 45, 20
    :align: center

    Šrek, Bažinatý, 35
    Oslík, Ukecaný, 10
    Ježibaba, Škaredá, 180
```
````

### <font color='#E37434'> *{list-table}* </font>

Direktíva **(list-table)** je určená pre vytvorenie tabuľky z jednoduchého zoznamu.

    ```{list-table} meno 
        :name: string                 - referencia na tabulku
        :width: number                - celková šírka tabulky na stránke v px alebo %
        :align: position              - poloha tabulky v texte left, center, right
        :widths: number, number ...   - relatívne šírky stĺpcov (suma 100)
        :stub-columns:

    * - header_a                      - záhlavie tabulky
      - header_b
    * - data_1a                       - riadok 1 tabulky
      - data_1b
    * - data_2a                       - riadok 2 tabulky
      - data_2b
    ```

````{dropdown}  <font color='#84B179'> Použitie direktívy {list-table} </font>
    
    ```{list-table} Významné osobnosti
        :name: table3                
        :width: 65%
        :align: center

    * - **Meno**
      - **Povolanie**
    * - Maťko
      - bača
    * - Kubko
      - asistent baču
    ```

```{list-table} Významné osobnosti
    :name: table3                
    :width: 65%
    :align: center

* - **Meno**
  - **Povolanie**
* - Maťko
  - bača
* - Kubko
  - asistent baču
```
````
    
### <font color='#E37434'> *<table\>* </font>

Do publikácie môžeme vkladať tabuľky formátované v [HTML](https://www.w3schools.com/html/html_tables.asp) a upravovať ichv vzhľad pomocou CSC štýlov. K takto vloženým tabulkám nie je možné v *Sphinx* vytvoriť referenciu.

    <table>
      <tr>
        <th> header_a </th>           - zahlavie tabulky
        <th> header_b </th>
      </tr>
      <tr>
        <td> data_1a </td>            - riadok 1 tabulky
        <td> data_1b </td>
      </tr>
      ...
    </table>

````{dropdown}  <font color='#84B179'> Použitie HTML tabulky </font>

    <table  style="width:60%; border: 1px solid black; td { padding: 10px; border: 1px solid black; border-collapse: collapse; }" >
      <tr>
        <th style="border: 1px solid black; padding: 10px;"> Company</th>
        <th style="border: 1px solid black; padding: 10px;">Contact</th>
        <th style="border: 1px solid black; padding: 10px;">Country</th>
      </tr>
      <tr>
        <td>Alfreds Futterkiste</td>
        <td>Maria Anders</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Centro comercial Moctezuma</td>
        <td>Francisco Chang</td>
        <td>Mexico</td>
      </tr>
    </table>


<table  style="width:60%; border: 1px solid black; td { padding: 10px; border: 1px solid black; border-collapse: collapse; }" >
  <tr>
    <th style="border: 1px solid black; padding: 10px;"> Company</th>
    <th style="border: 1px solid black; padding: 10px;">Contact</th>
    <th style="border: 1px solid black; padding: 10px;">Country</th>
  </tr>
  <tr>
    <td>Alfreds Futterkiste</td>
    <td>Maria Anders</td>
    <td>Germany</td>
  </tr>
  <tr>
    <td>Centro comercial Moctezuma</td>
    <td>Francisco Chang</td>
    <td>Mexico</td>
  </tr>
</table>

````

