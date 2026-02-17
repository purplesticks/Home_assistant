# Smart Home Automation: Riadenie rekuperácie (Python)

Tento projekt demonštruje prepis domácej automatizácie z YAML do jazyka **Python**. Cieľom bolo sprehľadniť logiku rozhodovania pri vetraní na základe kvality vzduchu a vonkajších podmienok.

## Čo tento program rieši?
Program automaticky vypína rekuperačnú jednotku v momente, keď je v dome čerstvý vzduch s cieľom znížiť spotrebu rekuperície a žnížiť opotrebenie filtrov. 

### Hlavné funkcie:
- **Sledovanie CO2:** Reaguje na pokles pod 550 ppm pomocou `state_trigger`.
- **Inteligentné podmienky:** Kontroluje, či je vonku aspoň 13°C.
- **Filter počasia:** Obsahuje zoznam nepriaznivých stavov (dážď, sneženie), pri ktorých sa rekuperácia nevypne.
- **Hysterézia:** Časový zámok (15 minút) zabraňuje neustálemu zapínaniu a vypínaniu pri hraničných hodnotách.

## Technické detaily
- **Jazyk:** Python 3
- **Platforma:** Home Assistant (integrácia PyScript)
- **Kľúčové koncepty:** Logické operátory (`and`, `not in`), konverzia dátových typov (`float`), práca s listami.

## Môj progres
Toto je môj prvý projekt, kde som aplikoval základy Pythonu na reálny problém. Pomohlo mi to pochopiť:
1. Rozdiel medzi statickým kódom a udalosťami (triggers).
2. Dôležitosť ošetrenia vstupov zo senzorov.
3. Ako písať čistý a komentovaný kód, ktorý je ľahko udržiavateľný.
