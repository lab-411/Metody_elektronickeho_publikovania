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

#   <font color='#4B9DA9'> Orientované grafy </font>

##  <font color='#547792'> Graphviz </font>

[Graphviz](https://graphviz.org/) (skratka od *Graph Visualization Software*) je open-source program pre vizualizáciu diagramov založených na orientovaných grafoch zadaných pomocou grafického jazyka [DOT](https://cs.wikipedia.org/wiki/DOT_(grafick%C3%BD_jazyk)). Vývoj programu začal v roku 1991 v [AT&T Laboratories, Inc.](https://en.wikipedia.org/wiki/AT%26T_Labs) a do súčasnej doby bol integrovaný do množstva aplikácií a projektov. 

```{graphviz}
        :caption: Orientovaný graf, [zdrojový kód](https://graphviz.org/Gallery/directed/unix.html)
        :align: center

/* courtesy Ian Darwin and Geoff Collyer, Softquad Inc. */
digraph unix {
    size = 7;
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]
	node [color=lightblue2, style=filled];
	"5th Edition" -> "6th Edition";
	"5th Edition" -> "PWB 1.0";
	"6th Edition" -> "LSX";
	"6th Edition" -> "1 BSD";
	"6th Edition" -> "Mini Unix";
	"6th Edition" -> "Wollongong";
	"6th Edition" -> "Interdata";
	"Interdata" -> "Unix/TS 3.0";
	"Interdata" -> "PWB 2.0";
	"Interdata" -> "7th Edition";
	"7th Edition" -> "8th Edition";
	"7th Edition" -> "32V";
	"7th Edition" -> "V7M";
	"7th Edition" -> "Ultrix-11";
	"7th Edition" -> "Xenix";
	"7th Edition" -> "UniPlus+";
	"V7M" -> "Ultrix-11";
	"8th Edition" -> "9th Edition";
	"1 BSD" -> "2 BSD";
	"2 BSD" -> "2.8 BSD";
	"2.8 BSD" -> "Ultrix-11";
	"2.8 BSD" -> "2.9 BSD";
	"32V" -> "3 BSD";
	"3 BSD" -> "4 BSD";
	"4 BSD" -> "4.1 BSD";
	"4.1 BSD" -> "4.2 BSD";
	"4.1 BSD" -> "2.8 BSD";
	"4.1 BSD" -> "8th Edition";
	"4.2 BSD" -> "4.3 BSD";
	"4.2 BSD" -> "Ultrix-32";
	"PWB 1.0" -> "PWB 1.2";
	"PWB 1.0" -> "USG 1.0";
	"PWB 1.2" -> "PWB 2.0";
	"USG 1.0" -> "CB Unix 1";
	"USG 1.0" -> "USG 2.0";
	"CB Unix 1" -> "CB Unix 2";
	"CB Unix 2" -> "CB Unix 3";
	"CB Unix 3" -> "Unix/TS++";
	"CB Unix 3" -> "PDP-11 Sys V";
	"USG 2.0" -> "USG 3.0";
	"USG 3.0" -> "Unix/TS 3.0";
	"PWB 2.0" -> "Unix/TS 3.0";
	"Unix/TS 1.0" -> "Unix/TS 3.0";
	"Unix/TS 3.0" -> "TS 4.0";
	"Unix/TS++" -> "TS 4.0";
	"CB Unix 3" -> "TS 4.0";
	"TS 4.0" -> "System V.0";
	"System V.0" -> "System V.2";
	"System V.2" -> "System V.3";
}

```

**Inštalácia**

Program je súčasťou štandardných repozitárov.

    sudo apt install graphviz
    

**Konfigurácia**

Rozhranie k programu je súčasťou distribúcie platformy *Sphinx*. Integrácia programu do platformy *Sphinx* je v súbore *config.py* zaradením do zoznamu *extensions*:

    extensions = [
      ...
      "sphinx.ext.graphviz"
      ...
      ]
    
### <font color='#E37434'> *{graphviz}* </font>
    
Atribúty direktívy **{graphviz}** sú v popísané v [dokumentácii](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html). Velkosť grafu určená parametrom *size* v zdrojovom texte grafu.

    ```{graphviz}
      :alt: string                - alternatívny text
      :layout: string             - format grafu - dot, neato, circo ...
      :name: string               - referencia
      :align: position            - poloha diagramu center, left, right
        
      zdrojovy text grafu
    ```



````{dropdown}  <font color='#84B179'> Príklad: Jednoduchý diagram </font>

    ```{graphviz}
        :caption: Jednoduchý orientovaný graf
        :align: center
        
      digraph test {
      a -> b;
      a -> c;
      b -> d;
      b -> e;
      c -> f;
      c -> g;
      }
    ```


```{graphviz}
    :caption: Jednoduchý orientovaný graf
    :align: center
   digraph test {
      a -> b;
      a -> c;
      b -> d;
      b -> e;
      c -> f;
      c -> g;
      }

```
````

````{dropdown}  <font color='#84B179'> Príklad: Diagram farieb </font>

    ```{graphviz}
    :caption: Diagram farieb
    :align: center
    
    digraph Farby {
        label = " "
        labelloc = "b"
        layout = neato
        size = 4.5
        fontname = Arial
        node [
            shape = ellipse
            width = 1
            color="#00000088"
            style = filled
            fontname="Helvetica,Arial,sans-serif"
        ]

        edge [len = 1.75 penwidth = 2.5 arrowhead=open]
        start = regular
        normalize = 0

        green       [fillcolor = green        fontcolor = white]
        white       [fillcolor = white      ]
        blue        [fillcolor = blue         fontcolor = white]
        red         [fillcolor = red          fontcolor = white]
        yellow      [fillcolor = yellow     ]
        cyan        [fillcolor = cyan       ]
        magenta     [fillcolor = magenta      fontcolor = white]
        deepskyblue [fillcolor = deepskyblue]
        orange      [fillcolor = orange     ]
        yellowgreen [fillcolor = yellowgreen]
        deeppink    [fillcolor = deeppink     fontcolor = white]
        purple      [fillcolor = purple       fontcolor = white]
        springgreen [fillcolor = springgreen]

        green   -> {white yellow cyan yellowgreen springgreen} [color = green  ]
        red     -> {white yellow magenta orange deeppink }     [color = red    ]
        yellow  -> {orange yellowgreen}                        [color = yellow ]
        blue    -> {white cyan magenta deepskyblue purple}     [color = blue   ]
        cyan    -> {springgreen deepskyblue}                   [color = cyan   ]
        magenta -> {deeppink purple}                           [color = magenta]
    }
    ```


```{graphviz}
    :caption: Diagram farieb
    :align: center
    :layout: neato
    
digraph Farby {
	label = " "
	labelloc = "b"
	fontname = Arial
	size = 4.5
	node [
		shape = ellipse
		width = 1
		color="#00000088"
		style = filled
		fontname="Helvetica,Arial,sans-serif"
	]

	edge [len = 1.75 penwidth = 2.5 arrowhead=open]
	start = regular
	normalize = 0

	green       [fillcolor = green        fontcolor = white]
	white       [fillcolor = white      ]
	blue        [fillcolor = blue         fontcolor = white]
	red         [fillcolor = red          fontcolor = white]
	yellow      [fillcolor = yellow     ]
	cyan        [fillcolor = cyan       ]
	magenta     [fillcolor = magenta      fontcolor = white]
	deepskyblue [fillcolor = deepskyblue]
	orange      [fillcolor = orange     ]
	yellowgreen [fillcolor = yellowgreen]
	deeppink    [fillcolor = deeppink     fontcolor = white]
	purple      [fillcolor = purple       fontcolor = white]
	springgreen [fillcolor = springgreen]

	green   -> {white yellow cyan yellowgreen springgreen} [color = green  ]
	red     -> {white yellow magenta orange deeppink }     [color = red    ]
	yellow  -> {orange yellowgreen}                        [color = yellow ]
	blue    -> {white cyan magenta deepskyblue purple}     [color = blue   ]
	cyan    -> {springgreen deepskyblue}                   [color = cyan   ]
	magenta -> {deeppink purple}                           [color = magenta]

}

```
````

##  <font color='#547792'> Doplnky </font>

### <font color='#E37434'> Lokálne použitie </font>

Pre kreslenie grafov mimo platformy *Sphinx* vyvoríme v textovom editore zdrojový kód grafu. Spustením prekladača v konzole vygenerujeme grafu do zvoleného formátu (parameter T): 

    dot -Tpng input_file.txt -o output_file.png

### <font color='#E37434'> Dokumentácia a rozšírenia</font>

**Domáca stránka, dokumentácia, syntax**

* [Graphviz](https://graphviz.org/)
* [Graphviz Python API](https://graphviz.readthedocs.io/en/stable/)

**Sphinx Integrácia**

* [Add Graphviz graphs](https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html)

**Galérie príkladov**

* [Graphviz (dot) examples](https://renenyffenegger.ch/notes/tools/Graphviz/examples/index)
* [Practical Guide to DOT Language](https://www.danieleteti.it/post/dot-language-guide-for-devs-and-analysts-en/)


**Online editory**

* [Graphviz Visual Editor](https://magjac.com/graphviz-visual-editor/)

