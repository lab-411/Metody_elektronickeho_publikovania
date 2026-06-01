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

# <font color='#4B9DA9'> Elektronické publikácie </font>

Elektronické publikovanie je proces vytvárania distribúcie a prístupu k obsahu v digitálnej forme, na rozdiel od klasických tlačových formátov. Zahŕňa množstvo foriem, ako sú e-knihy, články, časopisy, www stránky, interaktívne publikácie a mnohé ďaľšie. Pre distribúciu elektronických publikácií sú využívané rôzne komunikačné technológie, ktorých účelom je dopraviť obsah do koncových zariadení uživateľov, ktorými sú zvyčajne počítače, čitačky a smartfóny.   

Pod pojmom elektronická publikácia sme si donedávna najčastejšie predstavili dokument vo formáte *pdf*. Rozvoj internetu a jeho infraštruktúry, dostupnosť, rýchlosť ako aj nárast výkonu koncových zariadení umožňujú šírenie a zdieľanie informácií modernými metódami, ktoré sa odlišujú od klasického statického zdieľanie dokumentov. Publikácie môžu obsahovať formátované texty, klasickú hypertextovú štruktúru, interaktívne komponenty, multimediálne prvky a kombinovať text s výstupmi z iných programov a systémov. Elektronické dokumenty s interaktívnymi a multimediálnymi prvkami sa stávajú dôležitou časťou vzdelávacieho procesu zameraného na individuálne vzdelávania a samoštúdium prostredníctvom digitálnych učebníc, e-learningových vzdelávacích modulov a tréningových manuálov. 

##  <font color='#547792'> Požiadavky </font>

Táto publikácia je primárne zameraná na tvorbu vzdelávacích a technicky zameraných elektronických interaktívnych kníh. Pre tvorbu publikáciu potrebujeme publikačnú platformu, čo je zvyčajne súbor programových nástrojov, knižníc a pomôcok, ktorých výstupom je kompaktné dielo, ktoré spĺňa požiadavky na elektronickú publikáciu.   

Pre tvorbu elektronických publikácií existuje v súčasnej dobe množstvo platforiem, komerčných, ako aj z oblasti open source. Pri výbere platformy pre tvorbu elektronických publikácií z oblasti vedy, techniky a vzdelávania boli zohľadňované nasledujúce kritéria:

* open-source multiplatformové prostredie, voľne dostupné bez licenčných poplatkov a predplatného 
* jednoduchá editácia a vytváranie textov 
* zadávanie matematických výrazov v štandardnom formáte LaTeX
* tvorba in-line grafov, diagramov a schém
* dostupná dokumentácia, návody a príklady použitia
* možnosti rozširovania a úpravy vlastností platformy a voľby grafickej reprezentácie publikácií 
* možnosť integrácia programovacieho jazyka, typicky Python
* možnosť prehliadania publikácie v off-line móde
* možnosť využitia prvkov značkovacieho jazyka HTML pre forrmátovanie textu

Na základe vyššie uvedených kritérií bola pre túto publikáciu vybraná platforma založená na dokumentačnom systéme [Sphinx](0010_sphinx). V závislosti od účelu použitia je na internete voľne dostupných niekoľko ďaľších platforiem vhodných na tvorbu elektronických publikácií. 

### <font color='#E37434'> Jupyter </font>

[Jupyter Lab](https://jupyter.org/) je populárnou platformou pre tvorbu interaktívnych učebných textov vo forme notebookov kombinujucich text, matematické vzťahy a obrázky s interaktívnymi prvkami ako sú časti kódov v prgramovacích jazykoch vykonávaných priamo v prostredí dokumentu, ako aj interaktívne ovládacie prvky. Je ideálnou platformou pre učebné texty, kde je možné kombinovať teóriu s praktickým overením poznatkov. Platforma vyžaduje lokálny alebo vzdialený server, uživateľské rozhranie pre prostredie pre tvorbu dokumentov a ich používanie je www prehliadač. V rámci platformy je možné notebooky konvertovať do publikácií vo forme kníh pomocou [Jupyter Book](https://jupyterbook.org/).     

```{figure} ./img/jupyter_demo.png
:width: 600px
Stránka zápisníka v prostredí Jupyter Lab.
```

### <font color='#E37434'> SageMath </font>

[SageMath](https://www.sagemath.org/) využíva podobný koncept klient-server ako *Jupyter Lab*, je ale špecializovaná na oblasť matematiky od elementárnej až po pokročilú. Prostredie integruje množstvo knižníc z oblasti základov, lineárnej algebry, numerických metód, kryptografia, kombinatoriky, teórie grafov, teórie grúp, symbolických manipulácií a mnohé ďaľšie. Podobne ako *Jupyter Lab* platforma vyžaduje lokálny alebo vzdialený server, v prostredí www prehliadača je možné vytvárať dokumenty kombinujuce matematické texty s interaktívnymi prvkami a grafikou.

```{figure} ./img/sage_demo.png
:width: 600px
Interaktívny shell v prostredí SageMath.
```
  
