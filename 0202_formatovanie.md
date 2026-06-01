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

# <font color='#4B9DA9'> Formátovanie textu</font>

Zdrojový text dokumentu vytvárame v ľubovolnom textovom editore pre editovanie natívneho testu (nie v textovom editore z kancelárskych balíkov). Je vhodné, aby editor rozpoznával a farebne zvyrazňoval syntax formátovania *Markdown*, napríklad [Geany](https://www.geany.org/), [Visual Studio Code](https://code.visualstudio.com/), [Kate](https://kate-editor.org/) a ďaľšie.

##  <font color='#547792'> Komentáre </font>

Znakom ```%``` označíme v zdrojový texte dokumentu riadky s komentárom, poznámkami alebo časti dokumentu ktoré budú vyradené z generovania výsledného dokumentu:

      % komentár v dokumente je pri konverzii textu ignorovaný 


##  <font color='#547792'> Neformátovaný text </font>

Text odsadený o 4 a viac znakov od okraja strany je pokladaný za neformátovaný blok a je zobrazený v samostatnej bunke. Využíva sa najmä pri vkladaní zdrojových kódov programov a skriptov, ukážkach formátovania textu a všade tam, kde nie je vhodná interpretácia formátovania textu.

    Toto je neformátovaný text.
    # Riadiace **sekvencie** pre formátovanie textu sú ignorované.

##  <font color='#547792'> Záhlavie dokumentu </font>

Každá samostatná kapitola dokumentu musí začínať záhlavím začínajúcim jedným znakom mriežky ```#```, označenia podkapitol začínajú opakovaním tohoto znaku až do 6-tej úrovne. Záhlavia v hlavnom texte se prenášajú do obsahu dokumentu. 

    # Názov kapitoly
       ...
       ## Podkapitola 1.
       ...
          ### Odsek 1.
          ...
          ### Odsek 2.
          ...
       ## Podkapitola 2.
       ...
    
```{admonition} Poznámka
:class: tip
Konvertor *Sphinx* kontroluje hierachické usporiadanie textu, pri vynechaní názvu kapitoly alebo niektorej úrovne podkapitol vypíše pri konverzii upozornenie. 
```


##  <font color='#547792'> Typ textu </font>

Základné formátovanie textu ako *šikmý text*, **tučný text**, ***šikmý tučný text*** a `zvýraznený text` získame použitím hviezdičkovej konvencie a apostrofov:

    *šikmý text*
    **tučný text**
    ***šikmý tučný text***
    `zvýraznený text`
    


```{admonition} Poznámka
:class: tip
Text musí byť medzi hviedičkamu uzatvorený bez medzier na začiatku a konci, v opačnom prípade je formátovanie ignorované.

        **chyba **
```

##  <font color='#547792'> Farba textu </font>

Farebnú reprezentáciu textu môžeme definovať pomocou [HTML značiek](https://www.w3schools.com/html/default.asp). Pre zmenu farby textu môžeme použiť značku ```<font>...</font>```

    <font color='COLOR_NAME'> text </font>
    <font color='#RRGGBB'> text </font>

kde ```COLOR_NAME``` je meno pomenovanej farby. Zoznam mien štandardných farieb je uvedený nižšie, kompletný zoznam mien farieb rozpoznávaných www prehliadačmi je uvedený v [HTML dokumentácii](https://www.w3schools.com/colors/colors_names.asp). 

```{dropdown}  <font color='#84B179'> Mená základnej sady farieb </font>

* <font color='black'> white </font>
* <font color='silver'> silver </font>
* <font color='gray'> gray </font>
* <font color='black'> black </font>
* <font color='red'> red </font>
* <font color='maroon'> maroon </font>
* <font color='yellow'> yellow </font>
* <font color='olive'> olive </font>
* <font color='lime'> lime </font>
* <font color='green'> green </font>
* <font color='aqua'> aqua </font>
* <font color='teal'> teal </font>
* <font color='blue'> blue </font>
* <font color='navy'> navy </font>
* <font color='fuchsia'> fuchsia </font>
* <font color='purple'> purple </font>

```

Farbu textu môžeme zadať aj pomocou hexadecimálneho číselného kódu vo formáte ```#RRGGBB``` s hodnotami farebných zložiek červenej, zelenej a modrej farby. Prevod zvolenej farby na jej kód je súčasťou každého grafického editora, interaktívne si môžeme vygenerovať kódy pre zvolené farby na špecializovaných stránkach [internetu](https://htmlcolorcodes.com/).

Širšie možnosti formátovania farebného zobrazenie texty umožňuje atribút ```style``` v spojení so značkou [HTML elementu](https://www.w3schools.com/TAGs/att_global_style.asp) ```<p>```, ```<h1>```, ```<h2>```  ... : 

    <span style='style_definitions'> text </span>     - inline text
    <p    style='style_definitions'> text </p>        - paragraf
    <h1   style='style_definitions'> text </h1>       - zahlavie dokumentu
    
    style_definitions:
        color: COLOR_NAME;              - farba textu
        color: #RRGGBB;
        
        background-color: COLOR_NAME;   - farba pozadia textu 
        background-color: #RRGGBB;
        
        border: width type color;       - rámik textu
            width                       - šírka rámiku v px 
            type                        - typ ramika, dotted solid double dashed

       border-radius: value;            - polomer rohov rámika v px

       
```{dropdown}  <font color='#84B179'> Príklad 1. Farebné zvýraznenie textu. </font>

      Farebný inline <span style='color:fuchsia'> text </span>. 
      
      Zvýraznený <span style='color: #FF0000;border: 
                        1px solid green; 
                        background-color: aqua; 
                        border-radius: 5px;'>text</span> v rámiku.

Farebný <span style='color:fuchsia'> text </span>. 

Zvýraznený <span style='color: #FF0000;border: 
                        1px solid green; 
                        background-color: aqua; 
                        border-radius: 5px;'>text</span> v rámiku.
```       
       

       
```{dropdown}  <font color='#84B179'> Príklad 2. Farebné zvýraznenie paragrafu. </font>
    <p style='color:red'> 
        Farebne výraznený paragraf. 
    </p>. 

<p style='color:red'> Farebne výraznený paragraf. </p>. 
```
       
       
```{admonition} Poznámka
:class: tip
HTML značka ```<font>``` je vo verzii *HTML 5* pokladaná za zastaralú a jej používanie sa v nových dokumentoch neodporúča.
```





