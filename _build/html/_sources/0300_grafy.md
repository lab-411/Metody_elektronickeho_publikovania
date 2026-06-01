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

#   <font color='#4B9DA9'> Vizualizácia dát </font>

Zobrazenie numerických údajov v grafickej forme je dôležitým krokom pri analýze, spracovaní a interpretácií dát. Správne zvolená forma grafického zobrazenie môže zobraziť vzťahy a javy, ktoré nemusia byť pri zobrazení v číselnej forme zjavné. Pre prevod numerických dát do grafickej formy existuje veľa programových prostriedkov, od univerzálnych prostredí a knižníc po špecializované a tématicky zamerané systémy. V prostredí *Sphinx* môžeme jednoduchšie grafy vytvárať priamo v texte dokumentu pomocou makier *pgfplots*, pre komplikovanejšie grafy môžeme použiť programové prostriedky, ktoré umožňujú export do vhodného bitového alebo vektorového formátu. 

##  <font color='#547792'> *pgfplots* </font>

[pgfplots](https://github.com/pgf-tikz/pgfplots) je nadstavbou knižnice makier *PGF/TikZ* pre kreslenie grafov. Knižnica obsahuje makrá pre kreslenie grafov, ktoré značne uľahčujú prácu so samotnou knižnicou *TikZ*.  Ku knižnici je dostupná rozsiahla [dokumentácia](./doc/pgfplots.pdf) ako aj množstvo príkladov použitia v on-line [galériách](https://pgfplots.sourceforge.net/gallery.html).

**Inštalácia**

Knižnica *pgfplots* je súčasťiu distribúcie *LaTeX* a do prostredia *Sphinx* ju zaradíme ako doplnkový balík pre *LaTeX* v súbore *config.py* v slovníku *latex_elements*  

    latex_elements = {
      ...
      'extrapackages': r'\usepackage{pgfplots}',
      ...
    }


```{tikz}
\begin{tikzpicture}

  \pgfplotsset{
    small/.style={
    width=7.0cm,
    height=,
    tick label style={font=\scriptsize},
    label style={font=\scriptsize},
    legend style={font=\scriptsize},
    title style={font=\scriptsize},
    max space between ticks=25,
    },
  }

    \begin{axis}[
    small,
    title=Grafy trigionometrických funkcií,
        axis lines = left,
        xlabel = $x$,
        ylabel = $f(x)$,
            ymajorgrids=true,
            xmajorgrids=true,
        grid style=dashed,
        
        legend style={
          cells={anchor=west},
        legend pos=south east,
      },
    ]

        \addplot [
            domain=-10:10, 
            samples=100, 
            color=blue,
            ]
            {sin(deg(x))};
        \addlegendentry{ $sin(x)$ }

        \addplot [
            domain=-10:10, 
            samples=100, 
            color=red,
            ]
            {cos(deg(x))};
        \addlegendentry{ $cos(x)$ }

        \addplot [
            domain=-10:10,  
            samples=100, 
            color=cyan,
            ]
            {pow(sin(deg(x)),2)};
         \addlegendentry{ $sin(x)^2$  } 

    \end{axis}
\end{tikzpicture}
```

````{dropdown}  <font color='#84B179'> Zdrojový kód obrázku </font>

    ```{tikz}
    \begin{tikzpicture}

      \pgfplotsset{
          small/.style={                            % nastavenie formatovania grafu
          width=7.0cm,                              % sirka
          height=,                                  % vyska  - automaticky
          tick label style={font=\scriptsize},      % velkost pisma na osiach 
          label style={font=\footnotesize},         % velkost pisma popisu osi 
          legend style={font=\scriptsize},          % velkost pisma legendy
          title style={font=\scriptsize},           % velkost pisma nadpisu grafu
          max space between ticks=25,               % hustota mriezky grafu            
          },
      }

      \begin{axis}[                                 % nastavenie parametrov osi a obsahu grafu
          small,                                    % vyber formatovania grafu
          title=Grafy trigionometrických funkcií,   % nadpis grafu 
            axis lines = left,                      % poloha osi
            xlabel = $x$,                           % popis osi
            ylabel = $f(x)$,
                ymajorgrids=true,                   % zobrazenie mriezky pre osi
                xmajorgrids=true,
            grid style=dashed,                      % typ mriezky
            
            legend style={                          % formatovanie legendy
                cells={anchor=west},                % umiestnenie textu v legende
                legend pos=south east,              % umiestnenie legendy v grafe
            },
        ]

        \addplot [                                  % zobrazenie funkcie na grafe
            domain=-10:10,                          % rozsah hodnot premennej funkcie
            samples=100,                            % pocet vzoriek
            color=blue,                             % farba
          ]
          { sin(deg(x)) };                          % definicia funkcie 
          \addlegendentry{ $sin(x)$ }               % pridanie do legendy s textom

        \addplot [
            domain=-10:10, 
            samples=100, 
            color=red,
          ]
          {cos(deg(x))};
          \addlegendentry{ $cos(x)$ }

        \addplot [
            domain=-10:10,  
            samples=100, 
            color=cyan,
          ]
          {pow(sin(deg(x)),2)};
          \addlegendentry{ $sin(x)^2$  } 

      \end{axis}                                    % koniec bloku
    \end{tikzpicture}                               % koniec prostredia
    ```
````

##  <font color='#547792'> *matplotlib* </font>

Pre vkladanie grafov do prostredia *Sphinx* môžeme použiť populárnu knižnicu [matplotlib](https://matplotlib.org/) pre jazyk Python. Výstup grafov môžeme realizovať pomocou exportu do rastrového obrázku alebo do makier *TikZ*.


### <font color='#E37434'> Export grafu do formátu *png* </font>

     
```{code-cell} ipython3  
:tags: ["remove-cell"]

from numpy import *
import pylab as plt
plt.rcParams['figure.dpi'] = 300
plt.style.use("ggplot")

T = linspace(0, 5*pi*2, 1000)     # 2*pi*t

m  = 0.5
A0 = 1
ct = A0*(1 + m*cos(T))     # modulacny signal
am = ct * cos(10*T)        # amplitudova modulacia

plt.plot(T, am)
plt.plot(T, ct, 'k--')
plt.plot(T,-ct, 'k--')
plt.title(r'Modulačný činiteľ ' + str(m))
plt.grid()
plt.xlabel('t')
plt.ylabel('AM')

plt.savefig('am_signal.png', dpi=300)
plt.close()

```

```{figure} am_signal.png
:width: 500px
:name: sig_01

Graf vytvorený v knižnici *matplotlib*,
```


````{dropdown}  <font color='#84B179'> Zdrojový kód obrázku </font>

Doplnením do zdrojového kódu grafu uložíme graf ako rastrový obrázok. 

```{code-block} python
from numpy import *
import pylab as plt
plt.rcParams['figure.dpi'] = 300
plt.style.use("ggplot")

T = linspace(0, 5*pi*2, 1000)     # 2*pi*t

m  = 0.5
A0 = 1
ct = A0*(1 + m*cos(T))     # modulacny signal
am = ct * cos(10*T)        # amplitudova modulacia

plt.plot(T, am)
plt.plot(T, ct, 'k--')
plt.plot(T,-ct, 'k--')
plt.title(r'Modulačný činiteľ ' + str(m))
plt.grid()
plt.xlabel('t')
plt.ylabel('AM')
plt.savefig('am_signal.png', dpi=300)
plt.close()
```

Vygenerovaný obrázok zobrazíme pomocou direktívy {figure}. Na obrázok sa môžeme odkazovať referenciou.

    ```{figure} am_signal.png
    :width: 600px
    :name: sig_01

    Graf vytvorený v knižnici *matplotlib*.
    ```
````

### <font color='#E37434'> Export grafu do formátu *TikZ* </font>

```{code-cell} ipython3  
:tags: ["remove-cell"]

from numpy import *
import pylab as plt
plt.rcParams['figure.dpi'] = 300
plt.style.use("ggplot")

T = linspace(0, 5*pi*2, 1000)     # 2*pi*t

m  = 0.5
A0 = 1
ct = A0*(1 + m*cos(T))     # modulacny signal
am = ct * cos(10*T)        # amplitudova modulacia

plt.plot(T, am, 'b')
plt.plot(T, ct, 'k--')
plt.plot(T,-ct, 'k--')
plt.title(r'Modulačný činiteľ ' + str(m))
plt.grid()
plt.xlabel('t')
plt.ylabel('AM')

import matplot2tikz
matplot2tikz.clean_figure()
matplot2tikz.save("./py/am_signal.tex")

plt.close()

```


```{tikz} Graf vytvorený v knižnici *matplotlib*
  :include: ./py/am_signal.tex
  :xscale: 65
```



````{dropdown}  <font color='#84B179'> Export grafu do formátu do makier *TikZ* </font>


**Inštalácia**

Pre export do makier *TikZ* musíme doinštalovať pomocnú knižnicu *matplot2tikz*

     pip install matplot2tikz
     
     
Doplnením do zdrojového kódu grafu uložíme graf do makier *TikZ* 

```{code-block} python
import matplot2tikz
matplot2tikz.clean_figure()
matplot2tikz.save(" am_signal.tex")
```

Vygenerovaný obrázok zobrazíme pomocou direktívy {tikz}.

    ```{tikz} Graf vytvorený v knižnici *matplotlib*
      :include: ./py/test.tex
      :xscale: 75
    ```
````


### <font color='#E37434'> Dokumentácia a rozšírenia </font>

* https://lpn-doc-sphinx-primer.readthedocs.io/en/latest/concepts.html
* https://lpn-doc-sphinx-primer.readthedocs.io/en/latest/extensions/matplotlib.html
* https://lpn-doc-sphinx-primer.readthedocs.io/en/latest/extensions/tikz/tikztiming.html

  
**Galéria PGFPlots**

* [PGFPlots Gallery](https://pgfplots.sourceforge.net/gallery.html)

* https://www.overleaf.com/learn/latex/Pgfplots_package






  
