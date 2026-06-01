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

#  <font color='#4B9DA9'> Inštalácia </font>

*Sphinx* je multiplatformová aplikácia vytvorená v jazyku *Python*. Inštalácia pre rôzne platformy je popísaná v [dokumentácii](https://www.sphinx-doc.org/en/master/usage/installation.html). Prehliadanie publikácií vytvorených pomocou *Sphinx* nevyžaduje okrem štandardného www prehliadača inštaláciu doplnkového programového vybavenia. 

##  <font color='#547792'> Linux </font>

Z [Python Package Index](https://pypi.org/project/Sphinx/) (PyPI) pomocou inštalátora **pip** nainštalujeme základnú platformu *Sphinx*, podporu pre *Markdown* ako aj sadu základných užitočných rozšíreni:

    pip install sphinx
    pip install myst-parser
    pip install myst-nb
    pip install sphinx-copybutton
    pip install sphinx-togglebutton
    pip install sphinx-subfigure
    pip install sphinx-design
    
* [myst-parser](https://myst-parser.readthedocs.io/en/latest/) - podpora formátovania textov v *Markdown* na platforme *Sphinx*
* [myst-nb](https://myst-nb.readthedocs.io/en/v0.13.2/index.html) - rozšírenie *myst-parser*, umožňuje priame použitie Jupyter notebookov ako zdrojových textov
* [sphinx-copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/index.html) - pridá do buniek textu formátovaných ako zdrojové kódy ikonu pre skopírovanie obsahu bunky do systémového zápisníka (clipboard)
* [sphinx-togglebutton](https://sphinx-togglebutton.readthedocs.io/en/latest/) - umožňuje skrývanie a rozbalovanie textu v poznámkach a upozorneniach 
* [sphinx-subfigure](https://sphinx-subfigure.readthedocs.io/en/latest/) - umožňuje ukladanie obrázkov do mriežky
* [sphinx-design](https://sphinx-design.readthedocs.io/en/latest/index.html) - rozšírenie pre témy webových grafických rozhraní ako sú kaskádové štýly, expandovateľné kontainery, tlačítka, ikony a ďaľšie. Toto rozšírenie využívajú konfigurovateľné témy grafického rozhrania, ktoré sa inštalujú podľa potreby samostatne:

  * [alabaster](https://alabaster.readthedocs.io/en/latest/)
  * [sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/en/stable/index.html)
  * [pydata-sphinx-theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html)
  * [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/)
  * [furo](https://pradyunsg.me/furo/)

Témy sa inštalujú podľa potreby samostatne:

    pip install alabaster
    pip install sphinx-book-theme
    pip install pydata-sphinx-theme
    pip install sphinx-rtd-theme
    pip install furo
    
V prípade potreby môžeme inštalovať paralelne niekoľko rôznych verzií *Sphinx* a ich konfigurácií vo virtuálnych prostrediach vytvorených pomocou [venv](https://docs.python.org/3/library/venv.html). Aktuálnu verziu *Sphinx* získame pomocou príkazu 

    sphinx-build --version
    
    
##  <font color='#547792'> Windows </font>

*Python* nie je štandardnou súčasťou distribúcie Windows, pre jeho inštaláciu na využite návody dostupné na internete, napríklad [The Hitchhiker’s Guide to Python](https://docs.python-guide.org/). Doporučená verzia pre inštaláciu je *Python3*. Po inštalácii nainštalujte *Sphinx* s príslušenstvom pomocou inštalátora **pip** rovnako ako pri inštalácii pre Linux. 
  
