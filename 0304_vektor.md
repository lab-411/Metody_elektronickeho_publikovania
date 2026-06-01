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

#   <font color='#4B9DA9'> Vektorová grafika </font>

Vektorová grafika reprezentuje obrazovú informáciu pomocou definovaných útvarov ako sú body, priamky, krivky a mnohouholníky. Na platforme *Sphinx* je preferovaným prostredím pre zobrazovanie vektorovej grafiky rozsiahla knižnica makier [PGF/TikZ](https://tikz.dev/). Túto základnú sadu makier je možné rozširovať pomocou knižníc, ktoré sú tématicky zamerané na rôzne typy obrázkov a diagramov ako su napríklad *automata* pre kreslenie diagramov stavových automatov, *circuit* pre elektrické obvody, *3d* pre kreslenie v trojrozmernom priestore a mnohé [ďaľšie](https://tikz.net). Podrobný popis syntaxe makier *PGF/TikZ* je v [dokumentácii](./doc/pgfmanual.pdf). 

V dokumentoch na platforme *Sphinx* môžeme vektorovú grafiku zobrazovať pomocou makier *PGF/TikZ* niekoľkými spôsobmi: 

* Kód jednoduchších obrázkov vytvoríme priamo pomocou makier *TikZ* v zdrojovok texte dokumentu.
* Zdrojový kód obrázku získame vytvorením obrázku niektorom z v lokálnych editoroch podporujúcich syntax makier *TikZ* ako [KtikZ](https://github.com/fhackenberger/ktikz), [TikZitT](https://tikzit.github.io/) alebo v on-line editoroch, napríklad [TikZ Editor](https://app.texpile.com/tools/tikz-editor).
* Vytvorením obrázku v univerzálnych grafických programoch a knižniciach a ich exportom do formátu makier *PGF/TikZ*, napríklad [Inkscape](https://inkscape.org/) a mnohé ďaľšie.
* Konverziou vektorových obrázkov z iných grafických formátov do formátu *PGF/TikZ* pomocou špecializovaných konvertorov   


```{tikz} Obrázok vo formáte *.svg konvertovaný do makier *TikZ*.
:include: ./img/natu0019.tikz
:xscale: 45
```

##  <font color='#547792'> Metódy vkladania vektorových obrázkov </font>

Pre zobrazenie vektorovej grafiky v na platforme *Sphinx* je v tejto publikácii použité rozšírenie [TikZ](https://tikz.dev/), ktoré umožňuje formátovanie vektorových obrázkov v texte dokumentu rovnako ako pri rastrovej grafike (nastavenie veľkosti obrázku a jeho polohy).  

**Inštalácia**

Rozšírenie nainštalujeme pomocou inštalátora **pip**

    pip install sphinxcontrib-tikz
    

**Konfigurácia**

Integrácia programu do platformy *Sphinx* je v súbore *config.py* zaradením do zoznamu *extensions*:

    extensions = [
      ...
      "sphinxcontrib.tikz"
      ...
      ]
 
### <font color='#E37434'>  *{tikz}* </font> 

Direktíva **{tikz}** umožňuje formátovanie obrázku, zaradenie knižníc do prostredia TikZ a vloženie kódu obrázku.  

      ```{tikz} názov
          :libs: zoznam             - zoznam TikZ knižníc
          :xscale: number           - rozmer obrázku v rozsahu 0 ... 100(%)
          :align: pos               - poloha obrázku left, center, right 
          :alt: string              - alternatívny text
          :stringsubst: string  
          
          \usetikzlibrary { ... }   - zoznam knižníc pre prostredie TikZ
          \begin{tikzpicture}       - prostredie
        
          makrá Tikz                - zdrojový text obrázku
          
          \end{tikzpicture}
      ```



Alternatívne môžeme vložiť kód obrázku v makrách *TikZ* z externého súboru:

      ```{tikz} názov
      :include: ./src/test_01.tikz
      :xscale: 25
      ```


```{tikz} Jednoduchý vektorový obrázok 
:xscale: 20

\begin{tikzpicture}
  \draw[shading=ball, ball color=yellow] (0,0) circle [radius=2];
  \draw[shading=ball, ball color=black] (-0.5,0.5,0) ellipse [x radius=0.2, y radius=0.4];
  \draw[shading=ball, ball color=black] (0.5,0.5,0) ellipse [x radius=0.2, y radius=0.4];
  \draw[very thick] (-1,-1) arc [start angle=185, end angle=355,
    x radius=1, y radius=0.5];
\end{tikzpicture}
```
      
      
````{dropdown}  <font color='#84B179'> Zdrojový kód obrázku. </font>

    ```{tikz} Jednoduchý vektorový obrázok  
    :xscale: 35

    \begin{tikzpicture}
      \draw[shading=ball, ball color=yellow] (0,0) circle [radius=2];
      \draw[shading=ball, ball color=black] (-0.5,0.5,0) ellipse [x radius=0.2, y radius=0.4];
      \draw[shading=ball, ball color=black] (0.5,0.5,0) ellipse [x radius=0.2, y radius=0.4];
      \draw[very thick] (-1,-1) arc [start angle=185, end angle=355,
        x radius=1, y radius=0.5];
    \end{tikzpicture}
    ```
    
````


```{tikz} Použitie knižnice pre kreslenie diagramov.
:xscale: 35

\usetikzlibrary {arrows.meta,trees}
\begin{tikzpicture}
  [edge from parent fork down, sibling distance=25mm, level distance=15mm,
   every node/.style={fill=red!30,rounded corners},
   edge from parent/.style={red,-{Circle[open]},thick,draw}]
  \node {root}
      child {node {left}}
      child {node {right}
        child {node {child-left}}
        child {node {child-right}}
      };
\end{tikzpicture}
```

````{dropdown}  <font color='#84B179'> Zdrojový kód obrázku. </font>

    ```{tikz} Použitie knižnice pre kreslenie diagramov.
    :xscale: 35

    \usetikzlibrary {arrows.meta,trees}
    \begin{tikzpicture}
      [edge from parent fork down, sibling distance=25mm, level distance=15mm,
      every node/.style={fill=red!30,rounded corners},
      edge from parent/.style={red,-{Circle[open]},thick,draw}]
      \node {root}
          child {node {left}}
          child {node {right}
            child {node {child-left}}
            child {node {child-right}}
          };
    \end{tikzpicture}
    ```

    

````

```{admonition} Referencie na obrazky     
  :class: note  
  
   V aktuálnej verzii rozšírenia *TikZ* nie je možné definovať referencia na vektorové obrázky pomocou parametra `name`. Na obrázky sa ale dá v texte odkazovať pomocou krížových referencií v tvare
   
      V tomto texte sa odkazujeme na [](obrazok).
      
      (obrazok)=
      ```{tikz} popis obrazku
          :include: ./img/file.tikz
          :xscale: 45
      ```
```


##  <font color='#547792'> Doplnky </font>

### <font color='#E37434'> Lokálne použitie *TickZ* </font>

Pre kreslenie vektorových obrázkov pomocou makier *TickZ* mimo platformy *Sphinx* môžeme využiť niektorý z lokálne inštalovaných editorov, napríklad [KtikZ](https://github.com/fhackenberger/ktikz) alebo online editorov, napríklad [TikZ Editor](https://app.texpile.com/tools/tikz-editor).  

```{figure} ./img/ktikz_editor.png
:width: 650px
:name: img_0304c

Prostredie editora makier KitkZ. 
```

### <font color='#E37434'> Import obrázkov vo formáte *svg* </font>

Formát [SVG](https://www.wikiwand.com/en/SVG) nie je štandardne na platforme *Sphinx* podporovaný. Obrázky vo formáte SVG môžeme ale konvertovať do formáty TikZ konvertovať pomocou programu [svg2tikz](https://github.com/xyz2tex/svg2tikz), ktorý je voliteľným doplnkom grafického editora [Inkscape](https://inkscape.org/), môže byť ale použitý aj samostatne ako konzolová aplikácia. 

Inštalácia programu je pomocou inštalátora **pip**

    pip install svg2tikz
    
Parametre programu získame príkazom `svg2tikz --help`, príklad použitia programu pre konverziu obrázkov

    svg2tikz --figonly input_file.svg --output output_file.tikz

````{dropdown}  <font color='#84B179'> Príklad konverzie obrázku vo formáte SVG </font>

Konverzia obrázku

    svg2tikz --figonly ./img/cart0157.svg --output ./img/cart0157.tikz
    
Zobrazenie obrázku 


    ```{tikz} Konvertovaný obrázok
    :include: ./img/cart0157.tikz
    :xscale: 20
    ```
  
```{tikz} Konvertovaný obrázok
:include: ./img/cart0157.tikz
:xscale: 20
```

````
    
### <font color='#E37434'> Dokumentácia a odkazy </font>

**Knižnica makie TikZ**

* [The TikZ and PGF Packages](https://tikz.dev/)

**TikZ Sphinx Integrácia**

* [sphinxcontrib-tikz](https://sphinxcontrib-tikz.readthedocs.io/en/latest/)

**Galérie príkladov**

* [LaTeX and TikZ examples](https://texample.net/)
* [Awesome TikZ](https://github.com/ShuhongDai/tikz-examples)
* [Tikz-Graphics](https://github.com/alextsagkas/Tikz-Graphics#tikz-graphics)










