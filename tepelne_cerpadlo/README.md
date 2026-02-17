Obsah súborov
1. COP.py
Účel: Výpočet okamžitého koeficientu účinnosti (COP).

Logika: Využíva kalorimetrickú rovnicu na výpočet tepelného výkonu z prietoku a rozdielu teplôt (Delta T) a následne ho porovnáva s elektrickým príkonom.

Funkcie: Obsahuje softvérový "clamping" (ohraničenie hodnôt 0-8) a filtráciu pri nízkom príkone pod 200W.

2. Defrost_count.py
Účel: Inteligentné počítadlo odmrazovacích cyklov.

Logika: Započítava defrost len v prípade, že je potvrdený fyzikálnymi veličinami (záporná Delta T a aktívny kompresor) a trvá dlhšie ako 90 sekúnd.

Prínos: Eliminuje falošné detekcie a pomáha sledovať efektivitu stroja pri nízkych vonkajších teplotách.

3. Kompresor_count.py
Účel: Sledovanie počtu štartov a cyklovania kompresora.

Logika: Reaguje na binárny senzor prevádzky, ktorý využíva 10-minútový filter (delay_off) na odfiltrovanie krátkodobých technologických prestávok.

Prínos: Kľúčový ukazovateľ pre diagnostiku správneho nadimenzovania systému a ochranu životnosti kompresora.

4. Tepelna_strata_domu.py
Účel: Výpočet okamžitej tepelnej straty objektu vo Wattoch.

Logika: Pracuje s koeficientom prestupu tepla (H) a rozdielom medzi vonkajšou teplotou a priemerom z viacerých vnútorných senzorov.

Prínos: Umožňuje porovnať reálnu stratu domu s výkonom, ktorý dodáva kúrenie.

Inštalácia
Skripty sú určené pre integráciu PyScript v Home Assistante.

Skopírujte .py súbory do priečinka /config/pyscript/.

Skontrolujte názvy svojich entít v Home Assistante, aby sedeli s premennými v skriptoch.

Reloadnite PyScript integráciu.
