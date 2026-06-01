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

#   <font color='#4B9DA9'> Matematické výrazy </font>

Platforma *Sphinx* využíva pre vkladanie matematickych výrazov do textu typografický systém [LaTeX](https://en.wikibooks.org/wiki/LaTeX/Mathematics). V matematickom móde môžeme využívať všetky vlastnosti a možnosti typografického systému.

\begin{align}
\nabla \cdot \mathbf{E} \,\,\, &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \mathbf{B} \,\,\, &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \left(\mathbf{J} + \varepsilon_0  \frac{\partial \mathbf{E}}{\partial t} \right)
\end{align}

##  <font color='#547792'> Vkladanie výrazov </font>

Matematické výrazy je možné do textu dokumentu vložiť niekoľkými spôsobmi, použitím direktívy **{math}**, zjednodušeným postupom pomocou znakov `\$` ako aj primym vložením matematických výrazov formátovaných v typografickom systéme LaTeX.

### <font color='#E37434'> *{math}* </font>

Direktíva **{math}** je určený pre písanie rovníc alebo sústav rovníc. Je ekvivalentom príkazu **align** v systéme LaTeX. Rovnice sú oddelené znakmi ```\\``` a vzájomne zarovnané znakom ```&```.   V in-line texte môžeme zadať matematický výraz pomocou role``` {math}`vyraz` ```.

**Formát direktívy**

      ```{math}
      :label: ref         - referencia  
         equ_1 \\         - matematické vzťahy vo formáte LaTeX
         equ_2 \\
         ...
      ```
      
Na sústavu rovníc sa môžeme odkazovať pomocou referencie v tvare role ```{eq}`ref` ```. 

       
:::{dropdown}  <font color='#84B179'> Použitie direktívy {math} </font>

      Vzťah medzi amplitúdou {math}`A`, fázou {math}`\phi` 
      a zložkami {math}`I` a {math}`Q` popisuje vzťah {eq}`ref1`:
      
      ```{math}
      :label: ref1
         A &= \sqrt{I^2 + Q^2} \\
      \phi &= \arctan{\frac{Q}{I}}
      ```


Vzťah medzi amplitúdou {math}`A`, fázou {math}`\phi` a zložkami {math}`I` a {math}`Q` popisuje vzťah {eq}`ref1`:
      
```{math}
:label: ref1
A &= \sqrt{I^2 + Q^2} \\
\phi &= \arctan{\frac{Q}{I}}
``` 
:::


### <font color='#E37434'> *dollarmath* </font>

*Markdown* rozšírenie [dollarmath](0014_sphinx_predloha.md) umožňuje jednoduché zadávanie matematických výrazov v texte pomocou reťazca ```$ výraz $``` a sústavy rovníc vzájomne zarovnaných znakom ```&``` v tvare:

      $$
         equ_1 \\
         equ_2 \\
         ...
      $$(referencia)
      
Na sústavu rovníc sa môžeme odkazovať podobne ako v direktíve *{math}* pomocou referencie v tvare ```{eq}`referencia` ```.

```{dropdown}  <font color='#84B179'> Použitie rozšírenia \$ ...\$ a \$\$ ... \$\$ </font>

      Vzťah medzi aplitúdou $A$, fázou $\phi$ a zložkami $I$ a $Q4 
      popisuje vzťah {eq}`amp_phase`:
      
      $$
         A &= \sqrt{I^2 + Q^2} \\
      \phi &= \arctan{\frac{Q}{I}}
      $$(ref2)


Vzťah medzi amplitúdou $A$, fázou $\phi$ a zložkami $I$ a $Q$ popisuje vzťah {eq}`ref2`:
      
$$
A &= \sqrt{I^2 + Q^2} \\
\phi &= \arctan{\frac{Q}{I}}
$$(ref2)

```

### <font color='#E37434'> *amsmath* </font>

*Markdown* rozšírenie [amsmath](0014_sphinx_predloha.md) umožňuje zadávať matematické výrazy pomocou syntaxe LaTeX s využitím jeho prostredí *equation, cases, multiline, gather, align, alignat, flalign, matrix, pmatrix, bmatrix, Bmatrix, vmatrix, Vmatrix, eqnarray*, Podrobný popis vlastností rozšírenia je v [dokumentácii](./doc/amsldoc.pdf).

      \begin{equation} 
         y =  f(a)+\frac {f'(a)}{1!} (x-a) + 
          \frac{f''(a)}{2!} (x-a)^2 + \
          \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots
      \end{equation}
      

\begin{equation} 
  f(a)+\frac {f'(a)}{1!} (x-a) + 
  \frac{f''(a)}{2!} (x-a)^2 + \
  \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots
\end{equation}      

```{admonition} Poznámka
:class: note
K rovniciam v tomto rozšíreni je možné priradiť poradové číslo rovnici podľa syntaxe LaTeX, priradenie referencie pomocou `\label{eq:...}` nie v aktuálnej verzii *Sphinx* rozpoznávané a preto nie možné sa na toto poradové číslo odkazovať pomocou príkazu `{eg}...`.

      \begin{equation} 
      \label{eq:...}
      
      \end{equation}

```

### <font color='#E37434'> *display* </font>

Rozšírenie *myst-nb* umožňuje použitie knižníc Jupyteru pre interpretáciu kódy ako buniek notebooku. Interpretovaný text je automaticky pokladaný za popis v matematickom móde. 


```{code-cell} ipython
from IPython.display import Latex
Latex(r"""
      \text{Riešenie rovnice  } \,\,
      x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
""")
```

Ak nechceme v texte zobraziť bunku so zdrojovým kódom, je potrebné doplniť do bloku parameter **:tags: ["remove-cell"]**.


##  <font color='#547792'> Úpravy  </font>

### <font color='#E37434'> *Farby* </font>

Pre zobrazenie matematických vzťahov vo farbe, celých alebo len ich častí, môžeme použiť LaTeX prostredie [xcolor](./doc/xcolor.pdf), ktoré aktivujeme zaradením do kompilácie matematických výrazov  pomocou slovníka **latex_elements = { ... }** do súboru [conf.py](./conf.py) 

      latex_elements = {
            ...
            'extrapackages': r'\usepackage{xcolor}',
            ...
      }

      
Farebné zvýraznenie potom dosiahneme použitím príkazu **\color{...}** v zadaní matematického výrazu 

      \begin{equation} 
          y = f(a) + \
          \color{blue}  \frac {f'(a)}{1!} (x-a) + 
          \color{green} \frac{f''(a)}{2!} (x-a)^2 + \
          \color{red}   \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots
      \end{equation} 
      

\begin{equation} 
y = f(a)+\color{blue} + \frac {f'(a)}{1!} (x-a) + 
\color{green} \frac{f''(a)}{2!} (x-a)^2 + \
\color{red}  \frac{f^{(3)}(a)}{3!}(x-a)^3 + \cdots
\end{equation} 

### <font color='#E37434'> *Rámiky* </font>

Pomocou LaTeX prostredia [fbox](./doc/fbox.pdf) môžeme vykresliť matematické vzťahy v rámiku. Prostredie je potrebné aktivovať v súbore [conf.py](./conf.py). 

      latex_elements = {
            ...
            'extrapackages': r'\usepackage{fbox}',
            ...
      }

Argumentom prostredia **\fbox{...}** je textový reťazec, pre matematické vťahy musíme použiť dolárovú konvenciu 

      \begin{equation*}
          \fbox{
               $\color{red} q = \sqrt{\sin(\alpha^2) + \cos(\beta^2)}$
          }
      \end{equation*}


\begin{equation*}
\fbox{
      $\color{red} q = \sqrt{\sin(\alpha^2) + \cos(\beta^2)}$
      }
\end{equation*}


