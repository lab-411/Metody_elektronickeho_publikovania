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

#   <font color='#4B9DA9'> Diagramy </font>

##  <font color='#547792'> PlantUML </font>

[PlantUML](https://plantuml.com) je open-source nástroj, ktorý umožňuje používateľom vytvárať diagramy pomocou jednoduchého textového jazyka. Je primárne zameraný na vytváranie diagramov pre jednotlivé časti metodológie UML ([Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)):

* Sequence diagram
* Usecase diagram
* Class diagram
* Object diagram
* Activity diagram 
* Component diagram
* Deployment diagram
* State diagram
* Timing diagram

Diagram tried zobrazujúci dedičnosť je na obrázku {numref}`graf0`.

```{uml}
:caption: Class diagram v metodológii UML.
:name: graf0
:align: center
:scale: 100%

abstract Shape{
  void move()
  {abstract} void clear()
  {abstract} void draw()
  }
  
class Square{
  void clear()
  void draw()
}

class Circle{
  void clear()
  void draw()
}

class Triangle{
  void clear()
  void draw()
}

class Line{
  void clear()
  void draw()
}

Shape <|-- Square
Shape <|-- Circle
Shape <|-- Triangle
Shape <|-- Line

```

Okrem týchto základných typov diagramov PlantUML podporu pre rôzne ďalšie formáty súvisiace s vývojom softvéru

* Diagramy pre zobrazenie štruktúr JSON, YAML, EBNF, Regex 
* Vývojové diagramy SDL a Entity Relationship diagramy
* Ganttove diagramy
* Myšlienkové mapy MindMap
* Zobrazenie štruktúry adresárov 


**Inštalácia**

Inštalácia pozostáva zo stiahnutia programu, ktorý je vytvorený v jazyku Java a inštalácie rozhrania pre platformu Sphinx. Pre spustenie programu je vyžadované prostredie Java, ktoré je zvyčajne súčasťou operačného systému. Funkčnosť prostredia Java a jeho aktuálny verziu overíme v konzole príkazom

    java -version

Zo stránky [programu](https://plantuml.com/download) je potrebné stiahnúť skompilovaný  *.jar* súbor *plantuml-x-nnnn.jar* a uložiť ho do pracovného adresáru. Inštalácia rozhrania pre platformu Sphinx

    pip install sphinxcontrib-plantuml

**Konfigurácia**

Integrácia programu do platformy *Sphinx* je v súbore *config.py* zaradením do zoznamu *extensions*, nastavením *javy* a cesty do adresáru s programom zoznamom *plantuml*:

    extensions = [
        ...
        'sphinxcontrib.plantuml',
        ...
    ]

    plantuml = ["java", "-jar", "./plantuml/plantuml-1.2026.2.jar"]
    

### <font color='#E37434'> *{uml}* </font>

Direktíva **{uml}** je určená pre vloženie diagramu, nastavenie veľkosti diagramu, jeho pozície a priradeniu referencie.

    ```{uml}
      :caption: text              - názov diagramu
      :height: number             - výška diagramu v px
      :width: number              - šírka diagramu v px
      :scale: number              - zmena rozmerov v %
      :align: string              - poloha diagramu center, left, right
    
      Zdrojový kód diagramu
    ```
    
       
````{dropdown}  <font color='#84B179'> Príklad: Vývojový diagram </font>


    ```{uml}
    :caption: Vývojový diagram
    :name: graf1
    :align: center

      start
      repeat
        :read data;
        :generate diagrams;
      repeat while (more data?) is (yes) not (no)
      stop
    ```

```{uml}
:caption: Vývojový diagram
:name: diag1
:align: center
:scale: 100%

start

repeat
  :read data;
  :generate diagrams;
repeat while (more data?) is (yes) not (no)

stop
```
````

````{dropdown}  <font color='#84B179'> Príklad: Myšlienková mapa </font>


    ```{uml}
    :caption: Vývojový diagram
    :align: center
    :scale: 80%

      @startmindmap
      * Debian
      ** Ubuntu
      *** Linux Mint
      *** Kubuntu
      *** Lubuntu
      *** KDE Neon
      ** LMDE
      ** SolydXK
      ** SteamOS
      ** Raspbian with a very long name
      *** <s>Raspmbc</s> => OSMC
      *** <s>Raspyfi</s> => Volumio
      @endmindmap
    ```

```{uml}
:caption: Myšlienková mapa MindMap
:align: center
:scale: 80%

@startmindmap
* Debian
** Ubuntu
*** Linux Mint
*** Kubuntu
*** Lubuntu
*** KDE Neon
** LMDE
** SolydXK
** SteamOS
** Raspbian with a very long name
*** <s>Raspmbc</s> => OSMC
*** <s>Raspyfi</s> => Volumio
@endmindmap
```
````

````{dropdown}  <font color='#84B179'> Príklad: Sekvenčný diagram </font>


    ```{uml}
    :caption: Sekvenčný diagram
    :align: center

      @startuml
      skinparam sequenceMessageAlign right
      Bob -> Alice : Request
      Alice -> Bob : Response
      @enduml
    ```

```{uml}
:caption: Sekvenčný diagram
:align: center

@startuml
skinparam sequenceMessageAlign right
Bob -> Alice : Request
Alice -> Bob : Response
@enduml
```
````

##  <font color='#547792'> Doplnky </font>

### <font color='#E37434'> Lokálne použitie </font>

Pre kreslenie diagramov mimo platformy *Sphinx* vyvoríme v textovom editore zdrojový kód diagramu. Spustením prekladača v konzole vygenerujeme obrázok v predefinovanom formáte *.png, voľba iných formátov ako aj konfigurácie prekladača je popísaná v [dokumentácii](https://plantuml.com/command-line). 

    java -jar ./plantuml/plantuml-1.2026.2jar source.txt 

### <font color='#E37434'> Dokumentácia a rozšírenia</font>

**Domáca stránka programu, dokumentácia a syntax**

* [PlantUML](https://plantuml.com/)

**Sphinx Integrácia**

* [PlantUML for Sphinx](https://github.com/sphinx-contrib/plantuml/)
    
**Doplnky, témy a rozšírenia**

* [plantuml-libs](https://www.npmjs.com/package/@tmorin/plantuml-libs)
* [PlantUML Icon-Font Sprites](https://github.com/tupadr3/plantuml-icon-font-sprites)
* [PlantUML Themes Gallery](https://the-lum.github.io/puml-themes-gallery/)



    
    
